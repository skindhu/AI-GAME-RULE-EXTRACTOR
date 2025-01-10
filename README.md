# AI-GAME-RULE-EXTRACTOR: Extracting Game Rules from Gameplay Videos
<img src="https://wechat-account-1251781786.cos.ap-guangzhou.myqcloud.com/ai-game-rule-extractor/game-rule-excutor-font.webp">


English | [中文](README_zh-CN.md)

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

Follow the author's WeChat Official Account to learn more about AI exploration:

<img src="https://wechat-account-1251781786.cos.ap-guangzhou.myqcloud.com/wechat_account.jpeg" width="30%">
