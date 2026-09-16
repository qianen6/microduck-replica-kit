<!-- changed_branch: publication -->
<!-- changed_field: repository_state -->
<!-- repository_state: public_ready -->

# Microduck Replica Kit 🦆

一个面向 **Microduck 功能兼容复刻** 的、证据可追溯的社区工程包：锁定公开来源，重建参考装配，整理分阶段 BOM，记录尚未闭合的机械与电控问题，并提供可重复运行的导出与验证脚本。

> This is an independent community reconstruction project. It is not affiliated with or endorsed by Pollen Robotics or Hugging Face.

![AI-assisted exploded-view concept](docs/images/exploded-view-concept.png)

> 上图是依据公开照片与仿真几何制作的概念爆炸图，不是原厂制造图。

## 当前状态

| 项目 | 状态 |
|---|---|
| 官方软件与 RL 来源锁定 | ✅ |
| 47 个公开仿真 STL 的装配关系 | ✅ 可重复生成 |
| 整机参考包络 | ✅ 约 144.1 × 141.0 × 264.0 mm |
| 分阶段 BOM 与台架门禁 | ✅ |
| 制造级公差、走线和装配顺序 | 🧪 待实物测量 |
| `imu_to_dxl` 与电源/HAT PCB | 🧪 待自研 |
| 真机行走 | ⏳ 尚未完成 |

Microduck 官方公开的是软件、仿真与训练栈；机械和电子设计文件并未作为开源硬件发布。因此，本仓库区分三类信息：

1. **上游已公开事实**：代码常量、MJCF、仿真网格与官方规格；
2. **可复现推导**：装配变换、尺寸、紧固件与总线分析；
3. **待测假设**：配合公差、电源架构、线束、持续力矩与真机可靠性。

## 仓库内容

```text
.
├── docs/
│   ├── architecture-rev-a.md       # 功能兼容 Rev A 路线
│   ├── domestic-actuators.md       # 国产执行器候选
│   ├── cost-estimate.md             # 首台原型成本区间
│   ├── open-gaps.md                 # 四个 P0 缺口与关闭条件
│   └── images/                      # 概念图
├── hardware/
│   ├── BOM_REV_A.csv               # 分阶段、带采购门禁的 BOM
│   └── test-coupons.md              # M2/轴承/走线打印试片
├── scripts/
│   ├── fetch_upstream.ps1           # 按提交哈希抓取上游
│   └── export_reference_assembly.py # 从 MJCF 重建装配 STL
├── tools/validate_repo.py           # 静态发布验证
├── source-lock.json                 # 上游 URL、分支和提交哈希
├── NOTICE.md                        # 来源与许可证边界
└── LICENSE                          # 本仓原创代码：Apache-2.0
```

## 快速开始（Windows PowerShell）

```powershell
git clone https://github.com/qianen6/microduck-replica-kit.git
cd microduck-replica-kit

# 1. 拉取锁定版本的上游源码
powershell -ExecutionPolicy Bypass -File scripts/fetch_upstream.ps1

# 2. 创建几何工具环境
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements-geometry.txt

# 3. 从官方 MJCF 生成参考装配
.\.venv\Scripts\python.exe scripts/export_reference_assembly.py `
  upstream/microduck_rl generated/reference-assembly

# 4. 验证仓库
python tools/validate_repo.py --mode modified --readme README.md
```

参考导出在锁定来源上应得到：15 个刚体文件、整机 796,792 个三角面、包络约 `144.1 × 141.0 × 264.0 mm`。

## 推荐实物顺序

1. 单舵机 50 Hz 总线、电流和温升台架；
2. M2 孔、热熔螺母与两种轴承试片；
3. 一条五自由度腿和真实线束；
4. 15 舵机 + IMU 的完整总线；
5. 吊架上的 home / sit / stand / fall-to-limp；
6. 最后运行或重训行走策略。

详见 [Rev A 架构](docs/architecture-rev-a.md) 与 [P0 缺口](docs/open-gaps.md)。

## 上游

- [pollen-robotics/microduck](https://github.com/pollen-robotics/microduck) — 机器人运行时与控制栈
- [pollen-robotics/microduck_rl](https://github.com/pollen-robotics/microduck_rl) — MJCF、仿真网格和 RL 训练
- [fanhao375/microduck-replica](https://github.com/fanhao375/microduck-replica) — 装配、电控和紧固件逆向研究

具体提交见 [`source-lock.json`](source-lock.json)。

## 许可证

- 本仓原创代码、脚本和文字：Apache License 2.0；
- 从上游 Microduck 3D 模型生成的几何衍生物：CC BY-NC-SA 4.0；
- 概念爆炸图：CC BY-NC-SA 4.0；
- 上游项目仍由各自许可证约束。

完整来源和署名见 [`NOTICE.md`](NOTICE.md)。
