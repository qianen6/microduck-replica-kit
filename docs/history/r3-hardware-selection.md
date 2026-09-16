> 历史参考：对应旧版硬件/几何；不得视为 R9 当前 BOM、接线或打印放行。

# Microduck硬件定选与实施方案

> 一套明确的样机硬件主选方案，含采购、接线、改模和验证顺序。

**生成日期:** 2026-09-05

**预计总投入:** 首轮工程时间盒40小时；非交货承诺，物流、返工和完整步态训练另计

---

## 1. 已确认的用户需求简报

- **目标:** 确定一台Microduck复刻样机采用的部件和制作路线，减少反复购买和凭占位图打印。
- **当前起点:** 已有RA2静态模型和采购表；用户指定HD-1910-C001资料包。附件SHA-256：252dad0edfd1560d9bfe5561e065ce00294942c0ce94806dbf183d2f08c6c105，与项目留档相同；图纸页1与照片是舵机参数来源。
- **可用时间:** 按首轮40小时工程时间盒拆解；并非用户已承诺可用工时。
- **语言:** 中文
- **偏好形式:**
  - 决策表
  - 厂家图纸/规格
  - 接线与实施说明
- **期望深度:** 可实施的样机选型；不等同制造放行
- **限制条件:**
  - 保留用户指定舵机路线。
  - 优先可追溯规格与接口，接受为真实硬件修改外壳。
  - 不实际下单，不把未测参数写成已验证。
- **假设:**
  - 目标是一台可开发验证的复刻样机，不追求所有模块立即照搬原厂闭源硬件。
  - PCB交由有电路/布线能力的工程人员与SMT厂实施，先样机后扩量。
  - 预算未指定，优先原厂/授权可追溯件；报价与到货版本另取回执。
- **时间安排边界:**
  - **可用总时长:** 2400 分钟
  - **单次建议时长:** 60 分钟
  - **机动时间比例:** 15%

## 2. 核心指南

### 直接结论

