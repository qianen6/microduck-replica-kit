#!/usr/bin/env python3
"""Export assembled Microduck reference STLs from the public MJCF model.

Adapted from the assembly-export method published in
https://github.com/fanhao375/microduck-replica (Apache-2.0).

Generated meshes remain derivative works of the upstream Microduck 3D models
and must retain their upstream CC BY-NC-SA attribution.
"""

from __future__ import annotations

import argparse
import json
import struct
import subprocess
from pathlib import Path

import mujoco
import numpy as np


MJCF = Path("src/mjlab_microduck/robot/microduck/robot_allcollisions.xml")

BODY_FILE_NAMES = {
    "trunk_base": "01_trunk",
    "yaw2roll": "02_left_hip_yaw_roll",
    "hip_l": "03_left_hip_roll",
    "upper_leg_left": "04_left_thigh",
    "leg": "05_left_shin",
    "ankle_left": "06_left_ankle_foot",
    "neck": "07_neck_base",
    "neck_pitch": "08_neck_pitch",
    "yaw_roll_motion": "09_head_yaw_roll",
    "jaw_soft": "10_head_beak_assembly",
    "bearing_roll": "11_right_hip_yaw_roll",
    "hip_l_2": "12_right_hip_roll",
    "upper_leg_right": "13_right_thigh",
    "leg_2": "14_right_shin",
    "ankle_right": "15_right_ankle_foot",
}


def write_binary_stl(path: Path, triangles: np.ndarray) -> None:
    with path.open("wb") as handle:
        handle.write(b"\0" * 80)
        handle.write(struct.pack("<I", len(triangles)))
        for triangle in triangles:
            normal = np.cross(triangle[1] - triangle[0], triangle[2] - triangle[0])
            length = np.linalg.norm(normal)
            normal = normal / length if length > 1e-12 else np.zeros(3)
            handle.write(struct.pack("<3f", *normal))
            for vertex in triangle:
                handle.write(struct.pack("<3f", *vertex))
            handle.write(b"\0\0")


def geom_triangles(model: mujoco.MjModel, data: mujoco.MjData, geom_id: int) -> np.ndarray | None:
    mesh_id = model.geom_dataid[geom_id]
    if mesh_id < 0:
        return None
    vertex_start = model.mesh_vertadr[mesh_id]
    vertex_count = model.mesh_vertnum[mesh_id]
    face_start = model.mesh_faceadr[mesh_id]
    face_count = model.mesh_facenum[mesh_id]
    vertices = model.mesh_vert[vertex_start : vertex_start + vertex_count].reshape(-1, 3)
    faces = model.mesh_face[face_start : face_start + face_count].reshape(-1, 3)
    rotation = data.geom_xmat[geom_id].reshape(3, 3)
    world_vertices = (vertices @ rotation.T) + data.geom_xpos[geom_id]
    return world_vertices[faces] * 1000.0


def git_head(path: Path) -> str | None:
    try:
        return subprocess.check_output(
            [
                "git",
                "-c",
                f"safe.directory={path.as_posix()}",
                "-C",
                str(path),
                "rev-parse",
                "HEAD",
            ],
            text=True,
            stderr=subprocess.DEVNULL,
        ).strip()
    except (subprocess.CalledProcessError, FileNotFoundError):
        return None


def export(source: Path, output: Path) -> dict:
    mjcf_path = source / MJCF
    if not mjcf_path.is_file():
        raise SystemExit(f"MJCF not found: {mjcf_path}")
    output.mkdir(parents=True, exist_ok=True)

    model = mujoco.MjModel.from_xml_path(str(mjcf_path))
    data = mujoco.MjData(model)
    data.qpos[:] = 0
    data.qpos[3] = 1.0
    mujoco.mj_forward(model, data)

    all_triangles: list[np.ndarray] = []
    bodies: list[dict] = []

    for body_id in range(1, model.nbody):
        body_name = mujoco.mj_id2name(model, mujoco.mjtObj.mjOBJ_BODY, body_id)
        body_parts: list[np.ndarray] = []
        source_meshes: list[str] = []
        for geom_id in range(model.ngeom):
            if model.geom_bodyid[geom_id] != body_id or model.geom_group[geom_id] != 2:
                continue
            triangles = geom_triangles(model, data, geom_id)
            if triangles is None:
                continue
            body_parts.append(triangles)
            source_meshes.append(
                mujoco.mj_id2name(
                    model, mujoco.mjtObj.mjOBJ_MESH, model.geom_dataid[geom_id]
                )
            )
        if not body_parts:
            continue

        triangles = np.concatenate(body_parts, axis=0)
        all_triangles.append(triangles)
        file_stem = BODY_FILE_NAMES.get(body_name, body_name)
        file_name = f"{file_stem}.stl"
        write_binary_stl(output / file_name, triangles)
        bodies.append(
            {
                "body": body_name,
                "file": file_name,
                "triangles": int(len(triangles)),
                "source_meshes": source_meshes,
            }
        )

    assembly = np.concatenate(all_triangles, axis=0)
    write_binary_stl(output / "00_microduck_reference_assembly.stl", assembly)
    points = assembly.reshape(-1, 3)
    extents = np.ptp(points, axis=0)

    manifest = {
        "source": "pollen-robotics/microduck_rl",
        "source_commit": git_head(source),
        "license": "CC BY-NC-SA (upstream 3D models and derivatives)",
        "body_count": len(bodies),
        "assembly_triangles": int(len(assembly)),
        "extents_mm": [round(float(value), 3) for value in extents],
        "bodies": bodies,
    }
    (output / "assembly-manifest.json").write_text(
        json.dumps(manifest, indent=2, ensure_ascii=False), encoding="utf-8"
    )
    return manifest


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("source", type=Path, help="Path to the locked microduck_rl checkout")
    parser.add_argument("output", type=Path, help="Output directory")
    parser.add_argument("--strict", action="store_true", help="Require the known reference counts")
    args = parser.parse_args()

    manifest = export(args.source.resolve(), args.output.resolve())
    extents = "x".join(f"{value:.1f}" for value in manifest["extents_mm"])
    if args.strict:
        expected = (15, 796_792, "144.1x141.0x264.0")
        observed = (manifest["body_count"], manifest["assembly_triangles"], extents)
        if observed != expected:
            raise SystemExit(f"REFERENCE_EXPORT FAIL expected={expected} observed={observed}")
    print(
        "REFERENCE_EXPORT PASS "
        f"bodies={manifest['body_count']} triangles={manifest['assembly_triangles']} "
        f"extents_mm={extents}"
    )


if __name__ == "__main__":
    main()
