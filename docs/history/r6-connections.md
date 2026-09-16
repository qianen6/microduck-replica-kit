> 历史参考：对应旧版硬件/几何；不得视为 R9 当前 BOM、接线或打印放行。

# 全硬件连接核对依据

本轮按对话最新选择绘制：Pi Zero 2 W、RPI Robot HAT C1（23eab119）、15个HD-1910-C001、BNO085、已购VL53L8CX载板、套装CSI摄像头、20mm/1W喇叭、自定义双位置PN532 NFC、TCA9548A、NTAG213标签、2S850mAh35C持续XT30电池、BC-4S15D充电器套装及URT-1调试工具。旧采购表中的B6neo与NFC待官方确认备注没有作为当前依据。

## 图1：机内运行

采用最近讨论的基本架构：同一2S电池分出舵机动力与HAT逻辑支路。保险/总开关/欠压与分路配电是功能要求，额定值与实供组件未定，不将PROTECT-R6画成已存在的必购板。独立受控动力关断如需保留，仍需另完成实现；本图不宣称已实现。

| ID | 来源 | 去向 | 核对状态 |
|---|---|---|---|
| P01 | 2S电池XT30正负两线 | 保险、总开关与适当保护，再分路配电 | 拓扑确认；器件额定、导线长度/线径、端子电流待定 |
| P02 | 保护后的2S正极 | HAT J14.2 +BATT | C1原理图核对 |
| P03 | 电池公共负极/GND | HAT J14.1 GND | C1原理图核对 |
| P04 | J14.3 | 留空，不接充电器或GPIO | 该针为TTL DATA，本连接中不用 |
| P05 | 动力分路配电正极 | HD-1910每个接口的2 VCC | 新舵机PDF确认；应足额多点配电，不以一只HAT插头带15个舵机 |
| P06 | 动力公共负极/GND | HD每个接口的3 GND | 新舵机PDF确认 |
| D01 | HAT J13.3 DATA | HD每个接口的1 DATA，共享总线 | C1及HD资料确认；HD驱动仍需适配 |
| D02 | HAT J13.1 GND | 舵机/配电公共地 | 共地，不将大电流回流压到信号线 |
| D03 | J13.2 +BATT | 在这条通信线束内留空 | 板上该脚本身仍带电；避免绕过独立配电 |
| H01 | HAT J4 2×20排母 | Pi Zero 2 W的40针排针，2.54mm间距 | 官方BOM确认。HAT→Pi为5V供电，UART/I2C/I2S通过同一连接 |
| H02 | HAT J1两端 | 喇叭两根引线 | PAM8406桥接输出；两端均不接公共地；1W喇叭需限幅，8Ω仍需核实订单 |
| H03 | HAT板上MEMS麦克风、BMI088 | 板内连接，经J4到主控 | 不增购第二块麦克风/头部IMU，首版以躯干BNO为平衡反馈 |
| S01 | Pi CSI | 已购套装摄像头，使用匹配Zero的排线 | Pi端为Zero CSI；摄像头具体传感器/排线另一端未确认，不写成已购原厂IMX219 |
| S02 | Pi microSD槽 | 已购32GB microSD卡 | 卡槽连接 |
| S03 | 蓝牙手柄 | Pi蓝牙 | 无线连接，无供电线接Pi |
| S04 | Pi I2C1，BCM2/3（物理3/5） | BNO085载板SDA/SCL | 连接规划。具体载板VCC/IO、模式/INT/RST待商家资料；不将另一品牌载板的电气条件套用 |
| S05 | Pi规划软件I2C，BCM23/27（物理16/13） | VL53L8CX载板与TCA9548A上游SDA/SCL | 新总线需配置，非现成默认总线；从GPIO焊盘/适配引出，HAT J6/J7/J8不是同一I2C口 |
| S06 | VL53L8CX载板 | 电源/IO/接口模式/LPn/INT | 待载板资料。裸芯片AVDD3.3V但IO1.2/1.8V，图中不画作确定3.3V GPIO直连 |
| N01 | TCA9548A CH0 | 头部Grove PN532（SKU113020006） | 规划；模块改为I2C模式 |
| N02 | TCA9548A CH1 | 嘴部Grove PN532（同款） | 规划；两同地址设备不同时开通MUX通道 |
| N03 | Pi 3.3V/GND支路 | TCA9548A与两个Grove PN532 | Seeed明确模块工作电压3.3V；合计读写电流约166mA，需计入Pi3.3V预算 |
| N04 | 每个PN532 | 自己的配套分体天线；各天线无线读NTAG213标签 | 不交叉连接天线；不用官方墨水屏协议 |
| N05 | PN532两处射频场 | 软件交替控制 | 切MUX仅隔离I2C，不关射频场；需软件关场轮询，验证相互干扰 |

