#!/usr/bin/env python3
from __future__ import annotations

import argparse
import csv
import json
import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

REQUIRED = [
    "README.md",
    "LICENSE",
    "NOTICE.md",
    "source-lock.json",
    "hardware/BOM_REV_A.csv",
    "hardware/test-coupons.md",
    "docs/architecture-rev-a.md",
    "docs/domestic-actuators.md",
    "docs/cost-estimate.md",
    "docs/open-gaps.md",
    "docs/images/exploded-view-concept.png",
    "scripts/fetch_upstream.ps1",
    "scripts/export_reference_assembly.py",
    "ROLLBACK.sh",
]

SECRET_PATTERNS = [
    re.compile(r"ghp_[A-Za-z0-9]{20,}"),
    re.compile(r"github_pat_[A-Za-z0-9_]{20,}"),
    re.compile(r"sk-[A-Za-z0-9_-]{20,}"),
    re.compile(r"-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----"),
]


def fail(message: str) -> None:
    print(f"REPO_VALIDATE FAIL {message}")
    raise SystemExit(2)


def state(readme: Path) -> str:
    text = readme.read_text(encoding="utf-8-sig")
    match = re.search(r"repository_state:\s*([a-z_]+)", text)
    return match.group(1) if match else "missing"


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--mode", choices=("baseline", "modified"), required=True)
    parser.add_argument("--readme", type=Path, required=True)
    args = parser.parse_args()

    readme = args.readme.resolve()
    repo_state = state(readme)
    if args.mode == "baseline":
        if repo_state != "unpublished_skeleton":
            fail(f"state={repo_state} expected=unpublished_skeleton")
        print("REPO_VALIDATE BASELINE PASS state=unpublished_skeleton")
        return

    if repo_state != "public_ready":
        fail(f"state={repo_state} expected=public_ready")

    missing = [path for path in REQUIRED if not (ROOT / path).is_file()]
    if missing:
        fail(f"missing={','.join(missing)}")

    lock = json.loads((ROOT / "source-lock.json").read_text(encoding="utf-8"))
    if len(lock.get("sources", [])) != 3:
        fail("source_count")
    for source in lock["sources"]:
        if not re.fullmatch(r"[0-9a-f]{40}", source.get("commit", "")):
            fail(f"bad_commit={source.get('name')}")

    with (ROOT / "hardware/BOM_REV_A.csv").open(encoding="utf-8", newline="") as handle:
        rows = list(csv.DictReader(handle))
    servo_count = sum(
        int(row["quantity"])
        for row in rows
        if row["item"] == "Dynamixel XL330-M288-T"
    )
    if servo_count != 15:
        fail(f"servo_count={servo_count}")

    image = ROOT / "docs/images/exploded-view-concept.png"
    if image.read_bytes()[:8] != b"\x89PNG\r\n\x1a\n":
        fail("concept_image_not_png")

    forbidden_roots = [ROOT / ".venv", ROOT / "upstream", ROOT / "work"]
    if any(path.exists() for path in forbidden_roots):
        fail("forbidden_workspace_content")

    text_files = [
        path
        for path in ROOT.rglob("*")
        if path.is_file() and path.suffix.lower() in {".md", ".py", ".ps1", ".yml", ".yaml", ".json", ".csv", ".txt", ".sh"}
    ]
    for path in text_files:
        content = path.read_text(encoding="utf-8-sig", errors="replace")
        for pattern in SECRET_PATTERNS:
            if pattern.search(content):
                fail(f"secret_pattern={path.relative_to(ROOT)}")

    print(
        "REPO_VALIDATE MODIFIED PASS "
        f"state=public_ready required={len(REQUIRED)} sources=3 servos={servo_count} "
        f"image_bytes={image.stat().st_size} secrets=0"
    )


if __name__ == "__main__":
    main()
