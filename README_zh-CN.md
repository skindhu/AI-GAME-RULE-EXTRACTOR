# AI-GAME-RULE-EXTRACTOR: 从游戏视频中提取游戏规则
<img src="https://wechat-account-1251781786.cos.ap-guangzhou.myqcloud.com/ai-game-rule-extractor/game-rule-excutor-font.webp">


[English](README.md) | 中文

## 项目概述

AI-GAME-RULE-EXTRACTOR 是一个基于微软论文[《MM-VID: Advancing Video Understanding with GPT-4V(ision)》](https://arxiv.org/abs/2310.19773)思路开发的创新项目。它旨在通过分析游戏视频自动提取游戏规则，使开发者能够快速复制热门游戏的玩法规则。该项目结合了先进的计算机视觉和自然语言处理技术，为游戏开发者提供了一个强大的工具，以高效地理解和文档化复杂的游戏机制。

## 主要功能

- 场景检测：使用 SceneDetect 库自动识别视频中的关键场景。
- 视频分割：将长视频分割成更小的片段以便于分析。
- 语音识别：使用 WhisperX 从游戏视频中提取语音内容。
- 片段描述生成：利用 GPT-4o-mini 生成每个视频片段的详细描述。
- 规则生成：基于视频分析和背景信息，使用 GPT-4o-mini 生成全面的游戏规则文档。

## 安装

1. 克隆仓库：
   ```
   git clone https://github.com/skindhu/AI-GAME-RULE-EXTRACTOR
   cd AI-GAME-RULE-EXTRACTOR
   ```

2. 安装依赖：
   ```
   pip install -r requirements.txt
   ```

3. 配置 OpenAI API 密钥：
   在 `src/config.py` 文件中设置您的 OpenAI API 密钥。

## 使用方法

运行主脚本以开始分析过程：

```
python main.py
```

## 项目结构

- `main.py`: 主工作流程
- `src/`: 源代码目录
  - `scene_detection.py`: 场景检测模块
  - `video_splitter.py`: 视频分割模块
  - `speech_recognition.py`: 语音识别模块
  - `clip_description.py`: 片段描述生成模块
  - `rule_generator.py`: 规则生成模块
  - `config.py`: 配置文件

## 许可证

本项目采用 MIT 许可证 - 查看 [LICENSE](LICENSE) 文件了解详情。

## 联系方式
<img src="https://wechat-account-1251781786.cos.ap-guangzhou.myqcloud.com/wechat_account.jpeg" width="30%">
