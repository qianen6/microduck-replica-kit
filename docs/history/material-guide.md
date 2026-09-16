> 历史参考：对应旧版硬件/几何；不得视为 R9 当前 BOM、接线或打印放行。

# HD-1910 嘉立创3D打印材料选择清单

## 结论

材料判断可以由本清单完成，用户不需要逐个零件重新判断。嘉立创网页仍要求每个上传模型填写材料与工艺；用户可以按照本清单手动选择，也可以让Codex在已经登录的浏览器中代为填写。订单提交、工程审核后的最终确认和付款应当在核对数量与报价后执行。

## 推荐的首轮下单顺序

1. 用户先上传 `[LOCAL_PATH]`，并选择“PLA-P塑料／FDM熔融沉积”，数量选择1件。该件只用于验证孔位、舵盘、插头、线束和螺钉空间。
2. 用户在首件通过后上传一个关节或一条左腿所需的结构件，并选择“PA12尼龙／MJF多射流熔融”。
3. 用户把左鞋底选择为“TPU／FDM熔融沉积”，并先验证硬度、摩擦和尺寸。
4. 用户在单关节与单腿通过后再上传剩余零件，并按照下面的三组材料完成批量选择。

## 第一组：PA12尼龙／MJF多射流熔融

以下24个结构文件应当选择PA12尼龙：

- `PART_03_trunk_base_banana_pcb_locker.stl`
- `PART_04_trunk_base_trunk_base.stl`
- `PART_05_trunk_base_power_support.stl`
- `PART_09_yaw2roll_yaw2roll.stl`
- `PART_11_yaw2roll_bearing_roll.stl`
- `PART_13_hip_l_hip_l.stl`
- `PART_14_upper_leg_left_upper_leg_left.stl`
- `PART_15_upper_leg_left_rigidity_plate.stl`
- `PART_17_leg_leg.stl`
- `PART_19_ankle_left_foot_left.stl`
- `PART_21_ankle_left_ankle_left.stl`
- `PART_22_neck_neck.stl`
- `PART_23_neck_neck.stl`
- `PART_24_neck_pitch_neck_pitch.stl`
- `PART_26_yaw_roll_motion_yaw_roll_motion.stl`
- `PART_32_jaw_soft_motor_support.stl`
- `PART_43_bearing_roll_yaw2roll.stl`
- `PART_44_bearing_roll_bearing_roll.stl`
- `PART_46_hip_l_2_hip_l.stl`
- `PART_49_upper_leg_right_rigidity_plate.stl`
- `PART_50_upper_leg_right_upper_leg_right.stl`
- `PART_51_leg_2_leg.stl`
- `PART_52_ankle_right_ankle_right.stl`
- `PART_55_ankle_right_foot_right.stl`

用户还应当在尺寸验证通过后，把正式版 `HD1910_REAR_STATOR_ADAPTER.stl` 选择为PA12尼龙。适配片目标数量暂定15件，但用户应当根据单腿试装结果确认最终数量。

嘉立创当前PA12页面给出的工艺为MJF，标称公差为100毫米内±0.3毫米，推荐壁厚为1毫米。大腿加强板 `PART_15` 和 `PART_49` 的模型厚度正好约为1毫米，因此用户应当先打印一件验证，并避免直接批量下单。如果实物刚度不足，设计人员应当把厚度增加到1.5至2毫米，或者改用独立硬质板材。

如果PA12报价或交期不合适，用户可以把3201PA-F尼龙／SLS选择为备选，但用户仍应先打印一个关节验证轴承孔和螺钉孔尺寸。

## 第二组：JLC Black黑色树脂／SLA立体光固化

以下8个外观或精细装配文件可以选择JLC Black：

- `PART_02_trunk_base_right_shell.stl`
- `PART_07_trunk_base_left_shell.stl`
- `PART_30_jaw_soft_face_part.stl`
- `PART_33_jaw_soft_top_head_shell.stl`
- `PART_37_jaw_soft_noenoeil.stl`
- `PART_38_jaw_soft_jaw.stl`
- `PART_39_jaw_soft_bottom_head_shell.stl`
- `PART_40_jaw_soft_m12_lens_holder.stl`

JLC Black适合外壳、外观面和镜头座，并且它能提供比粉末尼龙更细腻的表面。用户如果更看重抗跌落而不是表面效果，也可以把这8个文件统一改选PA12尼龙。

## 第三组：TPU／FDM熔融沉积

以下4个柔性文件应当选择硬度95A的TPU：

- `PART_18_ankle_left_sole_left.stl`
- `PART_31_jaw_soft_jaw_soft.stl`
- `PART_36_jaw_soft_soft_mouth_top.stl`
- `PART_53_ankle_right_sole_right.stl`

