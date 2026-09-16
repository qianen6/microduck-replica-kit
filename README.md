<!-- changed_branch: main -->
<!-- changed_field: release_snapshot,publication_metadata,readme.community -->
<!-- repository_state: public_ready -->
<!-- release_snapshot: r9_2026_09_16 -->

# Microduck Replica Kit 🦆

**Microduck 社区复刻工程资料 · R9 工程试装版**

整理机械模型、打印文件、硬件路线和数字检查证据，便于复现与交流。当前路线为 **Pi Zero 2 W + OpenRB-150 + 15 个 HD-1910 + OV5647**；最新机械修订来自 2026-09-13，11 件试装打印工程来自 2026-09-14。

> 独立社区项目，与 Pollen Robotics / Hugging Face 无隶属或背书关系。数字检查通过不等于实物、电气或整机制造验证通过；当前仍为工程试装版。

## 从这里开始

| 你想做什么 | 入口 |
|---|---|
| 查看 / 编辑最新整机 | [R9 Blender 模型](models/r9/Microduck_R9_trial.blend) |
| 获取当前 39 件打印几何 | [STL 文件夹](models/r9/stl) · [逐件清单和 SHA-256](models/r9/parts-manifest.json) |
| 在 Bambu Studio 打开试装排版 | [11 件、两盘、已启用支撑的 3MF](printing/r9/R9_11_parts_support.3mf) |
| 理解文件区别、打印单位与使用顺序 | [打印说明](printing/r9/README.md) |
| 查看 R9 修改及未闭合问题 | [工程评估](docs/current/engineering-review.md) · [原始数字检查摘要](models/r9/evidence) |
| 查看当前硬件路线 | [硬件状态表](hardware/CURRENT_HARDWARE.md) |
| 查阅旧版螺丝、材料、接线与选型 | [历史资料索引](docs/history/README.md) |
| 检查本次发布内容与脱敏策略 | [发布说明](docs/PUBLISHING.md) · [验证记录](VERIFICATION.txt) |

## 当前状态

| 项目 | 状态 |
|---|---|
| 当前整机场景 | 113 个对象；39 件打印对象，15 个舵机参考 |
| R9 几何修订 | 11 个原有网格 + 2 个新增打印件；13 个修订网格历史检查闭合、单连通 |
| 相机与电池 | OV5647 孔位/镜头偏置修订、相机承架、可拆电池后盖 |
| 发布文件复核 | 脱敏前后网格、变换、父子层级与材质分配一致；3MF 的 3D 成员一致 |
| 打印工程 | 11 件试装子集，**不是 39 件全机打印包**；保留支撑设置，不发布机器 G-code |
| 实物配合、电气、动力学与行走 | 尚未完成；不得把静态几何检查当作整机验证 |

历史运动抽样覆盖 235 个姿态，仍记录 82 条新增材料相交；其中包含旧模型已存在的阻挡和名义配合。完整运动范围、轴向叠层和负载试验仍待闭合，详见工程评估。

## 快速使用

```bash
git clone https://github.com/qianen6/microduck-replica-kit.git
cd microduck-replica-kit
python tools/verify_publication.py modified
```

Blender 文件可用 Blender 5.2.1 打开；STL 以毫米为单位，采用零件局部坐标，切片前需确认朝向和尺寸。3MF 面向 Bambu P1S / 0.4 mm 喷嘴与纹理 PEI 板，材料与支撑需按自己的机器重新确认、重新切片。

先试装相机承架、电池盖及单关节，再扩展整机。电池标称输出范围、板卡端口额定值不构成 15 舵机动态供电余量证明。

### 重建上游参考装配（历史参考）

```powershell
powershell -ExecutionPolicy Bypass -File scripts/fetch_upstream.ps1
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements-geometry.txt
.\.venv\Scripts\python.exe scripts/export_reference_assembly.py upstream/microduck_rl generated/reference-assembly
```

该脚本重建锁定的上游仿真参考，不生成本仓 R9 改件。旧 Rev A 的 XL330 BOM 也不是当前 HD-1910 采购清单。

## 目录

```text
models/r9/          当前 Blender、39 件 STL、逐件清单及历史数字检查
printing/r9/        11 件试装 3MF 与打印说明
hardware/           当前路线说明及旧 Rev A BOM
docs/current/       R9 工程评估
docs/history/       R3–R8 选型、接线、紧固件与材料参考
firmware/reference/ 原厂 OpenRB 桥接参考（非已验证 HD-1910 驱动）
scripts/            上游参考获取和装配导出
tools/              可重复运行的发布检查
proof/              发布差异、哈希及脱敏复核摘要
```

## 交流群：鸭子复现

欢迎交流复刻、打印试装和问题复现。下图由项目维护者提供并指定公开用于入群。

<img src="docs/images/wechat-group.jpg" alt="微信群：鸭子复现" width="360">

**有效期：图片注明 7 天内、9 月 23 日前有效（本次发布于 2026-09-16）。** 到期后请通过仓库 Issue 请求更新二维码。二维码是本次明确保留的公开联系入口，其余个人/设备信息不随工作区上传。

## 来源与许可证

- [pollen-robotics/microduck](https://github.com/pollen-robotics/microduck)：运行时与控制栈。
- [pollen-robotics/microduck_rl](https://github.com/pollen-robotics/microduck_rl)：仿真几何与训练栈，锁定版本见 [source-lock.json](source-lock.json)。
- [fanhao375/microduck-replica](https://github.com/fanhao375/microduck-replica) 与 [飞特 v2.0 CAD 参考](https://github.com/fanhao375/microduck-replica-cad/releases/tag/v2.0)：复刻研究及 R9 局部接口参考。
- [ROBOTIS OpenRB-150](https://github.com/ROBOTIS-GIT/OpenRB-150)：原厂串口桥接示例。

本仓原创代码和文字使用 Apache-2.0；上游 Microduck 模型衍生的 Blender、STL、3MF 几何按 CC BY-NC-SA 4.0 保留署名与相同方式共享要求。第三方器件外观仅为装配参考，不冒充原厂开放硬件。群二维码仅用于本项目入群，不作模型或代码许可证授权。详见 [NOTICE.md](NOTICE.md)。
