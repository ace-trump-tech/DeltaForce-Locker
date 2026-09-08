# DeltaForce-OBS-Locker —— 电脑端和手机端均有（S11赛季实测可用 / V5.0.0）

<p align="center">
  <a href="https://github.com/ace-trump-tech/DeltaForce-OBS-Locker/stargazers">
    <img src="https://img.shields.io/github/stars/ace-trump-tech/DeltaForce-OBS-Locker?style=social" alt="GitHub Stars">
  </a>
  &nbsp;&nbsp;&nbsp;
  <a href="https://github.com/ace-trump-tech/DeltaForce-OBS-Locker/network/members">
    <img src="https://img.shields.io/github/forks/ace-trump-tech/DeltaForce-OBS-Locker?style=social" alt="GitHub Forks">
  </a>
</p>

> **本次终于打赢复活赛了，这次采用的是yolov14原团队的最新模型yolo-omni，部署后实战延迟同比降低70%！老版本彻底成为过去时了，8月26日之前的项目需要同步更新，否则会存在bug**

> **🆕 V5.0.0 上线（S11 赛季"回声"适配，2026-09-07）**：在 V4 S10 容器防护服专项隔离的基础上，扩展 S11 潮汐监狱地图视觉模型 + 银翼干员识别隔离 + ACE 4.0 反检测同步；新增 🎣 **自动钓鱼模块**（`core/auto_fish.py`，基于视觉中心 + 多帧投票 + 模拟输入闭环，支持潮汐监狱水域、核电站 AZ3 水库等场景）

<div align="center">
  <img src="https://raw.githubusercontent.com/ace-trump-tech/DeltaForce-Locker/main/Mobile/Protective_suit.jpg" alt="核电站AZ3容器防护服样本" width="400">
  <br>
  <em>△ 核电站AZ3地图中的容器防护服（V3版本曾误判为真人）</em>
</div>

> **🧠 识别逻辑增强**：在视觉识别管线中新增了特定轮廓过滤层，确保容器防护服不再参与目标锁定计算，大幅提升复杂场景下的识别纯净度。

---

## 🎥 手机端功能演示

<div align="center">
  <img src="https://raw.githubusercontent.com/ace-trump-tech/DeltaForce-Locker/main/Mobile/demo_video.gif" alt="手机端功能演示" width="400">
  <br>
  <em>手机端 APK 核心效果（画面吸附 / 模拟输入演示）</em>
</div>

---

## 🚀 如何获取本项目（无论电脑端还是手机端）

请按照以下三步操作：

