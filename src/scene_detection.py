"""
Scene detection module for video processing
"""
import scenedetect
from scenedetect import VideoManager, SceneManager
from scenedetect.detectors import ContentDetector

def detect_scenes(video_path):
    """
    Detect scene changes in the video
    
    Args:
        video_path (str): Path to the video file
        
    Returns:
        list: List of scenes with start and end times
    """
    video_manager = VideoManager([video_path])
    scene_manager = SceneManager()
    scene_manager.add_detector(ContentDetector())

    video_manager.start()
    scene_manager.detect_scenes(frame_source=video_manager)
    scenes = scene_manager.get_scene_list()
    
    return scenes
