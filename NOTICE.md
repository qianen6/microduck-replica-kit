# Attribution and license boundaries

This repository is an independent community reconstruction study of Pollen Robotics' Microduck. It is not affiliated with or endorsed by Pollen Robotics or Hugging Face.

## Upstream sources

| Source | Author | Relevant license |
|---|---|---|
| [pollen-robotics/microduck](https://github.com/pollen-robotics/microduck) | Pollen Robotics | Apache-2.0 |
| [pollen-robotics/microduck_rl](https://github.com/pollen-robotics/microduck_rl) | Pollen Robotics | Code: Apache-2.0; 3D models: CC BY-NC-SA |
| [fanhao375/microduck-replica](https://github.com/fanhao375/microduck-replica) | fanhao375 and contributors | Scripts: Apache-2.0; derived geometry: CC BY-NC-SA 4.0 |

The exact revisions used are recorded in `source-lock.json`.

## This repository

- Original documentation and code in this repository are released under Apache-2.0 unless a file states otherwise.
- `scripts/export_reference_assembly.py` is an adapted implementation of the MJCF assembly-export method published by `fanhao375/microduck-replica`; it remains Apache-2.0.
- `docs/images/exploded-view-concept.png` is an AI-assisted concept illustration derived from publicly visible Microduck appearance and reconstruction references. It is released under CC BY-NC-SA 4.0.
- Any generated STL or assembly drawing derived from the upstream Microduck 3D models must remain under CC BY-NC-SA 4.0 with attribution to Pollen Robotics and a link to `pollen-robotics/microduck_rl`.

Suggested attribution for generated geometry:

> Based on the Microduck simulation models by Pollen Robotics, licensed CC BY-NC-SA.  
> https://github.com/pollen-robotics/microduck_rl


## R9 publication

R9 Blender, STL and 3MF geometry derives from Microduck models by Pollen Robotics and the community reconstruction work credited above; shared under CC BY-NC-SA 4.0. Selected interface-clearance references: https://github.com/fanhao375/microduck-replica-cad/releases/tag/v2.0 . ROBOTIS bridge reference retains its original Apache-2.0 copyright header. Device envelope references are not original vendor open-hardware designs. The supplied community invitation image is provided for joining this project group only; no broader license is asserted.