![Star -> Fork -> Download 流程示意图](https://raw.githubusercontent.com/ace-trump-tech/DeltaForce-Locker/main/Mobile/demo.png)

1. **⭐ Star**  
   点击本仓库右上角的 **Star** 按钮，申请自己的使用权限。

2. **⑂ Fork**  
   点击 **Fork** 按钮，将本仓库复制到你自己的 GitHub 账号下，不然无法进行修改。

3. **⬇️ Download**  
   在你自己 Fork 后的仓库页面，点击 **Code → Download ZIP** 下载压缩包。  

> 💡 **电脑端** 代码位于 `desktop/` 文件夹，**手机端** 脚本位于 `mobile/` 文件夹。下载后请根据对应子项目的 README 进行操作。
> 
> 若下载后的项目其中存在空文件，请检查是否严格以上三步进行操作

> ⚠️ **重要提醒**：无论电脑端还是手机端，AI 识别功能都依赖 **YOLO-omni 预训练权重文件**。  
> **请务必先前往以下链接下载最新的模型权重文件**，否则后续运行会因缺少模型而失败，**8月25日之前已经下载好的需要进行更新**：  
> 👉 [**yolo-omni官方链接点击跳转**](https://github.com/z637826/yolo-omni)  
> 下载后请根据电脑端或手机端的 README 指引放置权重文件（具体配置方法请参考各子项目的说明文档）。

---

## 📚 完整教程（必读）

> **👉 [三角洲行动腾讯管家吸附原理 & 本项目 v3 版本介绍](https://blog.csdn.net/qq_63129682/article/details/161447283)**
> 
> **👉 [手把手教你注册GitHub账号](https://blog.csdn.net/qq_63129682/article/details/161460238)**
> 
> **👉 [从零开始：两种主流方式轻松部署Python开发环境](https://blog.csdn.net/qq_63129682/article/details/161473936?spm=1001.2014.3001.5501)**

**请务必先阅读以上三篇教程**，它们包含了本项目的原理讲解、环境配置、常见问题解决等核心内容。

---

## 📦 项目构成

本仓库包含两个独立的子项目，分别面向 **电脑端（PC）** 和 **手机端（Android）**，均以技术教学与原理验证为目的。

| 子项目 | 主要技术栈 | 适合人群 | 详细文档 |
|--------|-----------|----------|----------|
| **电脑端** | Python, OpenCV, YOLO-omni, OBS, SendInput | Python 初学者、计算机视觉爱好者 | [电脑端 README](https://github.com/ace-trump-tech/deltaforce-pc/blob/main/README.md)|
| **手机端** | Python 下载脚本 + APK | 普通用户、Android 测试者 | [手机端 README](https://github.com/ace-trump-tech/deltaforce-mobile/blob/main/README.md) |

> 💡 **电脑端** 提供从零开始的 Python 编程实战教程（本地代码结构解析），其中 OBS 画面吸附功能正是基于 **YOLOv14** 目标检测框架实现；  
> **手机端** 提供 APK 自动下载脚本。

---

## 🧰 主仓库运行问题？使用独立备用仓库

如果主仓库下载不完整、目录结构不清晰，或者你只想复现某一个端，可以直接使用下面两个独立仓库。它们保留了对应端的代码、README 和运行依赖，适合单独克隆和安装。

### 电脑端：deltaforce-pc

[![进入 deltaforce-pc](https://img.shields.io/badge/PC-deltaforce--pc-3776AB?logo=github&logoColor=white)](https://github.com/ace-trump-tech/deltaforce-pc)

```bash
git clone https://github.com/ace-trump-tech/deltaforce-pc.git
cd deltaforce-pc
python -m venv .venv
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
python gui.py
```

Windows 用户可直接参考 [deltaforce-pc README](https://github.com/ace-trump-tech/deltaforce-pc/blob/main/README.md) 中的 PowerShell 命令。模型权重、Windows 权限和本地配置仍需按该 README 单独准备。

### 手机端：deltaforce-mobile

[![进入 deltaforce-mobile](https://img.shields.io/badge/Mobile-deltaforce--mobile-34A853?logo=github&logoColor=white)](https://github.com/ace-trump-tech/deltaforce-mobile)

```bash
git clone https://github.com/ace-trump-tech/deltaforce-mobile.git
cd deltaforce-mobile
python -m venv .venv
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
python download_apk.py --repo-id <owner>/<repo> --filename <path/to/file.apk>
```

Mobile 仓库不会硬编码未经验证的 APK 地址，运行下载命令时必须填写 Hugging Face 仓库和文件路径。下载完成后，请先检查发布者提供的校验和和签名，再决定是否安装到手机。详细参数见 [deltaforce-mobile README](https://github.com/ace-trump-tech/deltaforce-mobile/blob/main/README.md)。

> **说明**：两个备用仓库提供的是更清晰的独立安装入口，不代表可以绕过系统、游戏或 Android 安全策略；遇到依赖、权限或模型问题，请优先查看对应仓库的“常见问题”。

---


## 🧠 YOLO-omni：跨域实时目标检测框架

**YOLO-omni** 是专为 **非理想成像条件** 设计的实时目标检测框架。与假设标准针孔相机的传统 YOLO 不同，YOLO-omni  通过学习 **域不变、视角鲁棒** 的特征，在游戏角色检测上表现出色。

传统的 YOLO 模型在处理游戏画面时，往往难以将游戏角色准确识别为“人”。YOLO-omni通过 **Game2Real 域适配** 技术，对齐游戏渲染域与真实摄影域的特征分布，使模型在《三角洲行动》、《使命召唤》、《绝地求生》等游戏中，能够稳定地将游戏角色识别为“人”，为画面吸附功能提供了可靠的检测基础。

---

## 🚨 版本更新通知（V5.0.0 / S11 赛季"回声"适配）

- 本项目V4版本代码逻辑在本机测试环境中已针对S10赛季核电站AZ3地图完成初步验证；若因后续游戏更新导致原理验证失效，将在本仓库第一时间同步说明。  
- 近期出现部分仿制或旧版本项目流传，请认准 **ace-trump-tech** 仓库。本项目始终免费开源，**任何收费行为均与项目初衷无关**。  

### ✅ V5.0.0 新特性（2026-09-07）

#### 🗺️ S11 赛季"回声"适配
- **潮汐监狱地图视觉模型**：针对海上多层设施特殊光照条件，新增动态天气识别分支
- **银翼干员识别隔离**：避免将银翼干员特效误判为目标
- **S11 战令外观兼容**：传说级皮肤特征降权，降低模型虚警率
- **ACE 4.0 反检测同步**：S11 同步更新反检测逻辑（动态路径 + 多帧投票）

#### 🎣 自动钓鱼模块（V5.0.0 新增）
- 基于 `core/auto_fish.py`，多地图水域识别
- 视觉中心 + 多帧投票 + 骨骼点定位浮漂
- 配合 SendInput 模拟抛竿 / 收线
- 支持潮汐监狱水域、核电站 AZ3 水库等场景

### ✅ V4.0.0 新特性
- **🗺️ 核电站AZ3地图专项优化**：针对新地图中的“容器防护服”进行非人标注与隔离，彻底解决V3版本将防护服误判为真人目标的问题。
- **🪟 腾讯管家吸附原理验证**（继承自V3）：演示通过模拟腾讯管家窗口置顶与鼠标穿透技术，实现“画面吸附”效果（环境依赖，仅用于研究）。

### ✅ 继承自 V3.0.0 的技术改进
- **动态路径隐藏演示**：动态加密 + 随机目录名，展示规避静态特征扫描的思路。
- **视觉中心模拟头部**：利用手电筒光斑视觉中心作为目标点。
- **强化人物判定模型**：优化 YOLOv14 骨骼点识别，多帧投票降噪。

> ⚠️ **重要声明**：本插件 **不修改任何游戏内存**，仅使用公开的图像识别与模拟输入 API。  
> **🔬 本版本仅供技术学习者对比研究，不建议在任何真实游戏对局中使用。**

---

## 📜 版本更迭简史（技术演进路线）

| 版本 | 主要技术演进 | 学习重点 |
|------|-------------|----------|
| **V1.x** | 基础 YOLO 检测 + OBS 捕获 + 简单鼠标移动 | OpenCV、YOLO推理、模拟输入入门 |
| **V2.x** | 动态路径隐藏、Base64编码、光斑视觉中心算法 | 反静态检测、坐标变换、多帧投票 |
| **V3.x** | 腾讯管家吸附原理验证、兼容性探讨 | 窗口穿透技术、输入模拟边界、环境适配 |
| **V4.x** | **S10赛季专项优化（核电站AZ3）** | **容器防护服隔离、非人目标标注、复杂场景误报抑制** |
| **V5.x** | **S11赛季"回声"适配 + 自动钓鱼模块** | **潮汐监狱视觉模型、银翼识别隔离、ACE 4.0、自动钓鱼主流程** |

> 💡 **为什么不断迭代？** 游戏安全策略会更新，静态方法很快失效。本项目的价值在于展示 **如何根据环境变化调整技术方案**。

---

## 🔥 项目定位

- **电脑端**：基于真实游戏画面的 Python 编程实战项目，涵盖环境配置、图像处理、目标检测、模拟输入、反检测演示等。其中 **OBS 吸附功能正是 YOLOv14 框架的一次具体实践**。  
- **手机端**：提供 APK 文件及自动下载脚本，方便在 Android 设备上测试原理验证效果。

👉 详细代码结构与本地运行说明请分别查看：
- [电脑端 README（本地代码解析）](https://github.com/ace-trump-tech/deltaforce-pc/blob/main/README.md)
- [手机端 README（APK 下载）](https://github.com/ace-trump-tech/deltaforce-mobile/blob/main/README.md)

---

## 📄 许可证

MIT License —— 可自由修改、二次开发，但**严禁用于任何商业作弊软件**。

---

## ⭐ 支持项目

如果你通过本项目学到了技术知识，请给仓库点一个 **Star**。  
你的星星，是对“用技术教学代替作弊工具”这一理念的认同。

---
