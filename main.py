"""
Main workflow for MM-VID project: Extracting game rules from gameplay videos
"""
import os
import logging
from src.scene_detection import detect_scenes
from src.video_splitter import split_video
from src.speech_recognition import recognize_speech
from src.clip_description import generate_clip_descriptions
from src.rule_generator import generate_rules
from src.config import DEBUG_MODE, DESCRIPTIONS_CACHE_FILE, GAME_RULES_FILE, BACKGROUND_FILE

# Configure logging
logging.basicConfig(
    level=logging.DEBUG if DEBUG_MODE else logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

def process_video(video_path, output_dir):
    """
    Process video to generate game rules
    
    Args:
        video_path (str): Path to the input video
        output_dir (str): Directory to save intermediate and final outputs
        
    Returns:
        str: Generated game rules
        
    Raises:
        FileNotFoundError: If video file doesn't exist
        Exception: For other processing errors
    """
    try:
        # Validate input
        if not os.path.exists(video_path):
            raise FileNotFoundError(f"Video file not found: {video_path}")
            
        # Create output directory
        os.makedirs(output_dir, exist_ok=True)
        
        # Step 1: Scene Detection
        logger.info("Step 1: Detecting scenes...")
        scenes = detect_scenes(video_path)
        logger.info(f"Detected {len(scenes)} scenes")

        # Step 2: Split Video into Multiple Clips
        logger.info("Step 2: Splitting video into clips...")
        clip_paths = split_video(video_path, scenes, output_dir)
        logger.info(f"Created {len(clip_paths)} video clips")

        # Step 3: Speech Recognition
        logger.info("Step 3: Performing speech recognition...")
        transcript = recognize_speech(video_path)
        logger.info("Speech recognition completed")

        # Step 4: Generate Clip Descriptions
        logger.info("Step 4: Generating clip descriptions...")
        if DEBUG_MODE and os.path.exists(DESCRIPTIONS_CACHE_FILE):
            with open(DESCRIPTIONS_CACHE_FILE, 'r', encoding='utf-8') as f:
                clip_descriptions = f.read()
        else:
            clip_descriptions = generate_clip_descriptions(clip_paths, scenes, 10)
            if DEBUG_MODE:
                with open(DESCRIPTIONS_CACHE_FILE, 'w', encoding='utf-8') as f:
                    f.write(clip_descriptions)
        logger.info("Clip descriptions generated")

        # Step 5: Generate Game Rules
        logger.info("Step 5: Generating game rules...")
        clip_descriptions = clip_descriptions + f'\n\n ASR Transcript:\n{transcript}'
        rules = generate_rules(clip_descriptions)
        logger.info("Game rules generated successfully")
        
        # 将结果保存到文件
        with open(GAME_RULES_FILE, 'w', encoding='utf-8') as f:
            f.write(rules)
        
        return rules
        
    except Exception as e:
        logger.error(f"Error during video processing: {str(e)}", exc_info=DEBUG_MODE)
        raise

def read_background():
    """读取游戏背景信息文件"""
    try:
        with open(BACKGROUND_FILE, 'r', encoding='utf-8') as f:
            return f.read().strip()
    except FileNotFoundError:
        print(f"Warning: {BACKGROUND_FILE} not found. Proceeding without background information.")
        return ""

def main():
    """Main entry point of the program"""
    video_path = "game.mov"
    output_dir = "clips"
    
    try:
        rules = process_video(video_path, output_dir)
        logger.info("Process completed successfully!")
        logger.info("Check game_rule.txt for the generated rules.")
        
        if DEBUG_MODE:
            logger.debug("Generated rules preview:")
            logger.debug("-" * 50)
            logger.debug(rules[:500] + "..." if len(rules) > 500 else rules)
            logger.debug("-" * 50)
            
    except Exception as e:
        logger.error(f"Failed to process video: {str(e)}")
        return 1
    
    return 0

if __name__ == "__main__":
    exit(main())