嘉立创当前TPU页面给出的默认填充率为15%，材料硬度为95A。用户应当先打印一个鞋底，确认摩擦、回弹和厚度；如果网页自动检查提示最小尺寸或薄壁不合格，用户应当先停止该零件的批量下单，并根据工程审核意见修改模型。

## 不上传的装配占位文件

用户不应上传14个轴承网格、NP-F970电池网格、镜头网格、主控板网格、接口板网格和扬声器网格。用户应当采购这些真实部件。

## 嘉立创网页操作

1. 用户每次最多可以在报价页面同时上传10个模型，并应确保每个文件只包含一个模型。
2. 用户在“材料与规格”步骤为每个模型选择本清单指定的材料。
3. 嘉立创系统会自动检查尺寸、壁厚和重量，工程人员随后会进行人工可打印性审核。
4. 用户在工程审核通过后再次核对文件、材料、数量、颜色、后处理、报价和收货地址，再完成付款。

## 当前参考页面

- 嘉立创下单流程：https://jlc3dp.com/help/article/how-to-place-a-3d-printing-order
- 嘉立创PA12-HP尼龙：https://jlc3dp.com/help/article/pa12-hp-nylon
- 嘉立创3201PA-F尼龙：https://jlc3dp.com/help/article/3201pa-f-nylon
- 嘉立创PA12-CF塑料：https://jlc3dp.com/help/article/pa12-cf-plastic
- 嘉立创TPU：https://jlc3dp.com/help/article/tpu
- 嘉立创JLC Black：https://www.jlc-3dp.cn/materialDetail/282e5458e1724a469e7c802bb7fab2c8.html

---

changed_branch: material_batch_storage
changed_field: jlc3dp_filename_length_limit_50

## 按材质分类存放规则

1. 管理人员只把实际需要打印的模型复制到 `batches`，并把采购件占位模型留在源目录。
2. 管理人员用两位数字固定材料顺序：`00` 表示首件验证，`10` 表示PA12结构件，`20` 表示JLC Black外观件，`30` 表示TPU柔性件。
3. 管理人员在每个材料目录内按嘉立创单次最多10个模型的限制建立 `批次_A`、`批次_B`、`批次_C` 子目录。
4. 管理人员把批量副本的文件名连同扩展名限制在50个字符以内，并在清单的来源路径中保留原始文件名。
5. 管理人员不把不同材质的文件放入同一个上传批次，也不把轴承、电池、主控板、镜头或扬声器占位模型放入上传目录。
6. 操作者先提交 `00_首件验证_PLA-P_FDM`，并在首件通过后再提交PA12、JLC Black和TPU批次。
7. 操作者把 `10_结构件_PA12_MJF` 中的正式适配片数量暂时保留为“待单腿验证，最多15件”，并在验证后填写最终数量。
8. 操作者每次下单前按照 `BATCH_MANIFEST.csv` 核对目录、文件、材料、工艺、数量和放行状态。

## 目录结构

```text
batches/
├─ 00_首件验证_PLA-P_FDM/
│  └─ 批次_A_01件/
├─ 10_结构件_PA12_MJF/
│  ├─ 批次_A_10件/
│  ├─ 批次_B_10件/
│  └─ 批次_C_05件/
├─ 20_外观件_JLC_Black_SLA/
│  └─ 批次_A_08件/
└─ 30_柔性件_TPU_FDM/
   └─ 批次_A_04件/
```

## 放行规则

- 首件验证批次只有在孔位、舵盘、插头、线束和螺钉空间全部通过后才会放行正式结构批次。
- PA12结构批次只有在单关节与单腿通过后才会批量提交。
- JLC Black外观批次只有在外观面方向、颜色和后处理得到确认后才会提交。
- TPU批次只有在一个鞋底完成硬度、摩擦、回弹和尺寸验证后才会提交其余柔性件。
- 任何批次只要出现薄壁、最小尺寸或人工审核问题，操作者就会停止该批次，并只修改被拒绝的模型。


## 文件名长度规则

1. 管理人员把批量上传目录中的每个文件名连同 `.stl` 扩展名限制在50个字符以内。
2. 管理人员保留 `PART_编号` 前缀，并优先删除重复出现的模块名称。
3. 管理人员只重命名批量目录中的副本，并让源模型继续保留原始名称。
4. `BATCH_MANIFEST.csv` 的“文件名”列记录短名称，“来源路径”列记录原始名称，从而保持一一对应关系。
5. 左大腿加强板从 `PART_15_upper_leg_left_upper_leg_rigidity_plate.stl` 缩短为 `PART_15_upper_leg_left_rigidity_plate.stl`。
6. 右大腿加强板从 `PART_49_upper_leg_right_upper_leg_rigidity_plate.stl` 缩短为 `PART_49_upper_leg_right_rigidity_plate.stl`。
