"""
Video splitting module for processing video into clips
"""
import os
from moviepy.tools import subprocess_call

def split_video(video_path, scene_list, output_dir):
    """
    Split video into multiple clips based on scene list
    
    Args:
        video_path (str): Path to the input video
        scene_list (list): List of scenes with start and end times
        output_dir (str): Directory to save the output clips
        
    Returns:
        list: List of paths to the created clips
    """
    clip_paths = []
    for i, scene in enumerate(scene_list):
        start, end = scene[0].get_seconds(), scene[1].get_seconds()
        duration = end - start
        clip_path = os.path.join(output_dir, f"clip_{i+1}.mp4")
        try:
            command = [
                'ffmpeg', '-y',
                '-i', video_path,
                '-ss', "%0.2f" % start,
                '-t', "%0.2f" % duration,
                '-map', "0",
                '-vcodec', 'libx264',  # 使用重编码
                '-acodec', 'aac',
                '-avoid_negative_ts', 'make_zero',
                clip_path
            ]
            subprocess_call(command, logger="bar")
            clip_paths.append(clip_path)            
        except Exception as e:
            print(f"Error processing clip {i+1}: {e}")
            continue
            
    return clip_paths
