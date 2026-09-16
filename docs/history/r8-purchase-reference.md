> 历史参考：对应旧版硬件/几何；不得视为 R9 当前 BOM、接线或打印放行。

## 2026-09-13：轴承与一次备料总表

本次重新读取正在打开的 Blender 场景，38 个打印件、15 个舵机和14个轴承，共67个对象的网格/变换与已审磁盘文件一致。轴承逐个测量内径、外径和宽度，不是只看文件名。原模型与未保存状态保留。

### A. 轴承：型号、尺寸和模型数量已直接核实

尺寸顺序统一为 **内径 × 外径 × 厚度**，单位 mm。选无凸缘、普通内圈宽度的径向深沟球轴承。

| 型号/订货描述 | 尺寸 mm | 模型实需 | 建议购买 |
|---|---|---:|---:|
| MR2216-ZZ，金属防尘盖 | 16×22×4 | 11 | 12 |
| 6700 开式，或明确标注 W3 的 3 mm 厚版本 | 10×15×3 | 3 | 4 |

大轴承分布：躯干两处、左右腿各三处、头颈三处，共11个。小轴承分布：左右脚踝各1个，头/喙侧1个，共3个。

MR2216-ZZ 的尺寸对应 [MBA 目录第117页](https://files.minibearings.au/pdf/catalogues/Bearings%20-%20Radial%20-%20Master%20List.pdf#page=117)。[Runstar 6700开式](https://www.runstarbearing.com/product/thin-section-ball-bearings-6700/) 为10×15×3；[ISK 6700ZZ](https://iskbearing.com/product-details/6700zz) 为10×15×4。订货以三个尺寸为准，标4 mm厚的6700ZZ/2RS不作为当前3 mm位置的直接替换。

### B. 螺丝：一次备料建议，与轴承的直接确认数量分开

**以下是备料数，不是全机实装净用量。** 为形成可执行的长度组合，对108个舵机候选固定位置临时采用“接收端兼容M2、啮合1.5–3.0 mm、尽量接近2.0 mm”的计算场景，再加入22个非舵机名义选型位置。模型未标注的HD-1910牙型和允许深度仍未被确认；若为塑料专用自攻牙，应使用匹配牙型的配套螺丝，而不是把机牙螺丝强行代用。

| 规格 | 场景计算分配，非实需 | 建议购买备料数 |
|---|---:|---:|
| M2×3 | 18 | 30 |
| M2×4 | 32 | 40 |
| M2×5 | 54 | 60 |
| M2×6 | 15 | 30 |
| M2×8 | 备用，未指定安装位 | 10 |
| M2.5×5 | 4 | 10 |
| M2.5×8 | 7 | 15 |

上述机牙备料选择平底承压的内六角圆柱头，常规304不锈钢即可；不要统一购买锥形沉头。对板卡螺丝还应核对实际螺帽外径与周围元件空间。M2×8列为备用，不声称模型必用10颗。

轴心原配螺丝和相机/镜头固定不被擅自计入场景130个安装位；源模型保留的偏孔与螺柱复查项仍见下文，采购备料不等于这些问题已经修复。

### C. 小配件

| 配件 | 模型明确使用量 | 建议购买 |
|---|---:|---:|
| M2薄平垫，参考内径2.2、外径4.0、厚0.3 mm | OpenRB 4片 | 10片 |
| M2.5薄平垫，参考内径2.7、外径4.5、厚0.3 mm | Pi 4片 | 10片 |
| M2普通螺母 | 通孔试配备用，不按必装件计算 | 10个 |
| M2.5普通螺母 | 通孔试配备用，不按必装件计算 | 10个 |

模型没有把所有1.6 mm导孔设计为热熔螺母孔；本表不建议直接往这些小孔压入热熔螺母。

### D. 逐个轴承对应

| 模型对象 | 型号对应 | 内径×外径×厚度 mm |
|---|---|---|
| `PART_01_trunk_base_seeed_bearing__configuration__22x16x4` | MR2216-ZZ | 16×22×4 |
| `PART_08_trunk_base_seeed_bearing__configuration__22x16x4` | MR2216-ZZ | 16×22×4 |
| `PART_10_yaw2roll_seeed_bearing__configuration__22x16x4` | MR2216-ZZ | 16×22×4 |
| `PART_12_hip_l_seeed_bearing__configuration__22x16x4` | MR2216-ZZ | 16×22×4 |
| `PART_16_upper_leg_left_seeed_bearing__configuration__22x16x4` | MR2216-ZZ | 16×22×4 |
| `PART_20_ankle_left_seeed_bearing__configuration_default` | 6700 OPEN / W3 (3 mm width) | 10×15×3 |
| `PART_25_neck_pitch_seeed_bearing__configuration__22x16x4` | MR2216-ZZ | 16×22×4 |
| `PART_27_yaw_roll_motion_seeed_bearing__configuration__22x16x4` | MR2216-ZZ | 16×22×4 |
| `PART_28_yaw_roll_motion_seeed_bearing__configuration__22x16x4` | MR2216-ZZ | 16×22×4 |
| `PART_34_jaw_soft_seeed_bearing__configuration_default` | 6700 OPEN / W3 (3 mm width) | 10×15×3 |
| `PART_45_bearing_roll_seeed_bearing__configuration__22x16x4` | MR2216-ZZ | 16×22×4 |
| `PART_47_hip_l_2_seeed_bearing__configuration__22x16x4` | MR2216-ZZ | 16×22×4 |
| `PART_48_upper_leg_right_seeed_bearing__configuration__22x16x4` | MR2216-ZZ | 16×22×4 |
| `PART_54_ankle_right_seeed_bearing__configuration_default` | 6700 OPEN / W3 (3 mm width) | 10×15×3 |

本次测量及备料假设数据（历史本地资料）

---