采用本清单的25条主选：HD1910不变，标准2S Gens ace动力电池、Radxa 4GB/32GB与原配Camera 8M219、Pololu升降压/ToF、SparkFun躯干IMU、明确声学件、真实外置急停。两块板按R3架构自制；新硬件入模后再决定整套打印。 [E_battery](#evidence-E_battery) [E_camera](#evidence-E_camera) [E_buck](#evidence-E_buck) [E_imu](#evidence-E_imu) [E_estop](#evidence-E_estop)

### 下一步行动

- **行动:** 先按首批栏拿样件并保存订货回执；把附件中型号混用、协议/控制表和持续负载定义交给舵机厂家补齐。先执行空载/轻载台架验证，再进入承载。
- **时间:** 首个90分钟工作时段
- **预期产出:** 一张带准确型号、配件和资料版本的首批清单
- **证据说明:** [E_debug](#evidence-E_debug) [E_battery](#evidence-E_battery) [E_camera_cable](#evidence-E_camera_cable)

### 真正重要的点

- 官方Radxa相机的32×32板框与旧25×24占位有明确差异，相机托应重画。 [E_camera](#evidence-E_camera)
- 电池与5V供电按高倍率标准LiPo和升降压路线选定；不用未注明放电能力的相机电池作默认动力电源。 [E_battery](#evidence-E_battery) [E_buck](#evidence-E_buck)
- 平衡IMU固定在躯干且需要软件后端修改；头部IMU标记不等于这颗实物传感器。 [E_runtime](#evidence-E_runtime) [E_rl](#evidence-E_rl) [E_imu](#evidence-E_imu)
- 急停只硬切舵机、主控保留供电；所有新方案仍需实机验证。 [E_estop](#evidence-E_estop) [E_power](#evidence-E_power)

### 具体建议

#### 主选：Radxa Camera 8M219 + 原配FPC

- **适合:** 优先接口可追溯与主控配套
- **原因:** 厂家明确支持ZERO3，具有尺寸图与线缆说明。
- **取舍与限制:** 32mm板需要改托架；视角与160°广角模块不同。
- **证据说明:** [E_camera](#evidence-E_camera) [E_camera_cable](#evidence-E_camera_cable)

#### 备选：Waveshare IMX219-160 非IR版，本轮不采购

- **适合:** 把广角视场作为优先目标时
- **原因:** 有明确25×24板框和160°版本。
- **取舍与限制:** 仍需FPC/驱动/光学校验，不作为无改动替换。
- **证据说明:** [E_alt_camera](#evidence-E_alt_camera)

#### 备选：USB TO AUDIO，本轮不采购

- **适合:** 接受另改头部空间、希望减少音频PCB开发时
- **原因:** 现成USB音频模块可缩短模拟电路开发。
- **取舍与限制:** 需USB布线和ALSA适配，本轮选择保留aic3104路线。
- **证据说明:** [E_alt_audio](#evidence-E_alt_audio) [E_codec](#evidence-E_codec)


### 确定采用的硬件与采购顺序

> **本节回答:** 每组只给一个主选型号；首批为0的PCB内含件由板厂配料，避免重复购买。

#### A01 舵机：FEETECH HD-1910-C001（用户指定附件款）

整机15；首批1。附件：本体34×20×23mm，总跨距29mm，孔距30×16mm；资料标称5–8.4V。 安装：原厂舵盘与线束成套，先单关节。 改模：15处安装接口逐一验证；不从混名STEP推定全部固定件相同。 验证：PDF写HD-1910M，STEP文件名HD-1915；缺协议表/连续负载定义。

**具体例子:** 收货记录：FEETECH HD-1910-C001（用户指定附件款）；首批1；型号标签和尺寸照片。

**证据说明:** [E_debug](#evidence-E_debug)

#### C01 主控：Radxa ZERO 3W 4GB RAM + 32GB eMMC，带40针排针；按V1.12/AIC8800询价

整机1；首批1。板框65×30mm；选3W，不替换3E或旧Zero。 安装：保留GPIO配套，安装在头部；与5519A一起入模。 改模：重核版本、元件高度、叠板与散热包络。 验证：实物丝印/内存/eMMC/无线芯片与订单一致。

**具体例子:** 收货记录：Radxa ZERO 3W 4GB RAM + 32GB eMMC，带40针排针；按V1.12/AIC8800询价；首批1；型号标签和尺寸照片。

**证据说明:** [E_radxa](#evidence-E_radxa) [E_radxa_versions](#evidence-E_radxa_versions)

#### C05 散热：Radxa Heatsink 5519A

整机1；首批1。官方ZERO 3W/3E配套型号；完整高度待实物/CAD。 安装：保留天线区域和散热风道。 改模：头壳与HAT叠高重新检查。 验证：封闭头壳下CPU温度与降频测试。

**具体例子:** 收货记录：Radxa Heatsink 5519A；首批1；型号标签和尺寸照片。

**证据说明:** [E_heat](#evidence-E_heat)

#### C06 板间连接：Samtec SSW-120-02-G-D；M2.5母母铜柱12mm

整机1；首批1。40针双排2.54mm；铜柱12mm为初版装配起点。 安装：螺钉与绝缘垫固定，检查排针有效插入深度。 改模：用真实插接组合替换原6mm方块占位。 验证：逐处确认螺钉长度、铜柱接触和电气绝缘。

**具体例子:** 收货记录：Samtec SSW-120-02-G-D；M2.5母母铜柱12mm；首批1；型号标签和尺寸照片。

**证据说明:** [E_header](#evidence-E_header)

#### P02 电池：Gens ace GEA8502S60E2

整机1；首批1。标准LiPo，2S/7.4V/850mAh/60C；约58×32×20mm、55g；EC2+JST-XHR-3P。 安装：保留原厂电池线头；改为圆角托盘与绑带，插头出线侧留缓冲。 改模：原NP-F滑轨/触点锁扣退役；电池座重画。 验证：外形约值与动态电流、保护/低电压需实测。

**具体例子:** 收货记录：Gens ace GEA8502S60E2；首批1；型号标签和尺寸照片。

**证据说明:** [E_battery](#evidence-E_battery)

#### P03 充电：SkyRC B6neo SK-100198

整机1；首批1。标准LiPo 2S平衡充电；首轮0.8A；满电总电压8.4V。 安装：电池取下后接主线及3针平衡口；配成品EC2充电线。 改模：充电器留在机外。 验证：按该型号说明书核对模式与极性，不选LiHV/3S。

**具体例子:** 收货记录：SkyRC B6neo SK-100198；首批1；型号标签和尺寸照片。

**证据说明:** [E_charger](#evidence-E_charger) [E_battery](#evidence-E_battery)

#### P04 主控5V：Pololu S13V30F5 #4082

整机1；首批1。5V升降压，典型约3A，22.9×22.9×9.7mm。 安装：接电池主保险后的独立3A逻辑支路，急停不断这一路。 改模：比D24V50F5更大，支架及间隙重查。 验证：6.4–8.4V输入与0–2.5A负载下测输出、温升和启动。

**具体例子:** 收货记录：Pololu S13V30F5 #4082；首批1；型号标签和尺寸照片。

**证据说明:** [E_buck](#evidence-E_buck)

#### E04 电源与TTL板：自制 PWR-SERVO-R3

整机1；首批0。34×42mm为板框目标；LM74502DDFR+2×CSD18540Q5B；逻辑/舵机分支分开。 安装：共源背靠背NFET；NC急停+上电默认关断/手动ARM；主干分路注入。 改模：按真实贴片保险丝、电容、接线焊盘重新布局。 验证：原理图/PCB/SMT尚未生产；需回馈尖峰、UVLO、保护和热测。

**具体例子:** 收货记录：自制 PWR-SERVO-R3；首批0；型号标签和尺寸照片。

**证据说明:** [E_power](#evidence-E_power) [E_power_reverse](#evidence-E_power_reverse) [E_fet](#evidence-E_fet) [E_fuse](#evidence-E_fuse)

#### E05 音频与接口板：自制 AUDIO-HAT-R3

整机1；首批0。65×30mm、4层1.6mm目标；TLV320AIC3104IRHBR+TPA2010D1YZF；12MHz时钟。 安装：保留项目I2S3/I2C3和aic3104卡名；模拟3.3/1.8V，数字3.3V单独供电。 改模：与散热器、相机、排针同时定叠高；尚非Gerber。 验证：供电时序、录放音、噪声、EMI和布线复核。

**具体例子:** 收货记录：自制 AUDIO-HAT-R3；首批0；型号标签和尺寸照片。

**证据说明:** [E_codec](#evidence-E_codec) [E_amp](#evidence-E_amp) [E_gpio](#evidence-E_gpio) [E_runtime](#evidence-E_runtime)

#### E07 数字3.3V：TPS62162DSGR（HAT内置）

整机1；首批0。1A降压；供ToF、NFC等数字负载，模拟LDO与其分开。 安装：放在HAT数字区，按TI参考电路布置。 改模：新增电感/电容空间，不能只放芯片方块。 验证：SMT供货确认；电流预算与纹波测试。

**具体例子:** 收货记录：TPS62162DSGR（HAT内置）；首批0；型号标签和尺寸照片。

**证据说明:** [E_digital_supply](#evidence-E_digital_supply)

#### S01 平衡IMU：SparkFun Micro LSM6DSV16X SEN-21336

整机1；首批1。7.62×19.05mm板框；3.3V；I2C 0x6B。 安装：刚性固定在躯干，接独立I2C4的27/28；保留坐标标识。 改模：增加躯干小卡座；头部功能标记不充当平衡IMU实体。 验证：新增I2C/SFLP后端并校准坐标；移除对ID200应答的依赖。

**具体例子:** 收货记录：SparkFun Micro LSM6DSV16X SEN-21336；首批1；型号标签和尺寸照片。

**证据说明:** [E_imu](#evidence-E_imu) [E_imu_product](#evidence-E_imu_product) [E_gpio](#evidence-E_gpio) [E_runtime](#evidence-E_runtime) [E_rl](#evidence-E_rl)

#### S02 测距：Pololu VL53L8CX #3419

整机1；首批1。约13×23×3mm；VIN=3.3V，I2C默认7-bit 0x29。 安装：头部前向；SPI/I2C脚接GND，SDA/SCL接I2C3；线长目标≤60mm。 改模：补实体支架与通光开口。 验证：读距、壳体遮挡/反射与总线负载测试。

**具体例子:** 收货记录：Pololu VL53L8CX #3419；首批1；型号标签和尺寸照片。

**证据说明:** [E_tof](#evidence-E_tof)

#### S03 相机：Radxa Camera 8M 219（含ZERO 3配套FPC）

整机1；首批1。板32±0.2mm见方；孔距28±0.1mm；镜头前凸15.98±0.2mm；PCB1.6mm。 安装：使用原配150mm同面22P 0.5→15P 1.0mm排线。 改模：旧25×24相机占位不适用；相机托、镜头座和面罩重画。 验证：前凸不是总厚，需加背部FPC座；视频和内参重标定。

**具体例子:** 收货记录：Radxa Camera 8M 219（含ZERO 3配套FPC）；首批1；型号标签和尺寸照片。

**证据说明:** [E_camera](#evidence-E_camera) [E_camera_cable](#evidence-E_camera_cable)

#### S05 麦克风：Same Sky CMC-4015-25T

整机1；首批1。顶入声模拟驻极体，直径4mm、高1.5mm。 安装：独立胶套/卡座，短线接AIC3104麦克风输入。 改模：按真实厚度、声孔和导声路径重画。 验证：按数据表偏置条件设置MICBIAS与负载，测底噪/灵敏度。

**具体例子:** 收货记录：Same Sky CMC-4015-25T；首批1；型号标签和尺寸照片。

**证据说明:** [E_mic](#evidence-E_mic) [E_codec](#evidence-E_codec)

#### E06 扬声器：PUI Audio AS02008MR-HT-WP

整机1；首批1。20mm直径、3.9mm高、8Ω、额定1.2W。 安装：前后声腔隔离，独立密封圈，接TPA2010差分功率输出。 改模：扬声器托与声孔重画。 验证：校准限幅；8Ω负载2.5Vrms约0.78W作为初始音量测试点。

**具体例子:** 收货记录：PUI Audio AS02008MR-HT-WP；首批1；型号标签和尺寸照片。

**证据说明:** [E_speaker](#evidence-E_speaker) [E_amp](#evidence-E_amp)

#### S06 NFC：Seeed Grove NFC(PN532) 113020006 + 原配天线

整机2；首批1。控制板25.43×20.35mm；天线约28×30.5mm；3.3V。 安装：首轮一套试读，最终两套分走UART4/5；天线分别靠近头盖和喙部非金属区域。 改模：增加板卡与天线固定，避开金属/散热片。 验证：补NFC程序与读距测试；保持原馈线长度，第二套后补。

**具体例子:** 收货记录：Seeed Grove NFC(PN532) 113020006 + 原配天线；首批1；型号标签和尺寸照片。

**证据说明:** [E_nfc](#evidence-E_nfc) [E_nfc_wiring](#evidence-E_nfc_wiring) [E_nfc_antenna](#evidence-E_nfc_antenna) [E_gpio](#evidence-E_gpio)

#### P07 急停：IDEC XA1E-BV302-R

整机1；首批1。16mm安装系列、29mm蘑菇头、2NC。 安装：首版外置有线控制盒；一路NC硬切舵机使能，另一路状态检测；复位后需重新ARM。 改模：旧小按钮占位与12.6mm开孔取消或改控制线出口。 验证：断线/按下/复位/上电顺序均测试，逻辑电源保持。

**具体例子:** 收货记录：IDEC XA1E-BV302-R；首批1；型号标签和尺寸照片。

**证据说明:** [E_estop](#evidence-E_estop) [E_power](#evidence-E_power)

#### FMAIN 主保险丝：Littelfuse 0451015.MRL

整机1；首批0。451系列15A，6.10×2.69×2.69mm。 安装：靠电池入口布置，额定值作为首版样机起点。 改模：删除旧汽车片式保险丝座占位。 验证：最终按电流波形、I²t、导线与PCB温升复核。

**具体例子:** 收货记录：Littelfuse 0451015.MRL；首批0；型号标签和尺寸照片。

**证据说明:** [E_fuse](#evidence-E_fuse)

#### FBRANCH 舵机支路保险丝：Littelfuse 0451005.MRL

整机3；首批0。451系列5A，每组5舵机一路，首版样机值。 安装：三路分支分别保护，主干后分点供电，不让首颗细线承担整组电流。 改模：按贴片封装重布电源板。 验证：不是精确电机限流器；过载保护与正常瞬态区分。

**具体例子:** 收货记录：Littelfuse 0451005.MRL；首批0；型号标签和尺寸照片。

**证据说明:** [E_fuse](#evidence-E_fuse)

#### FLOGIC 逻辑支路保险丝：Littelfuse 0451003.MRL

整机1；首批0。451系列3A，位于5V变换器输入侧。 安装：急停之前分出逻辑支路，断总电源仍用电池插头。 改模：更新配电走线及熔断器分组。 验证：检查冷启动和满负载浪涌。

**具体例子:** 收货记录：Littelfuse 0451003.MRL；首批0；型号标签和尺寸照片。

**证据说明:** [E_fuse](#evidence-E_fuse) [E_buck](#evidence-E_buck)

#### CAP 支路储能：Panasonic EEUFR1C471

整机3；首批0。16V、470µF、直径8mm、长11.5mm。 安装：横置并固定，引脚/外壳绝缘，靠近分支。 改模：旧10mm长度占位增加1.5mm。 验证：纹波、额定寿命及回馈电压测试。

**具体例子:** 收货记录：Panasonic EEUFR1C471；首批0；型号标签和尺寸照片。

**证据说明:** [E_cap](#evidence-E_cap)

#### E02 台架调试：FEETECH FE-URT1-C001

整机1；首批1。52×38.4×16mm，USB转TTL/485，最高1Mbps。 安装：只放台架，选TTL通道；电源按HD1910限制设定。 改模：不塞入鸭子机身。 验证：工具支持TTL不等于HD1910协议兼容已证明。

**具体例子:** 收货记录：FEETECH FE-URT1-C001；首批1；型号标签和尺寸照片。

**证据说明:** [E_debug](#evidence-E_debug)

#### W01 舵机端线束：HD-1910原厂配套线束，按实际插座批次

整机15；首批2。端子规格、针序由厂家对这批HD1910确认。 安装：保留原厂端子；D/V/G按标记与连通性核对，不凭线色推定。 改模：完整插头、应力缓冲和全行程线束加入模型。 验证：原包未明确的端子尺寸仍需厂家回执。

**具体例子:** 收货记录：HD-1910原厂配套线束，按实际插座批次；首批2；型号标签和尺寸照片。

**证据说明:** [E_debug](#evidence-E_debug)

#### W02 电源主干：W-PWR-R3：EC2设备端输入；18AWG高股数硅胶红黑线

整机1；首批1。电池保留原厂EC2；机器人侧加工成品配套线束。 安装：输入和回流同线规；三支路接AMASS XT30U成对插头；信号另走。 改模：建完整对接外形而非单端小方块。 验证：极性、端子版本、接触压降与拉脱力检查。

**具体例子:** 收货记录：W-PWR-R3：EC2设备端输入；18AWG高股数硅胶红黑线；首批1；型号标签和尺寸照片。

**证据说明:** [E_battery](#evidence-E_battery) [E_fuse](#evidence-E_fuse)

#### W03 传感器与急停线束：Qwiic JST-SH-4；Grove原配线；急停JST-GH-4成对线束

整机1；首批1。传感器逻辑统一3.3V；SH 1.0mm与GH 1.25mm分开。 安装：传感器各按丝印接，急停只走低电流控制；转轴附近留随动弯线。 改模：逐根定义净空和弯折区域；首版线长留余量后实装裁定。 验证：端子、屏蔽/回流、极限角不夹线检查。

**具体例子:** 收货记录：Qwiic JST-SH-4；Grove原配线；急停JST-GH-4成对线束；首批1；型号标签和尺寸照片。

**证据说明:** [E_gpio](#evidence-E_gpio) [E_tof](#evidence-E_tof) [E_imu](#evidence-E_imu) [E_nfc_wiring](#evidence-E_nfc_wiring)


### 两块自制板怎么做

> **本节回答:** 给出实现边界，不把机械板框当成现成电子板。

#### 配电分成常供逻辑和可断舵机两路

电池→主保险丝→节点A。A→3A逻辑保险丝→S13V30F5→5V_LOGIC；A→LM74502+共源背靠背NFET→三路5A保险丝→15舵机。所有额定值是首版测试值，不是已实测工作电流。

**具体例子:** 核对位置：p1 / Pin functions / Typical application

**证据说明:** [E_power](#evidence-E_power) [E_buck](#evidence-E_buck) [E_fuse](#evidence-E_fuse)

#### 急停与手动复位

IDEC的NC回路打开或线缆断开即硬件关断舵机使能；另一个NC作状态检测。上电默认关断，松开急停后仍等待ARM。主控逻辑电源保持，便于记录故障和正常关机。逻辑闭锁电路属于PWR板设计任务，尚未在实机验证。

**具体例子:** 核对位置：Key Features / Mechanical Specifications

**证据说明:** [E_estop](#evidence-E_estop) [E_power](#evidence-E_power)

#### 逻辑常供仍有欠压截止

常供只表示急停时保留主控，不表示无限放电。项目初始目标为6.6V预警/系统关机、6.4V舵机关闭、6.2V逻辑硬截止并锁定；升降压2.8V最低输入不是2S电池截止值。逐节欠压与失衡检查纳入PWR设计，阈值需结合公差、压降和实测修订。

**具体例子:** 核对位置：Product Specs：Capacity、Voltage、C rate、Dimensions、Balance Plug、Discharge Plug

**证据说明:** [E_battery](#evidence-E_battery) [E_buck](#evidence-E_buck) [E_power](#evidence-E_power)

#### 回馈与欠压不照搬旧值

选择LM74502而非原LM74800，导通时保留回馈到电池的路径。关断后仍需处理母线回馈尖峰。UVLO目标约6.4V，但电阻值需按新芯片阈值/公差重算；SMBJ12A不是8.4V舵机保护的充分方案。

**具体例子:** 核对位置：p1 / Pin functions / Typical application

**证据说明:** [E_power](#evidence-E_power) [E_power_reverse](#evidence-E_power_reverse) [E_battery](#evidence-E_battery)

#### 音频主路线保持AIC3104

AUDIO-HAT-R3沿用AIC3104+TPA2010D1和12MHz时钟，目标65×30mm、4层1.6mm。模拟3.3V/内核1.8V与数字3.3V分区。QFN/小封装由SMT厂贴装，先确认电路再固定板框。

**具体例子:** 核对位置：Pin functions / Power / Digital interface

**证据说明:** [E_codec](#evidence-E_codec) [E_amp](#evidence-E_amp) [E_header](#evidence-E_header)

#### 新增数字3.3V供电

TPS62162 1A数字电源供测距/NFC等负载；旧300mA模拟LDO不承担所有模块。设计预算为ToF 150mA+双NFC 166mA+IMU及其他余量，而非实测功耗。供货由SMT厂确认。

**具体例子:** 核对位置：Features / Part details

**证据说明:** [E_digital_supply](#evidence-E_digital_supply) [E_tof](#evidence-E_tof) [E_nfc_wiring](#evidence-E_nfc_wiring)

#### 线束按功能加工

舵机端保留原厂端子与线序证据。主供电/回流同线规，信号与大电流分开；每腿分点供电。CSI在头内使用原配线；颈部线束留随动弯曲，不穿实心轴，逐关节扫角后确定最终线长。

**具体例子:** 核对位置：Default FPC / FPC Cable

**证据说明:** [E_camera_cable](#evidence-E_camera_cable) [E_gpio](#evidence-E_gpio) [E_debug](#evidence-E_debug)


### 接线与软件要同步改的部分

> **本节回答:** 以下为接口分配方案；设备树、Linux设备节点和实际电气状态仍须在样机上核对。

#### GPIO2/4 · 5V_LOGIC

S13V30F5输出。两根5V及足够地针共同供电；与USB供电不并联

**具体例子:** 核对位置：40 PIN GPIO / Debug Serial / MIPI CSI

**证据说明:** [E_gpio](#evidence-E_gpio) [E_runtime](#evidence-E_runtime)

#### GPIO8 / 10 · UART2 TX / RX

PWR板TTL电路→HD1910。关闭串口控制台/引导输入干扰后使用

**具体例子:** 核对位置：40 PIN GPIO / Debug Serial / MIPI CSI

**证据说明:** [E_gpio](#evidence-E_gpio) [E_runtime](#evidence-E_runtime)

#### GPIO3 / 5 · I2C3 SDA / SCL

AIC3104 0x18 + ToF 0x29。沿用项目对应overlay；检查总线上拉组合

**具体例子:** 核对位置：40 PIN GPIO / Debug Serial / MIPI CSI

**证据说明:** [E_gpio](#evidence-E_gpio) [E_runtime](#evidence-E_runtime)

#### GPIO12 / 35 / 40 / 38 · I2S3 BCLK / LRCLK / TX / RX

AUDIO-HAT-R3。12MHz独立codec时钟；保留aic3104卡名

**具体例子:** 核对位置：40 PIN GPIO / Debug Serial / MIPI CSI

**证据说明:** [E_gpio](#evidence-E_gpio) [E_runtime](#evidence-E_runtime)

#### GPIO27 / 28 · I2C4 SDA / SCL

躯干LSM6DSV16X 0x6B。保持默认GPIO/I2C布线，不改成USB信号

**具体例子:** 核对位置：40 PIN GPIO / Debug Serial / MIPI CSI

**证据说明:** [E_gpio](#evidence-E_gpio) [E_runtime](#evidence-E_runtime)

#### GPIO16 / 18 · UART4 RX / TX

头部Grove NFC TX / RX。3.3V UART，模块保留默认UART模式

**具体例子:** 核对位置：40 PIN GPIO / Debug Serial / MIPI CSI

**证据说明:** [E_gpio](#evidence-E_gpio) [E_runtime](#evidence-E_runtime)

#### GPIO33 / 32 · UART5 RX / TX

喙部Grove NFC TX / RX。独立串口避免同地址I2C模块冲突

**具体例子:** 核对位置：40 PIN GPIO / Debug Serial / MIPI CSI

**证据说明:** [E_gpio](#evidence-E_gpio) [E_runtime](#evidence-E_runtime)

#### GPIO7 / 11 / 15 · ESTOP_STATUS / SOFTWARE_KILL / BAT_LOW

PWR板控制接口。软件只可附加关断，NC硬断链优先；低电量先通知主控关机

**具体例子:** 核对位置：40 PIN GPIO / Debug Serial / MIPI CSI

**证据说明:** [E_gpio](#evidence-E_gpio) [E_runtime](#evidence-E_runtime)

#### GPIO6/9/14/20/25/30/34/39 · GND

公共信号参考/电源回流。电机大电流不通过传感器细地线返回

**具体例子:** 核对位置：40 PIN GPIO / Debug Serial / MIPI CSI

**证据说明:** [E_gpio](#evidence-E_gpio) [E_runtime](#evidence-E_runtime)

#### IMU不再伪装成ID200设备

使用同型号LSM6DSV16X，但通过独立I2C4读取SFLP。新增I2C后端并从电机同步读ID列表移除200，将带时间戳的陀螺仪/四元数交给Sensors。保持单位、躯干坐标、过期检测和就绪条件；零样本不当作正常姿态。

**具体例子:** 核对位置：Board Outline / I2C / Power

**证据说明:** [E_imu](#evidence-E_imu) [E_runtime](#evidence-E_runtime) [E_rl](#evidence-E_rl)

#### 相机尺寸已实证纠正

Radxa官方图纸是32×32mm，旧模型25×24mm占位需要改。孔距28mm；镜头前凸15.98mm之外还有PCB和背部连接器。使用原配同面转接FPC，优先官方支持链路，接受广角范围不同并重新标定。

**具体例子:** 核对位置：印刷页5 Physical specifications；页4 FPC

**证据说明:** [E_camera](#evidence-E_camera) [E_camera_cable](#evidence-E_camera_cable) [E_alt_camera](#evidence-E_alt_camera)

#### 舵机由用户资料锁定，协议仍是原厂交付项

附件已重开并与项目留档SHA-256逐字节比对相同。它包含PDF/STEP/图片而没有协议与控制表；PDF和STEP型号文字不同。这里采用HD-1910-C001，不用FE-URT1兼容列表代替该舵机协议证明。

**具体例子:** 核对位置：FE-URT-1条目

**证据说明:** [E_debug](#evidence-E_debug) [E_runtime](#evidence-E_runtime)


### 下一版模型明确改哪些地方

> **本节回答:** R3选型没有自动成为RA3装配或打印放行。RA2模型本轮保持原样。

#### 电池座与躯干

用58×32×20mm动力电池代替NP-F滑轨电池；重画圆角托盘、绑带槽、线头缓冲和插拔区域。软包不能由螺钉顶压，按到货尺寸留制造余量。

**具体例子:** 核对位置：Product Specs：Capacity、Voltage、C rate、Dimensions、Balance Plug、Discharge Plug

**证据说明:** [E_battery](#evidence-E_battery)

#### 头部与散热叠层

将32mm相机、5519A、真实排针及铜柱同时入模，重画相机托和面罩；如果叠高不足，改壳而不是省略散热体。

**具体例子:** 核对位置：印刷页5 Physical specifications；页4 FPC

**证据说明:** [E_camera](#evidence-E_camera) [E_heat](#evidence-E_heat) [E_header](#evidence-E_header)

#### 传感器与声学支架

新增躯干IMU卡座、ToF通光孔、声学密封与声孔、两套NFC板/天线固定。NFC不要紧贴散热片；保留原配馈线。

**具体例子:** 核对位置：Board Outline / I2C / Power

**证据说明:** [E_imu](#evidence-E_imu) [E_tof](#evidence-E_tof) [E_speaker](#evidence-E_speaker) [E_mic](#evidence-E_mic) [E_nfc_wiring](#evidence-E_nfc_wiring)

#### 电源板和急停出口

用6.1mm贴片保险丝代替虚构小汽车保险丝座；三颗电容按11.5mm长度；升降压按22.9mm方板；原12.6mm急停开口改成控制线出口或恢复壳体。

**具体例子:** 核对位置：p1–3 电气特性/时间电流曲线/外形

**证据说明:** [E_fuse](#evidence-E_fuse) [E_cap](#evidence-E_cap) [E_buck](#evidence-E_buck) [E_estop](#evidence-E_estop)

#### 资料通过与实装通过分开

本次已核对来源和接口逻辑；还未做新选型的切片、全角度碰撞、载荷/温升与实物装配。材料、PCB与新模型通过对应测试后再整套打印。

**具体例子:** 核对位置：本地同源 duck-control/src/imu.rs、bus.rs、deploy/audio/*.dts

**证据说明:** [E_runtime](#evidence-E_runtime) [E_rl](#evidence-E_rl)


## 3. 精选资源

### 资源配置策略

比较了电池、音频与相机路线；以厂家参数和本地软件约束收敛主选，备选单列。

- **已审查候选资料:** 40
- **已选入资料:** 32
- **媒介:** text
- **内容用途:** reference

> 只收厂家规格、应用说明和源代码；不强制加入课程或视频。

### 选择适合你的路线

<!-- atlas-track:1 -->
#### 先采购与试配

- **适合:** 先完成首批样件与尺寸复核
- **节奏:** 每次30–60分钟，按阶段输入推进

**指定资源**

- [Gens ace 850mAh 7.4V 2S1P 60C EC2](https://gensace.de/products/gens-ace-850mah-7-4v-2s1p-60c-lipo-battery-pack-with-ec2-plug) — **使用位置:** Product Specs：Capacity、Voltage、C rate、Dimensions、Balance Plug、Discharge Plug; **推荐理由:** GEA8502S60E2；7.4V/850mAh/60C；约58×32×20mm、55g；EC2和JST-XHR-3P。 · **必做**
- [Radxa Camera 8M 219 Product Brief Rev 1.0](https://dl.radxa.com/accessories/camera-8m-219/radxa_camera_8m_219_product_brief_Revision_1.0.pdf) — **使用位置:** 印刷页5 Physical specifications；页4 FPC; **推荐理由:** 板32±0.2mm见方，孔距28±0.1mm，孔径2±0.1mm；镜头前凸15.98±0.2mm，PCB1.6mm；背面连接器另计。 · **必做**
- [Radxa Heatsink 5519A](https://radxa.com/products/accessories/heatsink-5519a/) — **使用位置:** 适配机型; **推荐理由:** 5519A为ZERO 3W/3E配套散热器。 · **必做**
- [LSM6DSV16X Hardware Overview](https://docs.sparkfun.com/SparkFun_6DoF_LSM6DSV16X/hardware_overview/) — **使用位置:** Board Outline / I2C / Power; **推荐理由:** Micro版SEN-21336为0.3×0.75英寸，即7.62×19.05mm；I2C默认0x6B；3.3V使用。 · **必做**
- [VL53L8CX Carrier #3419](https://www.pololu.com/product/3419) — **使用位置:** Features / Connections; **推荐理由:** 约13×23×3mm；3.2–5.5V；峰值150mA；I/O跟随VIN；SPI/I2C脚拉低选择I2C。 · **必做**
- [XA1E-BV302-R](https://www.idec.com/en-us/switches-indicator-lights/switches-pushbuttons/emergency-stop-switches/xa-16mm-estop/xa1e-bv302-r) — **使用位置:** Key Features / Mechanical Specifications; **推荐理由:** 16mm安装系列、29mm红蘑菇头、2NC、焊接端子。 · **必做**

<!-- /atlas-track -->

<!-- atlas-track:2 -->
#### 电路与软件实施

- **适合:** PCB/固件与整机集成人员
- **节奏:** 按原理图、布线、测试分段查阅

**指定资源**

- [LM74502DDFR](https://www.ti.com/lit/ds/symlink/lm74502.pdf) — **使用位置:** p1 / Pin functions / Typical application; **推荐理由:** 3.2–65V控制器，外接共源背靠背NFET；EN/UVLO拉低关断；导通时不提供反向电流阻断。 · **必做**
- [LM74502 bidirectional current application](https://e2e.ti.com/support/power-management-group/power-management/f/power-management-forum/1503649/lm74502-lm74502-as-high-side-driver-in-back-to-back-connected-common-source-mosfet) — **使用位置:** TI工程师答复; **推荐理由:** 共源背靠背NFET在控制器有效且栅极导通时允许双向电流。 · **必做**
- [451/453 Series Nano2 Fuse](https://www.littelfuse.com/assetdocs/fuse-451-and-453-datasheet?assetguid=533cd5cc-956c-4243-867f-6ab5a62f6ba1) — **使用位置:** p1–3 电气特性/时间电流曲线/外形; **推荐理由:** 451系列贴片保险丝，约6.10×2.69×2.69mm；规格覆盖3A、5A和15A。 · **必做**
- [TLV320AIC3104](https://www.ti.com/lit/ds/symlink/tlv320aic3104.pdf) — **使用位置:** Pin functions / Power / Digital interface; **推荐理由:** 保留AIC3104的I2S/I2C音频路线；IO/模拟3.3V、内核1.8V；具体供电与时序按数据表。 · **必做**
- [ZERO 3 Hardware Interface](https://docs.radxa.com/en/zero/zero3/hardware-design/hardware-interface) — **使用位置:** 40 PIN GPIO / Debug Serial / MIPI CSI; **推荐理由:** GPIO为3.3V；UART2占8/10；I2C4占27/28；UART4占16/18；UART5占32/33。 · **必做**
- [Microduck software repository](https://github.com/pollen-robotics/microduck) — **使用位置:** 本地同源 duck-control/src/imu.rs、bus.rs、deploy/audio/*.dts; **推荐理由:** 本地运行时要求躯干IMU；旧实现从Dynamixel ID200读取12字节；音频使用aic3104卡名。 · **必做**
- [Microduck RL repository](https://github.com/pollen-robotics/microduck_rl) — **使用位置:** 本地 robot_allcollisions.xml 的 sensor/site 与 microduck_constants.py; **推荐理由:** 本地训练传感器引用trunk_base的imu站点，而非head_imu；执行器仍是xl330/m6。 · **必做**

<!-- /atlas-track -->

### 按用途浏览

<!-- atlas-collection:1 -->
#### 硬件主选与规格

采购和建模查阅

- [Gens ace 850mAh 7.4V 2S1P 60C EC2](https://gensace.de/products/gens-ace-850mah-7-4v-2s1p-60c-lipo-battery-pack-with-ec2-plug)
- [Radxa ZERO 3W](https://radxa.com/products/zeros/zero3w/)
- [ZERO 3 Hardware Design Downloads](https://docs.radxa.com/en/zero/zero3/download)
- [ZERO 3 Hardware Interface](https://docs.radxa.com/en/zero/zero3/hardware-design/hardware-interface)
- [Radxa Heatsink 5519A](https://radxa.com/products/accessories/heatsink-5519a/)
- [Radxa Camera 8M 219 Product Brief Rev 1.0](https://dl.radxa.com/accessories/camera-8m-219/radxa_camera_8m_219_product_brief_Revision_1.0.pdf)
- [Radxa Camera 8M 219](https://docs.radxa.com/en/accessories/camera/camera-8m-219)
- [LSM6DSV16X Hardware Overview](https://docs.sparkfun.com/SparkFun_6DoF_LSM6DSV16X/hardware_overview/)
- [SparkFun LSM6DSV16X Hookup Guide](https://docs.sparkfun.com/SparkFun_6DoF_LSM6DSV16X/)
- [VL53L8CX Carrier #3419](https://www.pololu.com/product/3419)
- [AS02008MR-HT-WP](https://puiaudio.com/product/speakers-and-receivers/as02008mr-ht-wp)
- [CMC-4015-25T](https://www.sameskydevices.com/product/audio/microphones/electret-condenser-microphones/cmc-4015-25t)
- [TLV320AIC3104](https://www.ti.com/lit/ds/symlink/tlv320aic3104.pdf)
- [TPA2010D1](https://www.ti.com/lit/ds/symlink/tpa2010d1.pdf)
- [S13V30F5 #4082](https://www.pololu.com/product/4082)
- [LM74502DDFR](https://www.ti.com/lit/ds/symlink/lm74502.pdf)
- [CSD18540Q5B](https://www.ti.com/lit/gpn/CSD18540Q5B)
- [TPS62162DSGR](https://www.ti.com/product/TPS62162/part-details/TPS62162DSGR)
- [451/453 Series Nano2 Fuse](https://www.littelfuse.com/assetdocs/fuse-451-and-453-datasheet?assetguid=533cd5cc-956c-4243-867f-6ab5a62f6ba1)
- [EEUFR1C471](https://industrial.panasonic.com/kr/products/pt/aluminum-cap-lead/models?model_number=EEUFR1C471&order=model&sort=asc)
- [XA1E-BV302-R](https://www.idec.com/en-us/switches-indicator-lights/switches-pushbuttons/emergency-stop-switches/xa-16mm-estop/xa1e-bv302-r)
- [Grove NFC PN532 113020006](https://www.seeedstudio.com/Grove-NFC.html)
- [Grove NFC Wiki](https://wiki.seeedstudio.com/Grove_NFC/)
- [B6neo Series](https://www.skyrc.com/b6neo-series)
- [FE-URT-1 Programmer](https://www.feetechrc.com/serial-port-series-steering-gear_50681.html)
- [SSW-120-02-G-D](https://www.samtec.com/products/ssw-120-02-g-d)

<!-- /atlas-collection -->

<!-- atlas-collection:2 -->
#### 应用支持与接口

解决双向电流、天线及驱动问题

- [LM74502 bidirectional current application](https://e2e.ti.com/support/power-management-group/power-management/f/power-management-forum/1503649/lm74502-lm74502-as-high-side-driver-in-back-to-back-connected-common-source-mosfet)
- [NFC Antenna Dimensions](https://forum.seeedstudio.com/t/nfc-antenna-dimensions/6776)
- [Microduck software repository](https://github.com/pollen-robotics/microduck)
- [Microduck RL repository](https://github.com/pollen-robotics/microduck_rl)

<!-- /atlas-collection -->

<!-- atlas-collection:3 -->
#### 本轮未采用的备选

仅在对应取舍改变时使用

- [IMX219-160 Camera](https://www.waveshare.com/product/risc-v/cameras/imx219-160-camera.htm)
- [USB TO AUDIO](https://www.waveshare.com/product/usb-to-audio.htm)

<!-- /atlas-collection -->

### 资源详情

#### [Gens ace 850mAh 7.4V 2S1P 60C EC2](https://gensace.de/products/gens-ace-850mah-7-4v-2s1p-60c-lipo-battery-pack-with-ec2-plug)

- **作者或机构:** Gens ace
- **来源渠道:** 厂家规格与手册
- **类型:** 技术参考
- **用途:** 核对所选型号与接口
- **级别:** 工程实施
- **形式:** 网页、图纸或源代码
- **所需时间:** 按所列章节查阅，约5–15分钟
- **适合:** 该部件采购、布板和安装复核
- **获取方式:** 公开资料；采购价格、库存与地区供货需实际询价
- **优先级:** core
- **媒介:** text
- **内容用途:** reference
- **语言:** 英文为主
- **版本或更新情况:** 核对日期2026-09-05；版本信息见具体资料
- **验证日期:** 2026-09-05

**推荐理由:** GEA8502S60E2；7.4V/850mAh/60C；约58×32×20mm、55g；EC2和JST-XHR-3P。

**重点:** Product Specs：Capacity、Voltage、C rate、Dimensions、Balance Plug、Discharge Plug

**局限:** 网页库存标记混杂，尺寸为约值；C数是厂家标称而非本机实测。

**核验说明:** 核对了型号、对应规格或本地同源代码；网页库存标记混杂，尺寸为约值；C数是厂家标称而非本机实测。

#### [Radxa ZERO 3W](https://radxa.com/products/zeros/zero3w/)

- **作者或机构:** Radxa
- **来源渠道:** 厂家规格与手册
- **类型:** 技术参考
- **用途:** 核对所选型号与接口
- **级别:** 工程实施
- **形式:** 网页、图纸或源代码
- **所需时间:** 按所列章节查阅，约5–15分钟
- **适合:** 该部件采购、布板和安装复核
- **获取方式:** 公开资料；采购价格、库存与地区供货需实际询价
- **优先级:** core
- **媒介:** text
- **内容用途:** reference
- **语言:** 英文为主
- **版本或更新情况:** 核对日期2026-09-05；版本信息见具体资料
- **验证日期:** 2026-09-05

**推荐理由:** RK3566；可选eMMC与40针排针；22针0.5mm CSI；官方列出配套散热器和相机。

**重点:** 接口与配件

**局限:** 具体内存/eMMC和PCB版本以订货回执与丝印为准。

**核验说明:** 核对了型号、对应规格或本地同源代码；具体内存/eMMC和PCB版本以订货回执与丝印为准。

#### [ZERO 3 Hardware Design Downloads](https://docs.radxa.com/en/zero/zero3/download)

- **作者或机构:** Radxa
- **来源渠道:** 厂家规格与手册
- **类型:** 技术参考
- **用途:** 核对所选型号与接口
- **级别:** 工程实施
- **形式:** 网页、图纸或源代码
- **所需时间:** 按所列章节查阅，约5–15分钟
- **适合:** 该部件采购、布板和安装复核
- **获取方式:** 公开资料；采购价格、库存与地区供货需实际询价
- **优先级:** recommended
- **媒介:** text
- **内容用途:** reference
- **语言:** 英文为主
- **版本或更新情况:** 核对日期2026-09-05；版本信息见具体资料
- **验证日期:** 2026-09-05

**推荐理由:** V1.11与V1.12(AIC8800)分别提供图纸；旧3D文件不自动证明新板元件高度一致。

**重点:** Hardware Design

**局限:** 本地旧STEP有效性问题未在本轮消除。

**核验说明:** 核对了型号、对应规格或本地同源代码；本地旧STEP有效性问题未在本轮消除。

#### [ZERO 3 Hardware Interface](https://docs.radxa.com/en/zero/zero3/hardware-design/hardware-interface)

- **作者或机构:** Radxa
- **来源渠道:** 厂家规格与手册
- **类型:** 技术参考
- **用途:** 核对所选型号与接口
- **级别:** 工程实施
- **形式:** 网页、图纸或源代码
- **所需时间:** 按所列章节查阅，约5–15分钟
- **适合:** 该部件采购、布板和安装复核
- **获取方式:** 公开资料；采购价格、库存与地区供货需实际询价
- **优先级:** recommended
- **媒介:** text
- **内容用途:** reference
- **语言:** 英文为主
- **版本或更新情况:** 核对日期2026-09-05；版本信息见具体资料
- **验证日期:** 2026-09-05

**推荐理由:** GPIO为3.3V；UART2占8/10；I2C4占27/28；UART4占16/18；UART5占32/33。

**重点:** 40 PIN GPIO / Debug Serial / MIPI CSI

**局限:** UART2默认兼任控制台；需处理启动日志与引导输入。

**核验说明:** 核对了型号、对应规格或本地同源代码；UART2默认兼任控制台；需处理启动日志与引导输入。

#### [Radxa Heatsink 5519A](https://radxa.com/products/accessories/heatsink-5519a/)

- **作者或机构:** Radxa
- **来源渠道:** 厂家规格与手册
- **类型:** 技术参考
- **用途:** 核对所选型号与接口
- **级别:** 工程实施
- **形式:** 网页、图纸或源代码
- **所需时间:** 按所列章节查阅，约5–15分钟
- **适合:** 该部件采购、布板和安装复核
- **获取方式:** 公开资料；采购价格、库存与地区供货需实际询价
- **优先级:** recommended
- **媒介:** text
- **内容用途:** reference
- **语言:** 英文为主
- **版本或更新情况:** 核对日期2026-09-05；版本信息见具体资料
- **验证日期:** 2026-09-05

**推荐理由:** 5519A为ZERO 3W/3E配套散热器。

**重点:** 适配机型

**局限:** 官网正文未列完整高度，本轮不虚构其包络；到货或有效CAD后复核叠高。

**核验说明:** 核对了型号、对应规格或本地同源代码；官网正文未列完整高度，本轮不虚构其包络；到货或有效CAD后复核叠高。

#### [Radxa Camera 8M 219 Product Brief Rev 1.0](https://dl.radxa.com/accessories/camera-8m-219/radxa_camera_8m_219_product_brief_Revision_1.0.pdf)

- **作者或机构:** Radxa
- **来源渠道:** 厂家规格与手册
- **类型:** 技术参考
- **用途:** 核对所选型号与接口
- **级别:** 工程实施
- **形式:** 网页、图纸或源代码
- **所需时间:** 按所列章节查阅，约5–15分钟
- **适合:** 该部件采购、布板和安装复核
- **获取方式:** 公开资料；采购价格、库存与地区供货需实际询价
- **优先级:** core
- **媒介:** text
- **内容用途:** reference
- **语言:** 英文为主
- **版本或更新情况:** 核对日期2026-09-05；版本信息见具体资料
- **验证日期:** 2026-09-05

**推荐理由:** 板32±0.2mm见方，孔距28±0.1mm，孔径2±0.1mm；镜头前凸15.98±0.2mm，PCB1.6mm；背面连接器另计。

**重点:** 印刷页5 Physical specifications；页4 FPC

**局限:** 前凸尺寸不是整个模组总厚；旧25×24占位和M12镜头座需要改。

**核验说明:** 核对了型号、对应规格或本地同源代码；前凸尺寸不是整个模组总厚；旧25×24占位和M12镜头座需要改。

#### [Radxa Camera 8M 219](https://docs.radxa.com/en/accessories/camera/camera-8m-219)

- **作者或机构:** Radxa
- **来源渠道:** 厂家规格与手册
- **类型:** 技术参考
- **用途:** 核对所选型号与接口
- **级别:** 工程实施
- **形式:** 网页、图纸或源代码
- **所需时间:** 按所列章节查阅，约5–15分钟
- **适合:** 该部件采购、布板和安装复核
- **获取方式:** 公开资料；采购价格、库存与地区供货需实际询价
- **优先级:** core
- **媒介:** text
- **内容用途:** reference
- **语言:** 英文为主
- **版本或更新情况:** 核对日期2026-09-05；版本信息见具体资料
- **验证日期:** 2026-09-05

**推荐理由:** 原配150mm同面22P 0.5mm转15P 1.0mm，官方明确支持ZERO 3W/3E。

**重点:** Default FPC / FPC Cable

**局限:** 资料同时出现不同视角口径，按D74/H62/V49作初始标定参考，最终重标定。

**核验说明:** 核对了型号、对应规格或本地同源代码；资料同时出现不同视角口径，按D74/H62/V49作初始标定参考，最终重标定。

#### [LSM6DSV16X Hardware Overview](https://docs.sparkfun.com/SparkFun_6DoF_LSM6DSV16X/hardware_overview/)

- **作者或机构:** SparkFun
- **来源渠道:** 厂家规格与手册
- **类型:** 技术参考
- **用途:** 核对所选型号与接口
- **级别:** 工程实施
- **形式:** 网页、图纸或源代码
- **所需时间:** 按所列章节查阅，约5–15分钟
- **适合:** 该部件采购、布板和安装复核
- **获取方式:** 公开资料；采购价格、库存与地区供货需实际询价
- **优先级:** core
- **媒介:** text
- **内容用途:** reference
- **语言:** 英文为主
- **版本或更新情况:** 核对日期2026-09-05；版本信息见具体资料
- **验证日期:** 2026-09-05

**推荐理由:** Micro版SEN-21336为0.3×0.75英寸，即7.62×19.05mm；I2C默认0x6B；3.3V使用。

**重点:** Board Outline / I2C / Power

**局限:** 模组不是Dynamixel ID200设备；需要新的I2C读取后端。

**核验说明:** 核对了型号、对应规格或本地同源代码；模组不是Dynamixel ID200设备；需要新的I2C读取后端。

#### [SparkFun LSM6DSV16X Hookup Guide](https://docs.sparkfun.com/SparkFun_6DoF_LSM6DSV16X/)

- **作者或机构:** SparkFun
- **来源渠道:** 厂家规格与手册
- **类型:** 技术参考
- **用途:** 核对所选型号与接口
- **级别:** 工程实施
- **形式:** 网页、图纸或源代码
- **所需时间:** 按所列章节查阅，约5–15分钟
- **适合:** 该部件采购、布板和安装复核
- **获取方式:** 公开资料；采购价格、库存与地区供货需实际询价
- **优先级:** recommended
- **媒介:** text
- **内容用途:** reference
- **语言:** 英文为主
- **版本或更新情况:** 核对日期2026-09-05；版本信息见具体资料
- **验证日期:** 2026-09-05

**推荐理由:** SEN-21336为Micro版，SEN-21325为较大的标准版；两者不要混买。

**重点:** Required Materials

**局限:** 本轮选Micro版；保留原厂Qwiic线及原理图。

**核验说明:** 核对了型号、对应规格或本地同源代码；本轮选Micro版；保留原厂Qwiic线及原理图。

#### [VL53L8CX Carrier #3419](https://www.pololu.com/product/3419)

- **作者或机构:** Pololu
- **来源渠道:** 厂家规格与手册
- **类型:** 技术参考
- **用途:** 核对所选型号与接口
- **级别:** 工程实施
- **形式:** 网页、图纸或源代码
- **所需时间:** 按所列章节查阅，约5–15分钟
- **适合:** 该部件采购、布板和安装复核
- **获取方式:** 公开资料；采购价格、库存与地区供货需实际询价
- **优先级:** core
- **媒介:** text
- **内容用途:** reference
- **语言:** 英文为主
- **版本或更新情况:** 核对日期2026-09-05；版本信息见具体资料
- **验证日期:** 2026-09-05

**推荐理由:** 约13×23×3mm；3.2–5.5V；峰值150mA；I/O跟随VIN；SPI/I2C脚拉低选择I2C。

**重点:** Features / Connections

**局限:** 本方案VIN固定3.3V；短线连接，勿误用5V逻辑接Radxa。

**核验说明:** 核对了型号、对应规格或本地同源代码；本方案VIN固定3.3V；短线连接，勿误用5V逻辑接Radxa。

#### [AS02008MR-HT-WP](https://puiaudio.com/product/speakers-and-receivers/as02008mr-ht-wp)

- **作者或机构:** PUI Audio
- **来源渠道:** 厂家规格与手册
- **类型:** 技术参考
- **用途:** 核对所选型号与接口
- **级别:** 工程实施
- **形式:** 网页、图纸或源代码
- **所需时间:** 按所列章节查阅，约5–15分钟
- **适合:** 该部件采购、布板和安装复核
- **获取方式:** 公开资料；采购价格、库存与地区供货需实际询价
- **优先级:** recommended
- **媒介:** text
- **内容用途:** reference
- **语言:** 英文为主
- **版本或更新情况:** 核对日期2026-09-05；版本信息见具体资料
- **验证日期:** 2026-09-05

**推荐理由:** 20mm直径、3.9mm高、8Ω、额定1.2W、2.5g。

**重点:** Dimensions & Specifications

**局限:** 与旧20×5占位不同；安装、防漏气及声孔仍要实际验证。

**核验说明:** 核对了型号、对应规格或本地同源代码；与旧20×5占位不同；安装、防漏气及声孔仍要实际验证。

#### [CMC-4015-25T](https://www.sameskydevices.com/product/audio/microphones/electret-condenser-microphones/cmc-4015-25t)

- **作者或机构:** Same Sky
- **来源渠道:** 厂家规格与手册
- **类型:** 技术参考
- **用途:** 核对所选型号与接口
- **级别:** 工程实施
- **形式:** 网页、图纸或源代码
- **所需时间:** 按所列章节查阅，约5–15分钟
- **适合:** 该部件采购、布板和安装复核
- **获取方式:** 公开资料；采购价格、库存与地区供货需实际询价
- **优先级:** recommended
- **媒介:** text
- **内容用途:** reference
- **语言:** 英文为主
- **版本或更新情况:** 核对日期2026-09-05；版本信息见具体资料
- **验证日期:** 2026-09-05

**推荐理由:** 4×4×1.5mm顶入声模拟驻极体，标称3V、负载2.2kΩ。

**重点:** Specifications；datasheet p1

**局限:** 初次搜索的厂家正文与数据表已核对；后续直接抓取出现403。

**核验说明:** 核对了型号、对应规格或本地同源代码；初次搜索的厂家正文与数据表已核对；后续直接抓取出现403。

#### [TLV320AIC3104](https://www.ti.com/lit/ds/symlink/tlv320aic3104.pdf)

- **作者或机构:** Texas Instruments
- **来源渠道:** 厂家规格与手册
- **类型:** 技术参考
- **用途:** 核对所选型号与接口
- **级别:** 工程实施
- **形式:** 网页、图纸或源代码
- **所需时间:** 按所列章节查阅，约5–15分钟
- **适合:** 该部件采购、布板和安装复核
- **获取方式:** 公开资料；采购价格、库存与地区供货需实际询价
- **优先级:** recommended
- **媒介:** text
- **内容用途:** reference
- **语言:** 英文为主
- **版本或更新情况:** 核对日期2026-09-05；版本信息见具体资料
- **验证日期:** 2026-09-05

**推荐理由:** 保留AIC3104的I2S/I2C音频路线；IO/模拟3.3V、内核1.8V；具体供电与时序按数据表。

**重点:** Pin functions / Power / Digital interface

**局限:** 需要PCB与SMT，不是可直接购买的Microduck成品HAT。

**核验说明:** 核对了型号、对应规格或本地同源代码；需要PCB与SMT，不是可直接购买的Microduck成品HAT。

#### [TPA2010D1](https://www.ti.com/lit/ds/symlink/tpa2010d1.pdf)

- **作者或机构:** Texas Instruments
- **来源渠道:** 厂家规格与手册
- **类型:** 技术参考
- **用途:** 核对所选型号与接口
- **级别:** 工程实施
- **形式:** 网页、图纸或源代码
- **所需时间:** 按所列章节查阅，约5–15分钟
- **适合:** 该部件采购、布板和安装复核
- **获取方式:** 公开资料；采购价格、库存与地区供货需实际询价
- **优先级:** recommended
- **媒介:** text
- **内容用途:** reference
- **语言:** 英文为主
- **版本或更新情况:** 核对日期2026-09-05；版本信息见具体资料
- **验证日期:** 2026-09-05

**推荐理由:** TPA2010D1作为5V单声道功放，接AIC3104差分线路输出。

**重点:** Application / Gain setting

**局限:** 限制输出到所选扬声器额定功率以内，回路与麦克风分开。

**核验说明:** 核对了型号、对应规格或本地同源代码；限制输出到所选扬声器额定功率以内，回路与麦克风分开。

#### [S13V30F5 #4082](https://www.pololu.com/product/4082)

- **作者或机构:** Pololu
- **来源渠道:** 厂家规格与手册
- **类型:** 技术参考
- **用途:** 核对所选型号与接口
- **级别:** 工程实施
- **形式:** 网页、图纸或源代码
- **所需时间:** 按所列章节查阅，约5–15分钟
- **适合:** 该部件采购、布板和安装复核
- **获取方式:** 公开资料；采购价格、库存与地区供货需实际询价
- **优先级:** recommended
- **媒介:** text
- **内容用途:** reference
- **语言:** 英文为主
- **版本或更新情况:** 核对日期2026-09-05；版本信息见具体资料
- **验证日期:** 2026-09-05

**推荐理由:** 5V升降压，2.8–22V输入；约22.9×22.9×9.7mm；典型约3A。

**重点:** Features / Output-current graph

**局限:** 实际连续电流受输入电压、散热影响；3A不是无条件保证。

**核验说明:** 核对了型号、对应规格或本地同源代码；实际连续电流受输入电压、散热影响；3A不是无条件保证。

#### [LM74502DDFR](https://www.ti.com/lit/ds/symlink/lm74502.pdf)

- **作者或机构:** Texas Instruments
- **来源渠道:** 厂家规格与手册
- **类型:** 技术参考
- **用途:** 核对所选型号与接口
- **级别:** 工程实施
- **形式:** 网页、图纸或源代码
- **所需时间:** 按所列章节查阅，约5–15分钟
- **适合:** 该部件采购、布板和安装复核
- **获取方式:** 公开资料；采购价格、库存与地区供货需实际询价
- **优先级:** core
- **媒介:** text
- **内容用途:** reference
- **语言:** 英文为主
- **版本或更新情况:** 核对日期2026-09-05；版本信息见具体资料
- **验证日期:** 2026-09-05

**推荐理由:** 3.2–65V控制器，外接共源背靠背NFET；EN/UVLO拉低关断；导通时不提供反向电流阻断。

**重点:** p1 / Pin functions / Typical application

**局限:** 本轮替换原LM74800思路，保留回馈通路；断电后回馈尖峰仍需设计验证。

**核验说明:** 核对了型号、对应规格或本地同源代码；本轮替换原LM74800思路，保留回馈通路；断电后回馈尖峰仍需设计验证。

#### [LM74502 bidirectional current application](https://e2e.ti.com/support/power-management-group/power-management/f/power-management-forum/1503649/lm74502-lm74502-as-high-side-driver-in-back-to-back-connected-common-source-mosfet)

- **作者或机构:** Texas Instruments
- **来源渠道:** 厂家应用支持
- **类型:** 技术参考
- **用途:** 核对所选型号与接口
- **级别:** 工程实施
- **形式:** 网页、图纸或源代码
- **所需时间:** 按所列章节查阅，约5–15分钟
- **适合:** 该部件采购、布板和安装复核
- **获取方式:** 公开资料；采购价格、库存与地区供货需实际询价
- **优先级:** recommended
- **媒介:** text
- **内容用途:** reference
- **语言:** 英文为主
- **版本或更新情况:** 核对日期2026-09-05；版本信息见具体资料
- **验证日期:** 2026-09-05

**推荐理由:** 共源背靠背NFET在控制器有效且栅极导通时允许双向电流。

**重点:** TI工程师答复

**局限:** 属于该电路配置的应用答复，不替代整机回馈测试。

**核验说明:** 核对了型号、对应规格或本地同源代码；属于该电路配置的应用答复，不替代整机回馈测试。

#### [CSD18540Q5B](https://www.ti.com/lit/gpn/CSD18540Q5B)

- **作者或机构:** Texas Instruments
- **来源渠道:** 厂家规格与手册
- **类型:** 技术参考
- **用途:** 核对所选型号与接口
- **级别:** 工程实施
- **形式:** 网页、图纸或源代码
- **所需时间:** 按所列章节查阅，约5–15分钟
- **适合:** 该部件采购、布板和安装复核
- **获取方式:** 公开资料；采购价格、库存与地区供货需实际询价
- **优先级:** recommended
- **媒介:** text
- **内容用途:** reference
- **语言:** 英文为主
- **版本或更新情况:** 核对日期2026-09-05；版本信息见具体资料
- **验证日期:** 2026-09-05

**推荐理由:** 60V NFET，标称5×6mm封装；本方案两颗共源背靠背。

**重点:** Product summary / Package

**局限:** 导通损耗按实际栅压与温度核算，不只引用室温典型电阻。

**核验说明:** 核对了型号、对应规格或本地同源代码；导通损耗按实际栅压与温度核算，不只引用室温典型电阻。

#### [TPS62162DSGR](https://www.ti.com/product/TPS62162/part-details/TPS62162DSGR)

- **作者或机构:** Texas Instruments
- **来源渠道:** 厂家规格与手册
- **类型:** 技术参考
- **用途:** 核对所选型号与接口
- **级别:** 工程实施
- **形式:** 网页、图纸或源代码
- **所需时间:** 按所列章节查阅，约5–15分钟
- **适合:** 该部件采购、布板和安装复核
- **获取方式:** 公开资料；采购价格、库存与地区供货需实际询价
- **优先级:** recommended
- **媒介:** text
- **内容用途:** reference
- **语言:** 英文为主
- **版本或更新情况:** 核对日期2026-09-05；版本信息见具体资料
- **验证日期:** 2026-09-05

**推荐理由:** 3–17V、1A降压器，固定输出版本用于数字3.3V；选DSG封装。

**重点:** Features / Part details

**局限:** 官网直售显示缺货；PCB投产前由SMT供应商确认授权渠道供货。

**核验说明:** 核对了型号、对应规格或本地同源代码；官网直售显示缺货；PCB投产前由SMT供应商确认授权渠道供货。

#### [451/453 Series Nano2 Fuse](https://www.littelfuse.com/assetdocs/fuse-451-and-453-datasheet?assetguid=533cd5cc-956c-4243-867f-6ab5a62f6ba1)

- **作者或机构:** Littelfuse
- **来源渠道:** 厂家规格与手册
- **类型:** 技术参考
- **用途:** 核对所选型号与接口
- **级别:** 工程实施
- **形式:** 网页、图纸或源代码
- **所需时间:** 按所列章节查阅，约5–15分钟
- **适合:** 该部件采购、布板和安装复核
- **获取方式:** 公开资料；采购价格、库存与地区供货需实际询价
- **优先级:** recommended
- **媒介:** text
- **内容用途:** reference
- **语言:** 英文为主
- **版本或更新情况:** 核对日期2026-09-05；版本信息见具体资料
- **验证日期:** 2026-09-05

**推荐理由:** 451系列贴片保险丝，约6.10×2.69×2.69mm；规格覆盖3A、5A和15A。

**重点:** p1–3 电气特性/时间电流曲线/外形

**局限:** 本轮额定值为样机起点；按时间-电流曲线、I²t及线束温升复核，不承担精确电机限流。

**核验说明:** 核对了型号、对应规格或本地同源代码；本轮额定值为样机起点；按时间-电流曲线、I²t及线束温升复核，不承担精确电机限流。

#### [EEUFR1C471](https://industrial.panasonic.com/kr/products/pt/aluminum-cap-lead/models?model_number=EEUFR1C471&order=model&sort=asc)

- **作者或机构:** Panasonic
- **来源渠道:** 厂家规格与手册
- **类型:** 技术参考
- **用途:** 核对所选型号与接口
- **级别:** 工程实施
- **形式:** 网页、图纸或源代码
- **所需时间:** 按所列章节查阅，约5–15分钟
- **适合:** 该部件采购、布板和安装复核
- **获取方式:** 公开资料；采购价格、库存与地区供货需实际询价
- **优先级:** recommended
- **媒介:** text
- **内容用途:** reference
- **语言:** 英文为主
- **版本或更新情况:** 核对日期2026-09-05；版本信息见具体资料
- **验证日期:** 2026-09-05

**推荐理由:** FR系列，16V/470µF，直径8mm、长11.5mm。

**重点:** Model table

**局限:** 较旧10mm长度占位增加1.5mm；横置及引脚固定需要重画。

**核验说明:** 核对了型号、对应规格或本地同源代码；较旧10mm长度占位增加1.5mm；横置及引脚固定需要重画。

#### [XA1E-BV302-R](https://www.idec.com/en-us/switches-indicator-lights/switches-pushbuttons/emergency-stop-switches/xa-16mm-estop/xa1e-bv302-r)

- **作者或机构:** IDEC
- **来源渠道:** 厂家规格与手册
- **类型:** 技术参考
- **用途:** 核对所选型号与接口
- **级别:** 工程实施
- **形式:** 网页、图纸或源代码
- **所需时间:** 按所列章节查阅，约5–15分钟
- **适合:** 该部件采购、布板和安装复核
- **获取方式:** 公开资料；采购价格、库存与地区供货需实际询价
- **优先级:** core
- **媒介:** text
- **内容用途:** reference
- **语言:** 英文为主
- **版本或更新情况:** 核对日期2026-09-05；版本信息见具体资料
- **验证日期:** 2026-09-05

**推荐理由:** 16mm安装系列、29mm红蘑菇头、2NC、焊接端子。

**重点:** Key Features / Mechanical Specifications

**局限:** 首版放外置有线盒；开关器件合格不等于整机急停系统认证。

**核验说明:** 核对了型号、对应规格或本地同源代码；首版放外置有线盒；开关器件合格不等于整机急停系统认证。

#### [Grove NFC PN532 113020006](https://www.seeedstudio.com/Grove-NFC.html)

- **作者或机构:** Seeed Studio
- **来源渠道:** 厂家规格与手册
- **类型:** 技术参考
- **用途:** 核对所选型号与接口
- **级别:** 工程实施
- **形式:** 网页、图纸或源代码
- **所需时间:** 按所列章节查阅，约5–15分钟
- **适合:** 该部件采购、布板和安装复核
- **获取方式:** 公开资料；采购价格、库存与地区供货需实际询价
- **优先级:** supplementary
- **媒介:** text
- **内容用途:** reference
- **语言:** 英文为主
- **版本或更新情况:** 核对日期2026-09-05；版本信息见具体资料
- **验证日期:** 2026-09-05

**推荐理由:** 113020006是PN532读卡模块，页面显示有货；不是ST25DV64动态标签。

**重点:** SKU / Product summary

**局限:** 报价/库存会变化；装机需新增NFC程序。

**核验说明:** 核对了型号、对应规格或本地同源代码；报价/库存会变化；装机需新增NFC程序。

#### [Grove NFC Wiki](https://wiki.seeedstudio.com/Grove_NFC/)

- **作者或机构:** Seeed Studio
- **来源渠道:** 厂家规格与手册
- **类型:** 技术参考
- **用途:** 核对所选型号与接口
- **级别:** 工程实施
- **形式:** 网页、图纸或源代码
- **所需时间:** 按所列章节查阅，约5–15分钟
- **适合:** 该部件采购、布板和安装复核
- **获取方式:** 公开资料；采购价格、库存与地区供货需实际询价
- **优先级:** supplementary
- **媒介:** text
- **内容用途:** reference
- **语言:** 英文为主
- **版本或更新情况:** 核对日期2026-09-05；版本信息见具体资料
- **验证日期:** 2026-09-05

**推荐理由:** 控制板25.43×20.35mm、3.3V、UART默认，可连接独立PCB天线。

**重点:** Specifications / Hardware overview

**局限:** 两个模块分别走UART4与UART5；保持原配天线和馈线，不自行裁剪。

**核验说明:** 核对了型号、对应规格或本地同源代码；两个模块分别走UART4与UART5；保持原配天线和馈线，不自行裁剪。

#### [NFC Antenna Dimensions](https://forum.seeedstudio.com/t/nfc-antenna-dimensions/6776)

- **作者或机构:** Seeed Studio 技术支持
- **来源渠道:** 厂家应用支持
- **类型:** 技术参考
- **用途:** 核对所选型号与接口
- **级别:** 工程实施
- **形式:** 网页、图纸或源代码
- **所需时间:** 按所列章节查阅，约5–15分钟
- **适合:** 该部件采购、布板和安装复核
- **获取方式:** 公开资料；采购价格、库存与地区供货需实际询价
- **优先级:** supplementary
- **媒介:** text
- **内容用途:** reference
- **语言:** 英文为主
- **版本或更新情况:** 核对日期2026-09-05；版本信息见具体资料
- **验证日期:** 2026-09-05

**推荐理由:** 配套天线PCB为28×30.5mm；较大尺寸是包装尺寸。

**重点:** 2019-04-26 技术支持回复

**局限:** 以所发模块的配套天线为准，金属与壳体会改变读距。

**核验说明:** 核对了型号、对应规格或本地同源代码；以所发模块的配套天线为准，金属与壳体会改变读距。

#### [B6neo Series](https://www.skyrc.com/b6neo-series)

- **作者或机构:** SkyRC
- **来源渠道:** 厂家规格与手册
- **类型:** 技术参考
- **用途:** 核对所选型号与接口
- **级别:** 工程实施
- **形式:** 网页、图纸或源代码
- **所需时间:** 按所列章节查阅，约5–15分钟
- **适合:** 该部件采购、布板和安装复核
- **获取方式:** 公开资料；采购价格、库存与地区供货需实际询价
- **优先级:** recommended
- **媒介:** text
- **内容用途:** reference
- **语言:** 英文为主
- **版本或更新情况:** 核对日期2026-09-05；版本信息见具体资料
- **验证日期:** 2026-09-05

**推荐理由:** 选择B6neo SK-100198，支持DC/USB-PD输入和平衡充电。

**重点:** 型号表 / Specification

**局限:** 配原厂说明书按标准LiPo 2S设置，非LiHV模式；不在机器人内充电。

**核验说明:** 核对了型号、对应规格或本地同源代码；配原厂说明书按标准LiPo 2S设置，非LiHV模式；不在机器人内充电。

#### [FE-URT-1 Programmer](https://www.feetechrc.com/serial-port-series-steering-gear_50681.html)

- **作者或机构:** FEETECH
- **来源渠道:** 厂家规格与手册
- **类型:** 技术参考
- **用途:** 核对所选型号与接口
- **级别:** 工程实施
- **形式:** 网页、图纸或源代码
- **所需时间:** 按所列章节查阅，约5–15分钟
- **适合:** 该部件采购、布板和安装复核
- **获取方式:** 公开资料；采购价格、库存与地区供货需实际询价
- **优先级:** recommended
- **媒介:** text
- **内容用途:** reference
- **语言:** 英文为主
- **版本或更新情况:** 核对日期2026-09-05；版本信息见具体资料
- **验证日期:** 2026-09-05

**推荐理由:** FE-URT1-C001：USB转TTL/485调试板，52×38.4×16mm，最高1Mbps。

**重点:** FE-URT-1条目

**局限:** 仅台架工具。HD1910的机械参数来自用户附件，不由这个产品页证明。

**核验说明:** 核对了型号、对应规格或本地同源代码；仅台架工具。HD1910的机械参数来自用户附件，不由这个产品页证明。

#### [SSW-120-02-G-D](https://www.samtec.com/products/ssw-120-02-g-d)

- **作者或机构:** Samtec
- **来源渠道:** 厂家规格与手册
- **类型:** 技术参考
- **用途:** 核对所选型号与接口
- **级别:** 工程实施
- **形式:** 网页、图纸或源代码
- **所需时间:** 按所列章节查阅，约5–15分钟
- **适合:** 该部件采购、布板和安装复核
- **获取方式:** 公开资料；采购价格、库存与地区供货需实际询价
- **优先级:** recommended
- **媒介:** text
- **内容用途:** reference
- **语言:** 英文为主
- **版本或更新情况:** 核对日期2026-09-05；版本信息见具体资料
- **验证日期:** 2026-09-05

**推荐理由:** 2.54mm间距，双排40针直插母座。

**重点:** 产品标题/Prints

**局限:** 精确啮合尺寸按配置图；12mm铜柱是设计起点，不是已验收叠高。

**核验说明:** 核对了型号、对应规格或本地同源代码；精确啮合尺寸按配置图；12mm铜柱是设计起点，不是已验收叠高。

#### [Microduck software repository](https://github.com/pollen-robotics/microduck)

- **作者或机构:** Pollen Robotics
- **来源渠道:** 项目源代码
- **类型:** 技术参考
- **用途:** 核对所选型号与接口
- **级别:** 工程实施
- **形式:** 网页、图纸或源代码
- **所需时间:** 按所列章节查阅，约5–15分钟
- **适合:** 该部件采购、布板和安装复核
- **获取方式:** 公开资料；采购价格、库存与地区供货需实际询价
- **优先级:** core
- **媒介:** text
- **内容用途:** reference
- **语言:** 英文为主
- **版本或更新情况:** 核对日期2026-09-05；版本信息见具体资料
- **验证日期:** 2026-09-05

**推荐理由:** 本地运行时要求躯干IMU；旧实现从Dynamixel ID200读取12字节；音频使用aic3104卡名。

**重点:** 本地同源 duck-control/src/imu.rs、bus.rs、deploy/audio/*.dts

**局限:** 采用独立I2C IMU要改RobotIo后端；不是仅插线即可运行。

**核验说明:** 核对了型号、对应规格或本地同源代码；采用独立I2C IMU要改RobotIo后端；不是仅插线即可运行。

#### [Microduck RL repository](https://github.com/pollen-robotics/microduck_rl)

- **作者或机构:** Pollen Robotics
- **来源渠道:** 项目源代码
- **类型:** 技术参考
- **用途:** 核对所选型号与接口
- **级别:** 工程实施
- **形式:** 网页、图纸或源代码
- **所需时间:** 按所列章节查阅，约5–15分钟
- **适合:** 该部件采购、布板和安装复核
- **获取方式:** 公开资料；采购价格、库存与地区供货需实际询价
- **优先级:** supplementary
- **媒介:** text
- **内容用途:** reference
- **语言:** 英文为主
- **版本或更新情况:** 核对日期2026-09-05；版本信息见具体资料
- **验证日期:** 2026-09-05

**推荐理由:** 本地训练传感器引用trunk_base的imu站点，而非head_imu；执行器仍是xl330/m6。

**重点:** 本地 robot_allcollisions.xml 的 sensor/site 与 microduck_constants.py

**局限:** 硬件选型不等于HD电机辨识、策略重训或行走验证。

**核验说明:** 核对了型号、对应规格或本地同源代码；硬件选型不等于HD电机辨识、策略重训或行走验证。

#### [IMX219-160 Camera](https://www.waveshare.com/product/risc-v/cameras/imx219-160-camera.htm)

- **作者或机构:** Waveshare
- **来源渠道:** 厂家规格与手册
- **类型:** 技术参考
- **用途:** 核对所选型号与接口
- **级别:** 工程实施
- **形式:** 网页、图纸或源代码
- **所需时间:** 按所列章节查阅，约5–15分钟
- **适合:** 该部件采购、布板和安装复核
- **获取方式:** 公开资料；采购价格、库存与地区供货需实际询价
- **优先级:** supplementary
- **媒介:** text
- **内容用途:** reference
- **语言:** 英文为主
- **版本或更新情况:** 核对日期2026-09-05；版本信息见具体资料
- **验证日期:** 2026-09-05

**推荐理由:** 非IR的160°版本为25×24mm板框；与32×32mm Radxa模组不同。

**重点:** Specifications / Version Options

**局限:** 本轮不选；若广角优先，需重验FPC、驱动与标定，而非直接沿用原占位。

**核验说明:** 核对了型号、对应规格或本地同源代码；本轮不选；若广角优先，需重验FPC、驱动与标定，而非直接沿用原占位。

#### [USB TO AUDIO](https://www.waveshare.com/product/usb-to-audio.htm)

- **作者或机构:** Waveshare
- **来源渠道:** 厂家规格与手册
- **类型:** 技术参考
- **用途:** 核对所选型号与接口
- **级别:** 工程实施
- **形式:** 网页、图纸或源代码
- **所需时间:** 按所列章节查阅，约5–15分钟
- **适合:** 该部件采购、布板和安装复核
- **获取方式:** 公开资料；采购价格、库存与地区供货需实际询价
- **优先级:** supplementary
- **媒介:** text
- **内容用途:** reference
- **语言:** 英文为主
- **版本或更新情况:** 核对日期2026-09-05；版本信息见具体资料
- **验证日期:** 2026-09-05

**推荐理由:** 现成USB音频模块是一条减少自制音频电路的路线。

**重点:** Product details

**局限:** 本轮不选；机械空间、USB走线和ALSA设备名需另改，不是AIC3104 HAT的直接替身。

**核验说明:** 核对了型号、对应规格或本地同源代码；本轮不选；机械空间、USB走线和ALSA设备名需另改，不是AIC3104 HAT的直接替身。

## 4. 详细学习或探索路线图

<!-- atlas-stage:1 -->
### 阶段 1: 首批采购与资料回执

- **持续时间:** 首轮工程时间盒，采购/打样等待另计
- **每周投入:** 90分钟计划工时
- **必做内容计划用时:** 90 分钟

**目标**

- 带型号与附件版本的首批订单清单

**前置要求**


**指定资源**

- [Gens ace 850mAh 7.4V 2S1P 60C EC2](https://gensace.de/products/gens-ace-850mah-7-4v-2s1p-60c-lipo-battery-pack-with-ec2-plug) — **使用位置:** Product Specs：Capacity、Voltage、C rate、Dimensions、Balance Plug、Discharge Plug; **推荐理由:** GEA8502S60E2；7.4V/850mAh/60C；约58×32×20mm、55g；EC2和JST-XHR-3P。 · **必做**
- [FE-URT-1 Programmer](https://www.feetechrc.com/serial-port-series-steering-gear_50681.html) — **使用位置:** FE-URT-1条目; **推荐理由:** FE-URT1-C001：USB转TTL/485调试板，52×38.4×16mm，最高1Mbps。 · **必做**
- [Radxa Camera 8M 219 Product Brief Rev 1.0](https://dl.radxa.com/accessories/camera-8m-219/radxa_camera_8m_219_product_brief_Revision_1.0.pdf) — **使用位置:** 印刷页5 Physical specifications；页4 FPC; **推荐理由:** 板32±0.2mm见方，孔距28±0.1mm，孔径2±0.1mm；镜头前凸15.98±0.2mm，PCB1.6mm；背面连接器另计。 · **必做**

**学习单元**

- **S11 · 首批采购与资料回执：1** (45 分钟) · **必做**
  - **行动:** 核对25条定选清单与首批数量，取得商家型号/图纸回执。
  - **预期产出:** 带型号与附件版本的首批订单清单子记录1
  - **资源:** [Gens ace 850mAh 7.4V 2S1P 60C EC2](https://gensace.de/products/gens-ace-850mah-7-4v-2s1p-60c-lipo-battery-pack-with-ec2-plug) — Product Specs：Capacity、Voltage、C rate、Dimensions、Balance Plug、Discharge Plug
- **S12 · 首批采购与资料回执：2** (45 分钟) · **必做**
  - **行动:** 保存舵机协议/控制表和同型号CAD；核对电池标准LiPo与EC2。
  - **预期产出:** 带型号与附件版本的首批订单清单子记录2
  - **资源:** [FE-URT-1 Programmer](https://www.feetechrc.com/serial-port-series-steering-gear_50681.html) — FE-URT-1条目

**阶段产出:** 带型号与附件版本的首批订单清单

**产出模板**

- 型号/版本
- 测试条件
- 实测数值/波形/尺寸
- 通过依据
- 需要修改的电路或零件及复测条件

**完成标准**

- 有可复核的记录，而非仅写完成。
- 前置证据缺失时，不把该环节标记为通过。

**自检问题**

- 把资料参数、设计假设和实测结果分开了吗？
- 下一环节是否真的具备输入？

**最小可行路径**

- S11
- S12

**卡住时怎么办**

- 资料缺失时先推进独立的机械/主控验证，不猜测寄存器、线序或连续负载。
- 实测失败则只修改相关电路/零件并回归测试。

**可选分支**

- 扩展测试和返工所需时间另计。

<!-- /atlas-stage -->

<!-- atlas-stage:2 -->
### 阶段 2: 单舵机和主控台架

- **持续时间:** 首轮工程时间盒，采购/打样等待另计
- **每周投入:** 180分钟计划工时
- **必做内容计划用时:** 180 分钟

**目标**

- 单舵机与IMU数据日志

**前置要求**

- 阶段1的相关输入具备

**指定资源**

- [FE-URT-1 Programmer](https://www.feetechrc.com/serial-port-series-steering-gear_50681.html) — **使用位置:** FE-URT-1条目; **推荐理由:** FE-URT1-C001：USB转TTL/485调试板，52×38.4×16mm，最高1Mbps。 · **必做**
- [Microduck software repository](https://github.com/pollen-robotics/microduck) — **使用位置:** 本地同源 duck-control/src/imu.rs、bus.rs、deploy/audio/*.dts; **推荐理由:** 本地运行时要求躯干IMU；旧实现从Dynamixel ID200读取12字节；音频使用aic3104卡名。 · **必做**
- [LSM6DSV16X Hardware Overview](https://docs.sparkfun.com/SparkFun_6DoF_LSM6DSV16X/hardware_overview/) — **使用位置:** Board Outline / I2C / Power; **推荐理由:** Micro版SEN-21336为0.3×0.75英寸，即7.62×19.05mm；I2C默认0x6B；3.3V使用。 · **必做**

**学习单元**

- **S21 · 单舵机和主控台架：1** (90 分钟) · **必做**
  - **行动:** 先在6V限流台架进行舵机空载通信与机械试装；承载试验待真实额定工况确认。
  - **预期产出:** 单舵机与IMU数据日志子记录1
  - **资源:** [FE-URT-1 Programmer](https://www.feetechrc.com/serial-port-series-steering-gear_50681.html) — FE-URT-1条目
- **S22 · 单舵机和主控台架：2** (90 分钟) · **必做**
  - **行动:** 启动Radxa，处理UART2控制台；验证IMU身份、轴向、数据新鲜度。
  - **预期产出:** 单舵机与IMU数据日志子记录2
  - **资源:** [Microduck software repository](https://github.com/pollen-robotics/microduck) — 本地同源 duck-control/src/imu.rs、bus.rs、deploy/audio/*.dts

**阶段产出:** 单舵机与IMU数据日志

**产出模板**

- 型号/版本
- 测试条件
- 实测数值/波形/尺寸
- 通过依据
- 需要修改的电路或零件及复测条件

**完成标准**

- 有可复核的记录，而非仅写完成。
- 前置证据缺失时，不把该环节标记为通过。

**自检问题**

- 把资料参数、设计假设和实测结果分开了吗？
- 下一环节是否真的具备输入？

**最小可行路径**

- S21
- S22

**卡住时怎么办**

- 资料缺失时先推进独立的机械/主控验证，不猜测寄存器、线序或连续负载。
- 实测失败则只修改相关电路/零件并回归测试。

**可选分支**

- 扩展测试和返工所需时间另计。

<!-- /atlas-stage -->

<!-- atlas-stage:3 -->
### 阶段 3: 真实器件的机械占位

- **持续时间:** 首轮工程时间盒，采购/打样等待另计
- **每周投入:** 240分钟计划工时
- **必做内容计划用时:** 240 分钟

**目标**

- RA3占位模型与试配尺寸表

**前置要求**

- 阶段2的相关输入具备

**指定资源**

- [Radxa Camera 8M 219 Product Brief Rev 1.0](https://dl.radxa.com/accessories/camera-8m-219/radxa_camera_8m_219_product_brief_Revision_1.0.pdf) — **使用位置:** 印刷页5 Physical specifications；页4 FPC; **推荐理由:** 板32±0.2mm见方，孔距28±0.1mm，孔径2±0.1mm；镜头前凸15.98±0.2mm，PCB1.6mm；背面连接器另计。 · **必做**
- [Radxa Heatsink 5519A](https://radxa.com/products/accessories/heatsink-5519a/) — **使用位置:** 适配机型; **推荐理由:** 5519A为ZERO 3W/3E配套散热器。 · **必做**
- [Gens ace 850mAh 7.4V 2S1P 60C EC2](https://gensace.de/products/gens-ace-850mah-7-4v-2s1p-60c-lipo-battery-pack-with-ec2-plug) — **使用位置:** Product Specs：Capacity、Voltage、C rate、Dimensions、Balance Plug、Discharge Plug; **推荐理由:** GEA8502S60E2；7.4V/850mAh/60C；约58×32×20mm、55g；EC2和JST-XHR-3P。 · **必做**

**学习单元**

- **S31 · 真实器件的机械占位：1** (120 分钟) · **必做**
  - **行动:** 用到货尺寸/CAD更新电池、相机、散热器、排针及线束的包络。
  - **预期产出:** RA3占位模型与试配尺寸表子记录1
  - **资源:** [Radxa Camera 8M 219 Product Brief Rev 1.0](https://dl.radxa.com/accessories/camera-8m-219/radxa_camera_8m_219_product_brief_Revision_1.0.pdf) — 印刷页5 Physical specifications；页4 FPC
- **S32 · 真实器件的机械占位：2** (120 分钟) · **必做**
  - **行动:** 打印小试配件；记录孔位、螺钉、插拔与线头所需余量。
  - **预期产出:** RA3占位模型与试配尺寸表子记录2
  - **资源:** [Radxa Heatsink 5519A](https://radxa.com/products/accessories/heatsink-5519a/) — 适配机型

**阶段产出:** RA3占位模型与试配尺寸表

**产出模板**

- 型号/版本
- 测试条件
- 实测数值/波形/尺寸
- 通过依据
- 需要修改的电路或零件及复测条件

**完成标准**

- 有可复核的记录，而非仅写完成。
- 前置证据缺失时，不把该环节标记为通过。

**自检问题**

- 把资料参数、设计假设和实测结果分开了吗？
- 下一环节是否真的具备输入？

**最小可行路径**

- S31
- S32

**卡住时怎么办**

- 资料缺失时先推进独立的机械/主控验证，不猜测寄存器、线序或连续负载。
- 实测失败则只修改相关电路/零件并回归测试。

**可选分支**

- 扩展测试和返工所需时间另计。

<!-- /atlas-stage -->

<!-- atlas-stage:4 -->
### 阶段 4: 两块PCB首轮设计

- **持续时间:** 首轮工程时间盒，采购/打样等待另计
- **每周投入:** 720分钟计划工时
- **必做内容计划用时:** 720 分钟

**目标**

- 原理图、PCB、Gerber、BOM与贴片坐标

**前置要求**

- 阶段3的相关输入具备

**指定资源**

- [LM74502DDFR](https://www.ti.com/lit/ds/symlink/lm74502.pdf) — **使用位置:** p1 / Pin functions / Typical application; **推荐理由:** 3.2–65V控制器，外接共源背靠背NFET；EN/UVLO拉低关断；导通时不提供反向电流阻断。 · **必做**
- [TLV320AIC3104](https://www.ti.com/lit/ds/symlink/tlv320aic3104.pdf) — **使用位置:** Pin functions / Power / Digital interface; **推荐理由:** 保留AIC3104的I2S/I2C音频路线；IO/模拟3.3V、内核1.8V；具体供电与时序按数据表。 · **必做**
- [451/453 Series Nano2 Fuse](https://www.littelfuse.com/assetdocs/fuse-451-and-453-datasheet?assetguid=533cd5cc-956c-4243-867f-6ab5a62f6ba1) — **使用位置:** p1–3 电气特性/时间电流曲线/外形; **推荐理由:** 451系列贴片保险丝，约6.10×2.69×2.69mm；规格覆盖3A、5A和15A。 · **必做**

**学习单元**

- **S41 · 两块PCB首轮设计：1** (360 分钟) · **必做**
  - **行动:** 按配电/音频架构完成原理图、网表和ERC；补上UVLO/回馈/手动ARM电路。
  - **预期产出:** 原理图、PCB、Gerber、BOM与贴片坐标子记录1
  - **资源:** [LM74502DDFR](https://www.ti.com/lit/ds/symlink/lm74502.pdf) — p1 / Pin functions / Typical application
- **S42 · 两块PCB首轮设计：2** (360 分钟) · **必做**
  - **行动:** 完成布板、制造检查和3D装配复核，提交板厂PCB及SMT资料。
  - **预期产出:** 原理图、PCB、Gerber、BOM与贴片坐标子记录2
  - **资源:** [TLV320AIC3104](https://www.ti.com/lit/ds/symlink/tlv320aic3104.pdf) — Pin functions / Power / Digital interface

**阶段产出:** 原理图、PCB、Gerber、BOM与贴片坐标

**产出模板**

- 型号/版本
- 测试条件
- 实测数值/波形/尺寸
- 通过依据
- 需要修改的电路或零件及复测条件

**完成标准**

- 有可复核的记录，而非仅写完成。
- 前置证据缺失时，不把该环节标记为通过。

**自检问题**

- 把资料参数、设计假设和实测结果分开了吗？
- 下一环节是否真的具备输入？

**最小可行路径**

- S41
- S42

**卡住时怎么办**

- 资料缺失时先推进独立的机械/主控验证，不猜测寄存器、线序或连续负载。
- 实测失败则只修改相关电路/零件并回归测试。

**可选分支**

- 扩展测试和返工所需时间另计。

<!-- /atlas-stage -->

<!-- atlas-stage:5 -->
### 阶段 5: 电气与多模块联调

- **持续时间:** 首轮工程时间盒，采购/打样等待另计
- **每周投入:** 420分钟计划工时
- **必做内容计划用时:** 420 分钟

**目标**

- 电源与传感器联调报告

**前置要求**

- 阶段4的相关输入具备

**指定资源**

- [S13V30F5 #4082](https://www.pololu.com/product/4082) — **使用位置:** Features / Output-current graph; **推荐理由:** 5V升降压，2.8–22V输入；约22.9×22.9×9.7mm；典型约3A。 · **必做**
- [Radxa Camera 8M 219](https://docs.radxa.com/en/accessories/camera/camera-8m-219) — **使用位置:** Default FPC / FPC Cable; **推荐理由:** 原配150mm同面22P 0.5mm转15P 1.0mm，官方明确支持ZERO 3W/3E。 · **必做**
- [Grove NFC Wiki](https://wiki.seeedstudio.com/Grove_NFC/) — **使用位置:** Specifications / Hardware overview; **推荐理由:** 控制板25.43×20.35mm、3.3V、UART默认，可连接独立PCB天线。 · **必做**

**学习单元**

- **S51 · 电气与多模块联调：1** (210 分钟) · **必做**
  - **行动:** 记录5V输出、启动浪涌、母线回馈、线束温升，验证急停及复位不会自行恢复运动。
  - **预期产出:** 电源与传感器联调报告子记录1
  - **资源:** [S13V30F5 #4082](https://www.pololu.com/product/4082) — Features / Output-current graph
- **S52 · 电气与多模块联调：2** (210 分钟) · **必做**
  - **行动:** 逐项完成摄像、录放音、测距、IMU和NFC，再检查并发通信与50Hz控制时间。
  - **预期产出:** 电源与传感器联调报告子记录2
  - **资源:** [Radxa Camera 8M 219](https://docs.radxa.com/en/accessories/camera/camera-8m-219) — Default FPC / FPC Cable

**阶段产出:** 电源与传感器联调报告

**产出模板**

- 型号/版本
- 测试条件
- 实测数值/波形/尺寸
- 通过依据
- 需要修改的电路或零件及复测条件

**完成标准**

- 有可复核的记录，而非仅写完成。
- 前置证据缺失时，不把该环节标记为通过。

**自检问题**

- 把资料参数、设计假设和实测结果分开了吗？
- 下一环节是否真的具备输入？

**最小可行路径**

- S51
- S52

**卡住时怎么办**

- 资料缺失时先推进独立的机械/主控验证，不猜测寄存器、线序或连续负载。
- 实测失败则只修改相关电路/零件并回归测试。

**可选分支**

- 扩展测试和返工所需时间另计。

<!-- /atlas-stage -->

<!-- atlas-stage:6 -->
### 阶段 6: 单腿到整机放行复核

- **持续时间:** 首轮工程时间盒，采购/打样等待另计
- **每周投入:** 240分钟计划工时
- **必做内容计划用时:** 240 分钟

**目标**

- 明确已通过/待返工的制造清单

**前置要求**

- 阶段5的相关输入具备

**指定资源**

- [Microduck software repository](https://github.com/pollen-robotics/microduck) — **使用位置:** 本地同源 duck-control/src/imu.rs、bus.rs、deploy/audio/*.dts; **推荐理由:** 本地运行时要求躯干IMU；旧实现从Dynamixel ID200读取12字节；音频使用aic3104卡名。 · **必做**
- [Microduck RL repository](https://github.com/pollen-robotics/microduck_rl) — **使用位置:** 本地 robot_allcollisions.xml 的 sensor/site 与 microduck_constants.py; **推荐理由:** 本地训练传感器引用trunk_base的imu站点，而非head_imu；执行器仍是xl330/m6。 · **必做**
- [Gens ace 850mAh 7.4V 2S1P 60C EC2](https://gensace.de/products/gens-ace-850mah-7-4v-2s1p-60c-lipo-battery-pack-with-ec2-plug) — **使用位置:** Product Specs：Capacity、Voltage、C rate、Dimensions、Balance Plug、Discharge Plug; **推荐理由:** GEA8502S60E2；7.4V/850mAh/60C；约58×32×20mm、55g；EC2和JST-XHR-3P。 · **必做**

**学习单元**

- **S61 · 单腿到整机放行复核：1** (120 分钟) · **必做**
  - **行动:** 完成单腿承载、全角度走线检查；实测舵机参数并更新质量/惯量。
  - **预期产出:** 明确已通过/待返工的制造清单子记录1
  - **资源:** [Microduck software repository](https://github.com/pollen-robotics/microduck) — 本地同源 duck-control/src/imu.rs、bus.rs、deploy/audio/*.dts
- **S62 · 单腿到整机放行复核：2** (120 分钟) · **必做**
  - **行动:** 逐件审核RA3打印清单；整机与步态验证没有通过的项目继续保留开放。
  - **预期产出:** 明确已通过/待返工的制造清单子记录2
  - **资源:** [Microduck RL repository](https://github.com/pollen-robotics/microduck_rl) — 本地 robot_allcollisions.xml 的 sensor/site 与 microduck_constants.py

**阶段产出:** 明确已通过/待返工的制造清单

**产出模板**

- 型号/版本
- 测试条件
- 实测数值/波形/尺寸
- 通过依据
- 需要修改的电路或零件及复测条件

**完成标准**

- 有可复核的记录，而非仅写完成。
- 前置证据缺失时，不把该环节标记为通过。

**自检问题**

- 把资料参数、设计假设和实测结果分开了吗？
- 下一环节是否真的具备输入？

**最小可行路径**

- S61
- S62

**卡住时怎么办**

- 资料缺失时先推进独立的机械/主控验证，不猜测寄存器、线序或连续负载。
- 实测失败则只修改相关电路/零件并回归测试。

**可选分支**

- 扩展测试和返工所需时间另计。

<!-- /atlas-stage -->


## 5. 资源出处

### 证据说明

<!-- atlas-evidence:1 -->
<a id="evidence-E_battery"></a>
#### E_battery · GEA8502S60E2；7.4V/850mAh/60C；约58×32×20mm、55g；EC2和JST-XHR-3P。

- **判断类型:** fact
- **可信度:** high
- **信息截至:** 2026-09-05
- **核验说明:** 网页库存标记混杂，尺寸为约值；C数是厂家标称而非本机实测。

- [Gens ace 850mAh 7.4V 2S1P 60C EC2](https://gensace.de/products/gens-ace-850mah-7-4v-2s1p-60c-lipo-battery-pack-with-ec2-plug) — Product Specs：Capacity、Voltage、C rate、Dimensions、Balance Plug、Discharge Plug

<!-- /atlas-evidence -->

<!-- atlas-evidence:2 -->
<a id="evidence-E_radxa"></a>
#### E_radxa · RK3566；可选eMMC与40针排针；22针0.5mm CSI；官方列出配套散热器和相机。

- **判断类型:** fact
- **可信度:** high
- **信息截至:** 2026-09-05
- **核验说明:** 具体内存/eMMC和PCB版本以订货回执与丝印为准。

- [Radxa ZERO 3W](https://radxa.com/products/zeros/zero3w/) — 接口与配件

<!-- /atlas-evidence -->

<!-- atlas-evidence:3 -->
<a id="evidence-E_radxa_versions"></a>
#### E_radxa_versions · V1.11与V1.12(AIC8800)分别提供图纸；旧3D文件不自动证明新板元件高度一致。

- **判断类型:** fact
- **可信度:** high
- **信息截至:** 2026-09-05
- **核验说明:** 本地旧STEP有效性问题未在本轮消除。

- [ZERO 3 Hardware Design Downloads](https://docs.radxa.com/en/zero/zero3/download) — Hardware Design

<!-- /atlas-evidence -->

<!-- atlas-evidence:4 -->
<a id="evidence-E_gpio"></a>
#### E_gpio · GPIO为3.3V；UART2占8/10；I2C4占27/28；UART4占16/18；UART5占32/33。

- **判断类型:** fact
- **可信度:** high
- **信息截至:** 2026-09-05
- **核验说明:** UART2默认兼任控制台；需处理启动日志与引导输入。

- [ZERO 3 Hardware Interface](https://docs.radxa.com/en/zero/zero3/hardware-design/hardware-interface) — 40 PIN GPIO / Debug Serial / MIPI CSI

<!-- /atlas-evidence -->

<!-- atlas-evidence:5 -->
<a id="evidence-E_heat"></a>
#### E_heat · 5519A为ZERO 3W/3E配套散热器。

- **判断类型:** fact
- **可信度:** high
- **信息截至:** 2026-09-05
- **核验说明:** 官网正文未列完整高度，本轮不虚构其包络；到货或有效CAD后复核叠高。

- [Radxa Heatsink 5519A](https://radxa.com/products/accessories/heatsink-5519a/) — 适配机型

<!-- /atlas-evidence -->

<!-- atlas-evidence:6 -->
<a id="evidence-E_camera"></a>
#### E_camera · 板32±0.2mm见方，孔距28±0.1mm，孔径2±0.1mm；镜头前凸15.98±0.2mm，PCB1.6mm；背面连接器另计。

- **判断类型:** fact
- **可信度:** high
- **信息截至:** 2026-09-05
- **核验说明:** 前凸尺寸不是整个模组总厚；旧25×24占位和M12镜头座需要改。

- [Radxa Camera 8M 219 Product Brief Rev 1.0](https://dl.radxa.com/accessories/camera-8m-219/radxa_camera_8m_219_product_brief_Revision_1.0.pdf) — 印刷页5 Physical specifications；页4 FPC

<!-- /atlas-evidence -->

<!-- atlas-evidence:7 -->
<a id="evidence-E_camera_cable"></a>
#### E_camera_cable · 原配150mm同面22P 0.5mm转15P 1.0mm，官方明确支持ZERO 3W/3E。

- **判断类型:** fact
- **可信度:** high
- **信息截至:** 2026-09-05
- **核验说明:** 资料同时出现不同视角口径，按D74/H62/V49作初始标定参考，最终重标定。

- [Radxa Camera 8M 219](https://docs.radxa.com/en/accessories/camera/camera-8m-219) — Default FPC / FPC Cable

<!-- /atlas-evidence -->

<!-- atlas-evidence:8 -->
<a id="evidence-E_imu"></a>
#### E_imu · Micro版SEN-21336为0.3×0.75英寸，即7.62×19.05mm；I2C默认0x6B；3.3V使用。

- **判断类型:** fact
- **可信度:** high
- **信息截至:** 2026-09-05
- **核验说明:** 模组不是Dynamixel ID200设备；需要新的I2C读取后端。

- [LSM6DSV16X Hardware Overview](https://docs.sparkfun.com/SparkFun_6DoF_LSM6DSV16X/hardware_overview/) — Board Outline / I2C / Power

<!-- /atlas-evidence -->

<!-- atlas-evidence:9 -->
<a id="evidence-E_imu_product"></a>
#### E_imu_product · SEN-21336为Micro版，SEN-21325为较大的标准版；两者不要混买。

- **判断类型:** fact
- **可信度:** high
- **信息截至:** 2026-09-05
- **核验说明:** 本轮选Micro版；保留原厂Qwiic线及原理图。

- [SparkFun LSM6DSV16X Hookup Guide](https://docs.sparkfun.com/SparkFun_6DoF_LSM6DSV16X/) — Required Materials

<!-- /atlas-evidence -->

<!-- atlas-evidence:10 -->
<a id="evidence-E_tof"></a>
#### E_tof · 约13×23×3mm；3.2–5.5V；峰值150mA；I/O跟随VIN；SPI/I2C脚拉低选择I2C。

- **判断类型:** fact
- **可信度:** high
- **信息截至:** 2026-09-05
- **核验说明:** 本方案VIN固定3.3V；短线连接，勿误用5V逻辑接Radxa。

- [VL53L8CX Carrier #3419](https://www.pololu.com/product/3419) — Features / Connections

<!-- /atlas-evidence -->

<!-- atlas-evidence:11 -->
<a id="evidence-E_speaker"></a>
#### E_speaker · 20mm直径、3.9mm高、8Ω、额定1.2W、2.5g。

- **判断类型:** fact
- **可信度:** high
- **信息截至:** 2026-09-05
- **核验说明:** 与旧20×5占位不同；安装、防漏气及声孔仍要实际验证。

- [AS02008MR-HT-WP](https://puiaudio.com/product/speakers-and-receivers/as02008mr-ht-wp) — Dimensions & Specifications

<!-- /atlas-evidence -->

<!-- atlas-evidence:12 -->
<a id="evidence-E_mic"></a>
#### E_mic · 4×4×1.5mm顶入声模拟驻极体，标称3V、负载2.2kΩ。

- **判断类型:** fact
- **可信度:** medium
- **信息截至:** 2026-09-05
- **核验说明:** 初次搜索的厂家正文与数据表已核对；后续直接抓取出现403。

- [CMC-4015-25T](https://www.sameskydevices.com/product/audio/microphones/electret-condenser-microphones/cmc-4015-25t) — Specifications；datasheet p1

<!-- /atlas-evidence -->

<!-- atlas-evidence:13 -->
<a id="evidence-E_codec"></a>
#### E_codec · 保留AIC3104的I2S/I2C音频路线；IO/模拟3.3V、内核1.8V；具体供电与时序按数据表。

- **判断类型:** fact
- **可信度:** high
- **信息截至:** 2026-09-05
- **核验说明:** 需要PCB与SMT，不是可直接购买的Microduck成品HAT。

- [TLV320AIC3104](https://www.ti.com/lit/ds/symlink/tlv320aic3104.pdf) — Pin functions / Power / Digital interface

<!-- /atlas-evidence -->

<!-- atlas-evidence:14 -->
<a id="evidence-E_amp"></a>
#### E_amp · TPA2010D1作为5V单声道功放，接AIC3104差分线路输出。

- **判断类型:** fact
- **可信度:** high
- **信息截至:** 2026-09-05
- **核验说明:** 限制输出到所选扬声器额定功率以内，回路与麦克风分开。

- [TPA2010D1](https://www.ti.com/lit/ds/symlink/tpa2010d1.pdf) — Application / Gain setting

<!-- /atlas-evidence -->

<!-- atlas-evidence:15 -->
<a id="evidence-E_buck"></a>
#### E_buck · 5V升降压，2.8–22V输入；约22.9×22.9×9.7mm；典型约3A。

- **判断类型:** fact
- **可信度:** high
- **信息截至:** 2026-09-05
- **核验说明:** 实际连续电流受输入电压、散热影响；3A不是无条件保证。

- [S13V30F5 #4082](https://www.pololu.com/product/4082) — Features / Output-current graph

<!-- /atlas-evidence -->

<!-- atlas-evidence:16 -->
<a id="evidence-E_power"></a>
#### E_power · 3.2–65V控制器，外接共源背靠背NFET；EN/UVLO拉低关断；导通时不提供反向电流阻断。

- **判断类型:** fact
- **可信度:** high
- **信息截至:** 2026-09-05
- **核验说明:** 本轮替换原LM74800思路，保留回馈通路；断电后回馈尖峰仍需设计验证。

- [LM74502DDFR](https://www.ti.com/lit/ds/symlink/lm74502.pdf) — p1 / Pin functions / Typical application

<!-- /atlas-evidence -->

<!-- atlas-evidence:17 -->
<a id="evidence-E_power_reverse"></a>
#### E_power_reverse · 共源背靠背NFET在控制器有效且栅极导通时允许双向电流。

- **判断类型:** fact
- **可信度:** high
- **信息截至:** 2026-09-05
- **核验说明:** 属于该电路配置的应用答复，不替代整机回馈测试。

- [LM74502 bidirectional current application](https://e2e.ti.com/support/power-management-group/power-management/f/power-management-forum/1503649/lm74502-lm74502-as-high-side-driver-in-back-to-back-connected-common-source-mosfet) — TI工程师答复

<!-- /atlas-evidence -->

<!-- atlas-evidence:18 -->
<a id="evidence-E_fet"></a>
#### E_fet · 60V NFET，标称5×6mm封装；本方案两颗共源背靠背。

- **判断类型:** fact
- **可信度:** high
- **信息截至:** 2026-09-05
- **核验说明:** 导通损耗按实际栅压与温度核算，不只引用室温典型电阻。

- [CSD18540Q5B](https://www.ti.com/lit/gpn/CSD18540Q5B) — Product summary / Package

<!-- /atlas-evidence -->

<!-- atlas-evidence:19 -->
<a id="evidence-E_digital_supply"></a>
#### E_digital_supply · 3–17V、1A降压器，固定输出版本用于数字3.3V；选DSG封装。

- **判断类型:** fact
- **可信度:** high
- **信息截至:** 2026-09-05
- **核验说明:** 官网直售显示缺货；PCB投产前由SMT供应商确认授权渠道供货。

- [TPS62162DSGR](https://www.ti.com/product/TPS62162/part-details/TPS62162DSGR) — Features / Part details

<!-- /atlas-evidence -->

<!-- atlas-evidence:20 -->
<a id="evidence-E_fuse"></a>
#### E_fuse · 451系列贴片保险丝，约6.10×2.69×2.69mm；规格覆盖3A、5A和15A。

- **判断类型:** fact
- **可信度:** high
- **信息截至:** 2026-09-05
- **核验说明:** 本轮额定值为样机起点；按时间-电流曲线、I²t及线束温升复核，不承担精确电机限流。

- [451/453 Series Nano2 Fuse](https://www.littelfuse.com/assetdocs/fuse-451-and-453-datasheet?assetguid=533cd5cc-956c-4243-867f-6ab5a62f6ba1) — p1–3 电气特性/时间电流曲线/外形

<!-- /atlas-evidence -->

<!-- atlas-evidence:21 -->
<a id="evidence-E_cap"></a>
#### E_cap · FR系列，16V/470µF，直径8mm、长11.5mm。

- **判断类型:** fact
- **可信度:** high
- **信息截至:** 2026-09-05
- **核验说明:** 较旧10mm长度占位增加1.5mm；横置及引脚固定需要重画。

- [EEUFR1C471](https://industrial.panasonic.com/kr/products/pt/aluminum-cap-lead/models?model_number=EEUFR1C471&order=model&sort=asc) — Model table

<!-- /atlas-evidence -->

<!-- atlas-evidence:22 -->
<a id="evidence-E_estop"></a>
#### E_estop · 16mm安装系列、29mm红蘑菇头、2NC、焊接端子。

- **判断类型:** fact
- **可信度:** high
- **信息截至:** 2026-09-05
- **核验说明:** 首版放外置有线盒；开关器件合格不等于整机急停系统认证。

- [XA1E-BV302-R](https://www.idec.com/en-us/switches-indicator-lights/switches-pushbuttons/emergency-stop-switches/xa-16mm-estop/xa1e-bv302-r) — Key Features / Mechanical Specifications

<!-- /atlas-evidence -->

<!-- atlas-evidence:23 -->
<a id="evidence-E_nfc"></a>
#### E_nfc · 113020006是PN532读卡模块，页面显示有货；不是ST25DV64动态标签。

- **判断类型:** fact
- **可信度:** high
- **信息截至:** 2026-09-05
- **核验说明:** 报价/库存会变化；装机需新增NFC程序。

- [Grove NFC PN532 113020006](https://www.seeedstudio.com/Grove-NFC.html) — SKU / Product summary

<!-- /atlas-evidence -->

<!-- atlas-evidence:24 -->
<a id="evidence-E_nfc_wiring"></a>
#### E_nfc_wiring · 控制板25.43×20.35mm、3.3V、UART默认，可连接独立PCB天线。

- **判断类型:** fact
- **可信度:** high
- **信息截至:** 2026-09-05
- **核验说明:** 两个模块分别走UART4与UART5；保持原配天线和馈线，不自行裁剪。

- [Grove NFC Wiki](https://wiki.seeedstudio.com/Grove_NFC/) — Specifications / Hardware overview

<!-- /atlas-evidence -->

<!-- atlas-evidence:25 -->
<a id="evidence-E_nfc_antenna"></a>
#### E_nfc_antenna · 配套天线PCB为28×30.5mm；较大尺寸是包装尺寸。

- **判断类型:** fact
- **可信度:** high
- **信息截至:** 2026-09-05
- **核验说明:** 以所发模块的配套天线为准，金属与壳体会改变读距。

- [NFC Antenna Dimensions](https://forum.seeedstudio.com/t/nfc-antenna-dimensions/6776) — 2019-04-26 技术支持回复

<!-- /atlas-evidence -->

<!-- atlas-evidence:26 -->
<a id="evidence-E_charger"></a>
#### E_charger · 选择B6neo SK-100198，支持DC/USB-PD输入和平衡充电。

- **判断类型:** fact
- **可信度:** high
- **信息截至:** 2026-09-05
- **核验说明:** 配原厂说明书按标准LiPo 2S设置，非LiHV模式；不在机器人内充电。

- [B6neo Series](https://www.skyrc.com/b6neo-series) — 型号表 / Specification

<!-- /atlas-evidence -->

<!-- atlas-evidence:27 -->
<a id="evidence-E_debug"></a>
#### E_debug · FE-URT1-C001：USB转TTL/485调试板，52×38.4×16mm，最高1Mbps。

- **判断类型:** fact
- **可信度:** high
- **信息截至:** 2026-09-05
- **核验说明:** 仅台架工具。HD1910的机械参数来自用户附件，不由这个产品页证明。

- [FE-URT-1 Programmer](https://www.feetechrc.com/serial-port-series-steering-gear_50681.html) — FE-URT-1条目

<!-- /atlas-evidence -->

<!-- atlas-evidence:28 -->
<a id="evidence-E_header"></a>
#### E_header · 2.54mm间距，双排40针直插母座。

- **判断类型:** fact
- **可信度:** high
- **信息截至:** 2026-09-05
- **核验说明:** 精确啮合尺寸按配置图；12mm铜柱是设计起点，不是已验收叠高。

- [SSW-120-02-G-D](https://www.samtec.com/products/ssw-120-02-g-d) — 产品标题/Prints

<!-- /atlas-evidence -->

<!-- atlas-evidence:29 -->
<a id="evidence-E_runtime"></a>
#### E_runtime · 本地运行时要求躯干IMU；旧实现从Dynamixel ID200读取12字节；音频使用aic3104卡名。

- **判断类型:** fact
- **可信度:** high
- **信息截至:** 2026-09-05
- **核验说明:** 采用独立I2C IMU要改RobotIo后端；不是仅插线即可运行。

- [Microduck software repository](https://github.com/pollen-robotics/microduck) — 本地同源 duck-control/src/imu.rs、bus.rs、deploy/audio/*.dts

<!-- /atlas-evidence -->

<!-- atlas-evidence:30 -->
<a id="evidence-E_rl"></a>
#### E_rl · 本地训练传感器引用trunk_base的imu站点，而非head_imu；执行器仍是xl330/m6。

- **判断类型:** fact
- **可信度:** high
- **信息截至:** 2026-09-05
- **核验说明:** 硬件选型不等于HD电机辨识、策略重训或行走验证。

- [Microduck RL repository](https://github.com/pollen-robotics/microduck_rl) — 本地 robot_allcollisions.xml 的 sensor/site 与 microduck_constants.py

<!-- /atlas-evidence -->

<!-- atlas-evidence:31 -->
<a id="evidence-E_alt_camera"></a>
#### E_alt_camera · 非IR的160°版本为25×24mm板框；与32×32mm Radxa模组不同。

- **判断类型:** fact
- **可信度:** high
- **信息截至:** 2026-09-05
- **核验说明:** 本轮不选；若广角优先，需重验FPC、驱动与标定，而非直接沿用原占位。

- [IMX219-160 Camera](https://www.waveshare.com/product/risc-v/cameras/imx219-160-camera.htm) — Specifications / Version Options

<!-- /atlas-evidence -->

<!-- atlas-evidence:32 -->
<a id="evidence-E_alt_audio"></a>
#### E_alt_audio · 现成USB音频模块是一条减少自制音频电路的路线。

- **判断类型:** fact
- **可信度:** high
- **信息截至:** 2026-09-05
- **核验说明:** 本轮不选；机械空间、USB走线和ALSA设备名需另改，不是AIC3104 HAT的直接替身。

- [USB TO AUDIO](https://www.waveshare.com/product/usb-to-audio.htm) — Product details

<!-- /atlas-evidence -->

**资源筛选说明:** 商业规格能支持型号和参数，不等于本机实测性能；附件与本地代码核验另记在项目数据中。

<!-- atlas-source:1 -->
### 厂家规格与手册

按文中定位查阅并核对版本。

- [Gens ace 850mAh 7.4V 2S1P 60C EC2](https://gensace.de/products/gens-ace-850mah-7-4v-2s1p-60c-lipo-battery-pack-with-ec2-plug) — Gens ace; Product Specs：Capacity、Voltage、C rate、Dimensions、Balance Plug、Discharge Plug
- [Radxa ZERO 3W](https://radxa.com/products/zeros/zero3w/) — Radxa; 接口与配件
- [ZERO 3 Hardware Design Downloads](https://docs.radxa.com/en/zero/zero3/download) — Radxa; Hardware Design
- [ZERO 3 Hardware Interface](https://docs.radxa.com/en/zero/zero3/hardware-design/hardware-interface) — Radxa; 40 PIN GPIO / Debug Serial / MIPI CSI
- [Radxa Heatsink 5519A](https://radxa.com/products/accessories/heatsink-5519a/) — Radxa; 适配机型
- [Radxa Camera 8M 219 Product Brief Rev 1.0](https://dl.radxa.com/accessories/camera-8m-219/radxa_camera_8m_219_product_brief_Revision_1.0.pdf) — Radxa; 印刷页5 Physical specifications；页4 FPC
- [Radxa Camera 8M 219](https://docs.radxa.com/en/accessories/camera/camera-8m-219) — Radxa; Default FPC / FPC Cable
- [LSM6DSV16X Hardware Overview](https://docs.sparkfun.com/SparkFun_6DoF_LSM6DSV16X/hardware_overview/) — SparkFun; Board Outline / I2C / Power
- [SparkFun LSM6DSV16X Hookup Guide](https://docs.sparkfun.com/SparkFun_6DoF_LSM6DSV16X/) — SparkFun; Required Materials
- [VL53L8CX Carrier #3419](https://www.pololu.com/product/3419) — Pololu; Features / Connections
- [AS02008MR-HT-WP](https://puiaudio.com/product/speakers-and-receivers/as02008mr-ht-wp) — PUI Audio; Dimensions & Specifications
- [CMC-4015-25T](https://www.sameskydevices.com/product/audio/microphones/electret-condenser-microphones/cmc-4015-25t) — Same Sky; Specifications；datasheet p1
- [TLV320AIC3104](https://www.ti.com/lit/ds/symlink/tlv320aic3104.pdf) — Texas Instruments; Pin functions / Power / Digital interface
- [TPA2010D1](https://www.ti.com/lit/ds/symlink/tpa2010d1.pdf) — Texas Instruments; Application / Gain setting
- [S13V30F5 #4082](https://www.pololu.com/product/4082) — Pololu; Features / Output-current graph
- [LM74502DDFR](https://www.ti.com/lit/ds/symlink/lm74502.pdf) — Texas Instruments; p1 / Pin functions / Typical application
- [CSD18540Q5B](https://www.ti.com/lit/gpn/CSD18540Q5B) — Texas Instruments; Product summary / Package
- [TPS62162DSGR](https://www.ti.com/product/TPS62162/part-details/TPS62162DSGR) — Texas Instruments; Features / Part details
- [451/453 Series Nano2 Fuse](https://www.littelfuse.com/assetdocs/fuse-451-and-453-datasheet?assetguid=533cd5cc-956c-4243-867f-6ab5a62f6ba1) — Littelfuse; p1–3 电气特性/时间电流曲线/外形
- [EEUFR1C471](https://industrial.panasonic.com/kr/products/pt/aluminum-cap-lead/models?model_number=EEUFR1C471&order=model&sort=asc) — Panasonic; Model table
- [XA1E-BV302-R](https://www.idec.com/en-us/switches-indicator-lights/switches-pushbuttons/emergency-stop-switches/xa-16mm-estop/xa1e-bv302-r) — IDEC; Key Features / Mechanical Specifications
- [Grove NFC PN532 113020006](https://www.seeedstudio.com/Grove-NFC.html) — Seeed Studio; SKU / Product summary
- [Grove NFC Wiki](https://wiki.seeedstudio.com/Grove_NFC/) — Seeed Studio; Specifications / Hardware overview
- [B6neo Series](https://www.skyrc.com/b6neo-series) — SkyRC; 型号表 / Specification
- [FE-URT-1 Programmer](https://www.feetechrc.com/serial-port-series-steering-gear_50681.html) — FEETECH; FE-URT-1条目
- [SSW-120-02-G-D](https://www.samtec.com/products/ssw-120-02-g-d) — Samtec; 产品标题/Prints
- [IMX219-160 Camera](https://www.waveshare.com/product/risc-v/cameras/imx219-160-camera.htm) — Waveshare; Specifications / Version Options
- [USB TO AUDIO](https://www.waveshare.com/product/usb-to-audio.htm) — Waveshare; Product details

<!-- /atlas-source -->

<!-- atlas-source:2 -->
### 厂家应用支持

按文中定位查阅并核对版本。

- [LM74502 bidirectional current application](https://e2e.ti.com/support/power-management-group/power-management/f/power-management-forum/1503649/lm74502-lm74502-as-high-side-driver-in-back-to-back-connected-common-source-mosfet) — Texas Instruments; TI工程师答复
- [NFC Antenna Dimensions](https://forum.seeedstudio.com/t/nfc-antenna-dimensions/6776) — Seeed Studio 技术支持; 2019-04-26 技术支持回复

<!-- /atlas-source -->

<!-- atlas-source:3 -->
### 项目源代码

按文中定位查阅并核对版本。

- [Microduck software repository](https://github.com/pollen-robotics/microduck) — Pollen Robotics; 本地同源 duck-control/src/imu.rs、bus.rs、deploy/audio/*.dts
- [Microduck RL repository](https://github.com/pollen-robotics/microduck_rl) — Pollen Robotics; 本地 robot_allcollisions.xml 的 sensor/site 与 microduck_constants.py

<!-- /atlas-source -->


---

*AnythingAtlas · 规划学习任何主题的最佳路径*