HAT端线插为EHR-3（EH2.5mm3针）；HD端按厂家称谓AMP2.0-3P。图上针号是电气针号，不是从任意方向观察插头的左右顺序。引脚位置还应依据实际连接器针1标记确认。

## 图2：充电、调试与烧录（互斥/独立场景）

1. 充电：随箱12V适配器→BC-4S15D的DC输入。2S电池三线平衡插头→充电器2S口，具体插头及顺序待实物确认。电池XT30与机器人断开；鳄鱼夹线是输入侧备用线，不是给电池充电的输出线。暂不为该充电方式买XT30主充电线。同型号说明书给1.5A，对850mAh为约1.76C；先核电池允许充电电流，35C是放电规格。
2. 舵机调试：电脑USB数据→URT-1 Mini-USB。独立7.4V限流电源（或合适2S电源，二选一）→URT-1 TTL/SCS侧V/G电源端子。URT TTL/SCS 5264-3AW→对应AMP2.0-3P转接线→单个HD舵机，按S/V/G对接。USB并不提供舵机动力；URT电源端口最大6A，不带15个；调试时HAT与该DATA线断开。
3. 烧录/主控台架：电脑USB→读卡器→microSD写系统，拔卡再插Pi。Pi单独台架使用套装Micro-USB5V电源，此时断开HAT电池输入，避免双电源未经设计并联。可选显示器通过Mini-HDMI转接/HDMI线；可选USB外设通过Micro-USB OTG。电脑可经Wi-Fi/SSH连接Pi。
4. 散热片为贴装/固定，不接电线。万用表、烙铁、卡尺、压接工具是机外工具，不永久接入机器人。轴承、螺钉、铜柱不是电连接对象，图不画机械装配或3D打印件。

## 图的验收边界

核查对象是图中硬件是否齐全、连接端点/标签是否与上述已确认资料一致、互斥工况是否混接。BNO/ToF具体载板电压与接口细节、保护配电额定、软件总线配置及带载能力仍未知，图中使用待核标记，不宣称已经通过实机电气测试。

## 资料

- HAT固定版本：https://github.com/pollen-robotics/elec_RPI_Robot_HAT/tree/23eab11927f95ceca0dfa35bf182caeb7db39ea0 。本地直接读原理图main/dynamixel/audio/sensors及生产BOM，核对J4/J13/J14/J1。TH1位于TTL信号链，不把它误称为15舵机动力保护。
- HD-1910-C001串型规格书-20260907.pdf：用户附件，第3～4页（4～8.4V、7.4V额定0.9A/堵转2A、AMP2.0-3P，1DATA2VCC3GND）。
- URT-1使用说明(1).pdf：用户附件，第1～3页（Mini-USB、5264-3AW、5.08端子、最大6A）。
- 充电器同型号说明书：https://m.media-amazon.com/images/I/B1HhPqCEHML.pdf 。实际版本仍按随箱说明确认。
- Grove NFC：https://wiki.seeedstudio.com/Grove_NFC/ 。3.3V、分体天线、UART默认及改I2C焊点。
- TCA9548A：https://www.ti.com/product/TCA9548A 。
- VL53L8CX：https://www.st.com/resource/en/datasheet/vl53l8cx.pdf 。裸芯片电气条件不等于第三方载板接口电平。
- BNO085参考：https://learn.adafruit.com/adafruit-9-dof-orientation-imu-fusion-breakout-bno085/python-circuitpython 。只用于Pi/I2C兼容性参考，不替代用户紫色载板原理图。
