# AI-GAME-RULE-EXTRACTOR: Extracting Game Rules from Gameplay Videos

<div align="center">
  <a href="#zh">中文</a> | <a href="#en">English</a>
</div>

---

<h2 id="zh">中文文档</h2>

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
![](https://camo.githubusercontent.com/4e8d0a24493470f410be0c2f516264003152dd8793e36635c41c48ca58b4f1c2/68747470733a2f2f7765636861742d6163636f756e742d313235313738313738362e636f732e61702d6775616e677a686f752e6d7971636c6f75642e636f6d2f7765636861745f6163636f756e742e6a706567)

---

<h2 id="en">English Documentation</h2>

## Project Overview

AI-GAME-RULE-EXTRACTOR is an innovative project developed based on Microsoft's paper [《MM-VID: Advancing Video Understanding with GPT-4V(ision)》](https://arxiv.org/abs/2310.19773). It aims to automatically extract game rules from gameplay videos, enabling developers to quickly replicate the gameplay mechanics of popular games. This project combines advanced computer vision and natural language processing technologies to provide game developers with a powerful tool for efficiently understanding and documenting complex game mechanics.

## Key Features

- Scene Detection: Automatically identify key scenes in videos using the SceneDetect library.
- Video Splitting: Divide long videos into smaller segments for analysis.
- Speech Recognition: Extract voice content from game videos using WhisperX.
- Clip Description Generation: Generate detailed descriptions for each video segment using GPT-4o-mini.
- Rule Generation: Create comprehensive game rule documentation based on video analysis and background information using GPT-4o-mini.

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/skindhu/AI-GAME-RULE-EXTRACTOR
   cd AI-GAME-RULE-EXTRACTOR
   ```

2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Configure OpenAI API key:
   Set your OpenAI API key in the `src/config.py` file.

## Usage

Run the main script to start the analysis process:

```
python main.py
```

## Project Structure

- `main.py`: Main workflow
- `src/`: Source code directory
  - `scene_detection.py`: Scene detection module
  - `video_splitter.py`: Video splitting module
  - `speech_recognition.py`: Speech recognition module
  - `clip_description.py`: Clip description generation module
  - `rule_generator.py`: Rule generation module
  - `config.py`: Configuration file

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact
![](https://camo.githubusercontent.com/4e8d0a24493470f410be0c2f516264003152dd8793e36635c41c48ca58b4f1c2/68747470733a2f2f7765636861742d6163636f756e742d313235313738313738362e636f732e61702d6775616e677a686f752e6d7971636c6f75642e636f6d2f7765636861745f6163636f756e742e6a706567)
