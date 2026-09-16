> 历史参考：对应旧版硬件/几何；不得视为 R9 当前 BOM、接线或打印放行。

# R8 螺丝、轴承与备料总表

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


## 结论

已重新读取当前 Blender 场景和磁盘 R8 浅紫黑装配文件；38 个装配打印件和 15 个 HD-1910 的网格、变换一致。当前场景的未保存状态保持不变，模型文件未保存、未修改。相机代理在当前场景与磁盘版本中不同，本次未覆盖当前场景。

**这份报告区分“孔位数量”“名义螺丝选型”和“实物适配”。当前模型没有完整的螺丝实体与螺纹数据，整机最终采购表仍有待定项。上一轮建议的短螺丝套装不是经确认的全机 BOM。**

## 1. 非舵机侧：22 个安装位的名义选型

下列新选型以接收孔形成对应公制螺纹为条件；打印导孔本身不等于现成机牙螺纹。型号中的长度按头下长度计。板卡规格沿用 R8 明文设计，其他规格由同轴孔、肩面、夹持厚度及底孔深度选取。未做实物螺纹拉脱、预紧、工具可达性或动态验证。

| 名义规格 | 安装位数量 | 分配 | 当前复核状态 |
|---|---:|---|---|
| M2×4 | 4 | OpenRB 四孔；配 0.3 mm 薄垫片 | 长度有余量；1 个接收柱的环向材料采样需要复查 |
| M2×6 | 7 | BNO 压片 2、开关压片 2、左右脚/踝连接各 1、左右躯干壳接合 1 | 长度有余量；1 个 BNO 接收柱需复查；躯干接合孔存在约 0.079 mm 轴线偏差 |
| M2.5×5 | 4 | Pi Zero 2 W 四孔；配 0.3 mm 薄垫片 | 长度有余量；2 个接收柱的环向材料采样需要复查 |
| M2.5×8 | 7 | 上下头壳 3、内部支架与下头壳 4 | 新增的条件选型；同轴孔及名义长度已复核 |
| 合计 | 22 | 不含舵机侧、轴心紧固、相机/镜头组件 | 不是整机螺丝总数 |

头型应保持平底承压。结构圆柱沉孔与锥形沉头孔不是一回事；目前长度表未等同于所有螺帽和工具均通过完整空间验证。

## 2. 舵机侧安装位已重新计数，牙型/长度待厂家资料

- 舵盘孔圈匹配到 **68 个独立安装位**。旧表的 54 个只是一个不完整子集。
- 机壳孔型匹配得到 42 个穿孔特征，底座/电源托架有 2 对共用轴线；去重后得到 **40 个候选紧固轴线**，其中 **39 处名义对齐，1 处偏置 0.50 mm**。
- 右躯干壳 `PART_02_trunk_base_right_shell` 的 `B027` 对应第 2 个舵机机壳候选孔，径向偏差 0.50 mm，超过 Ø2.2 过孔对 M2 螺杆的名义单边 0.10 mm 余量。该位置需要处理配合，再锁定装配。
- 四个轴心紧固候选位位于 `PART_09`、`PART_43`、`PART_17`、`PART_51`；中心螺丝是否使用舵机原配、是否需要换长，按厂家轴心螺纹和有效深度确认，不直接按 15×2 重复购买。
- 机壳接合位的夹持厚度约 0.8–3.2 mm，舵盘接合位约 1.8–4.3 mm。统一采用 M2×4 或 M2×6 会改变实际拧入深度，当前缺少厂家允许深度，故没有将其填成已确认型号。

厂家需补充：舵盘孔圈和机壳孔分别采用机牙还是塑料自攻/成形牙、名义直径与螺距、最大/推荐拧入深度、中心螺丝规格、随件数量。孔径 Ø1.6 不能替代以上螺纹标注。

### 舵盘孔圈安装位分布

| 打印件 | 安装位 |
|---|---:|
| `PART_02_trunk_base_right_shell` | 4 |
| `PART_07_trunk_base_left_shell` | 4 |
| `PART_09_yaw2roll_yaw2roll` | 4 |
| `PART_13_hip_l_hip_l` | 8 |
| `PART_17_leg_leg` | 4 |
| `PART_21_ankle_left_ankle_left` | 4 |
| `PART_24_neck_pitch_neck_pitch` | 12 |
| `PART_26_yaw_roll_motion_yaw_roll_motion` | 4 |
| `PART_38_jaw_soft_jaw` | 4 |
| `PART_43_bearing_roll_yaw2roll` | 4 |
| `PART_46_hip_l_2_hip_l` | 8 |
| `PART_51_leg_2_leg` | 4 |
| `PART_52_ankle_right_ankle_right` | 4 |

### 机壳候选轴线分布（共用穿孔已去重）

| 穿过的打印件 | 轴线数量 |
|---|---:|
| `PART_02_trunk_base_right_shell` | 1 |
| `PART_04_trunk_base_trunk_base` | 2 |
| `PART_04_trunk_base_trunk_base + PART_05_trunk_base_power_support` | 2 |
| `PART_05_trunk_base_power_support` | 2 |
| `PART_07_trunk_base_left_shell` | 1 |
| `PART_09_yaw2roll_yaw2roll` | 2 |
| `PART_11_yaw2roll_bearing_roll` | 2 |
| `PART_15_upper_leg_left_upper_leg_rigidity_plate` | 4 |
| `PART_17_leg_leg` | 2 |
| `PART_22_neck_neck` | 4 |
| `PART_23_neck_neck` | 4 |
| `PART_26_yaw_roll_motion_yaw_roll_motion` | 4 |
| `PART_43_bearing_roll_yaw2roll` | 2 |
| `PART_44_bearing_roll_bearing_roll` | 2 |
| `PART_49_upper_leg_right_upper_leg_rigidity_plate` | 4 |
| `PART_51_leg_2_leg` | 2 |

