"""
Speech recognition module using WhisperX
"""
import logging
import whisperx

logger = logging.getLogger(__name__)

def recognize_speech(video_path):
    """
    Perform speech recognition on video using WhisperX
    
    Args:
        video_path (str): Path to the video file
        
    Returns:
        str: Transcribed text from the video
        
    Raises:
        Exception: If speech recognition fails
    """
    try:
        logger.debug(f"Loading WhisperX model for {video_path}")
        model = whisperx.load_model("large", device='cpu', compute_type="float32")
        
        logger.debug("Starting transcription")
        result = model.transcribe(video_path)
        
        logger.debug("Processing segments")
        segments = result["segments"]
        
        # 合并所有文本片段，保留时间戳信息
        transcription = []
        for segment in segments:
            time_start = segment.get("start", 0)
            time_end = segment.get("end", 0)
            text = segment.get("text", "").strip()
            if text:
                transcription.append(f"[{time_start:.2f}-{time_end:.2f}] {text}")
        
        text = "\n".join(transcription)
        logger.debug(f"Transcription completed, generated {len(transcription)} segments")
        
        return text
        
    except Exception as e:
        logger.error(f"Error during speech recognition: {str(e)}")
        logger.debug("Returning empty transcription due to error")
        return "No transcription available."