## 3. 保留问题与排除项

- 不计入旧 Robot HAT、旧 ToF 两个压片、5 个独立试装片的螺丝。
- 相机/镜头固定、旧 PCB 锁条和若干未配对预留孔未被擅自视为已确定装机螺丝。孔特征不按“一孔一颗”累计。
- R8 内支架按螺纹小径与大径之间的环向材料采样，P02、P04、P05，以及 BNO 位 P09 出现部分空缺样本。这是复查提示，不是拉脱强度试验结果。
- 上下头壳在原始闭合坐标下有约 67.89 mm³ 实体交集；本轮只记录，没有移动或修改头壳。数字孔位匹配不等同于整套打印件已实装通过。

## 4. 逐个非舵机侧连接的测量记录

| ID | 用途 | 规格 | 夹持厚度 mm | 名义啮合 mm | 到孔底余量 mm | 环向材料采样占比 | 状态 |
|---|---|---|---:|---:|---:|---:|---|
| P01 | Pi Zero 2 W | M2.5x5 | 1.900 | 3.100 | 1.200 | 1.000 | NOMINAL_LENGTH_FITS |
| P02 | Pi Zero 2 W | M2.5x5 | 1.900 | 3.100 | 1.200 | 0.958 | REVIEW_REQUIRED |
| P03 | Pi Zero 2 W | M2.5x5 | 1.900 | 3.100 | 1.200 | 1.000 | NOMINAL_LENGTH_FITS |
| P04 | Pi Zero 2 W | M2.5x5 | 1.900 | 3.100 | 1.200 | 0.875 | REVIEW_REQUIRED |
| P05 | OpenRB-150 | M2x4 | 1.900 | 2.100 | 1.400 | 0.542 | REVIEW_REQUIRED |
| P06 | OpenRB-150 | M2x4 | 1.900 | 2.100 | 1.400 | 1.000 | NOMINAL_LENGTH_FITS |
| P07 | OpenRB-150 | M2x4 | 1.900 | 2.100 | 1.400 | 1.000 | NOMINAL_LENGTH_FITS |
| P08 | OpenRB-150 | M2x4 | 1.900 | 2.100 | 1.400 | 1.000 | NOMINAL_LENGTH_FITS |
| P09 | BNO edge clamp | M2x6 | 0.700 | 5.300 | 0.650 | 0.833 | REVIEW_REQUIRED |
| P10 | BNO edge clamp | M2x6 | 1.550 | 4.450 | 0.650 | 1.000 | NOMINAL_LENGTH_FITS |
| P11 | Slide-switch retainer | M2x6 | 1.650 | 4.350 | 3.400 | 1.000 | NOMINAL_LENGTH_FITS |
| P12 | Slide-switch retainer | M2x6 | 1.650 | 4.350 | 3.400 | 1.000 | NOMINAL_LENGTH_FITS |
| P13 | Foot to ankle | M2x6 | 2.000 | 4.000 | 1.500 | 1.000 | NOMINAL_LENGTH_FITS |
| P14 | Foot to ankle | M2x6 | 2.000 | 4.000 | 1.500 | 1.000 | NOMINAL_LENGTH_FITS |
| P15 | Left/right trunk shell join | M2x6 | 2.800 | 3.200 | 1.500 | 1.000 | NOMINAL_LENGTH_FITS |
| P16 | Upper/lower head shell | M2.5x8 | 2.804 | 5.196 | 6.004 | 1.000 | NOMINAL_LENGTH_FITS |
| P17 | Upper/lower head shell | M2.5x8 | 2.804 | 5.196 | 6.004 | 1.000 | NOMINAL_LENGTH_FITS |
| P18 | Upper/lower head shell | M2.5x8 | 2.804 | 5.196 | 6.004 | 1.000 | NOMINAL_LENGTH_FITS |
| P19 | Internal carrier to lower head shell | M2.5x8 | 2.400 | 5.600 | 3.700 | 1.000 | NOMINAL_LENGTH_FITS |
| P20 | Internal carrier to lower head shell | M2.5x8 | 2.400 | 5.600 | 3.700 | 1.000 | NOMINAL_LENGTH_FITS |
| P21 | Internal carrier to lower head shell | M2.5x8 | 2.400 | 5.600 | 3.700 | 1.000 | NOMINAL_LENGTH_FITS |
| P22 | Internal carrier to lower head shell | M2.5x8 | 2.400 | 5.600 | 3.616 | 1.000 | NOMINAL_LENGTH_FITS |

## 5. 复核方法与文件

1. 对当前场景做只读网格导出，另外使用 Blender 后台打开磁盘文件导出对照；没有覆盖用户的未保存内容。
2. 从三角网格提取内凹圆柱面；同轴台阶/沉孔合并为一个孔特征，避免把孔口两面算成两颗螺丝。
3. 将孔轴与已保留的舵机运动学坐标、12 mm 舵盘孔圈和 30×16 mm 机壳名义孔型比较。
4. 对打印件之间的接收孔、夹持厚度、底孔余量进行复算，明确列出推断与待确认项。
5. 用带沉孔的合成样件回归测试确认“两段圆柱面对应一个紧固轴线”。

源模型：[LOCAL_PATH]

SHA-256：`65b51e8ec352e212dee833e8251a91c4132a9aabef6cf057ad519c725064edf5`

- 孔特征（历史本地资料）
- 接口去重与偏置记录（历史本地资料）
- 逐位名义选型（历史本地资料）
- 验证结果（历史本地资料）
- 可复现命令及字面输出（历史本地资料）
