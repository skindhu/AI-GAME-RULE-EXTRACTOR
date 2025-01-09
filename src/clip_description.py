"""
Clip description generation module using GPT-4V
"""
import os
import io
import base64
from PIL import Image
from moviepy import VideoFileClip
from src.config import DEBUG_MODE, DESCRIPTIONS_CACHE_FILE, client

def sample_frames(video, num_frames):
    """Sample frames from video clip"""
    duration = video.duration
    frame_times = [duration * i / (num_frames - 1) for i in range(num_frames)]
    return [video.get_frame(t) for t in frame_times]

def convert_to_base64(image):
    """Convert PIL image to base64 string"""
    buffered = io.BytesIO()
    image.save(buffered, format="JPEG")
    return base64.b64encode(buffered.getvalue()).decode("utf-8")

def generate_clip_descriptions(clip_paths, scenes, num_frames=10):
    """
    Generate descriptions for video clips using GPT-4V
    
    Args:
        clip_paths (list): List of paths to video clips
        scenes (list): List of scenes with timing information
        num_frames (int): Number of frames to sample from each clip
        
    Returns:
        str: Combined descriptions of all clips
    """
    # Check cache first
    if DEBUG_MODE and os.path.exists(DESCRIPTIONS_CACHE_FILE):
        with open(DESCRIPTIONS_CACHE_FILE, 'r', encoding='utf-8') as f:
            return f.read()

    descriptions = []
    for clip_path, scene in zip(clip_paths, scenes):
        clip = VideoFileClip(clip_path)
        frames = sample_frames(clip, num_frames)
        images = [Image.fromarray(frame) for frame in frames]
        image_files = [convert_to_base64(image) for image in images]
        content = []
        prompt = (
            "You are an expert game analyst with extensive experience in documenting detailed game mechanics and rules. "
            "For this sequence of gameplay images, provide an extremely detailed analysis focusing on:\n\n"
            "1. Player Actions and Controls:\n"
            "   - Every possible player interaction\n"
            "   - Specific button combinations or gestures\n"
            "   - Movement mechanics and restrictions\n"
            "   - Action timing and cooldowns\n\n"
            "2. Game Interface Elements:\n"
            "   - All UI components and their functions\n"
            "   - Status indicators and meters\n"
            "   - Menu systems and navigation\n"
            "   - Visual feedback mechanisms\n\n"
            "3. Gameplay Mechanics:\n"
            "   - Detailed interaction systems\n"
            "   - Combat or competition mechanics\n"
            "   - Resource management systems\n"
            "   - Power-ups and special abilities\n\n"
            "4. Scoring and Progress:\n"
            "   - Point calculation methods\n"
            "   - Achievement conditions\n"
            "   - Level progression criteria\n"
            "   - Ranking or rating systems\n\n"
            "5. Environmental Interactions:\n"
            "   - Object interactions\n"
            "   - Terrain effects\n"
            "   - Environmental hazards\n"
            "   - Interactive elements\n\n"
            "Describe every detail you observe, no matter how minor it might seem.\n"
            f"Time range: {scene}"
        )

        content.append({"type": "text", "text": prompt})
        for image_file in image_files:
            content.append({
                "type": "image_url",
                "image_url": {"url": f"data:image/jpeg;base64,{image_file}"},
            })

        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {
                    "role": "user",
                    "content": content
                }
            ],
            max_tokens=2000,
        )
        descriptions.append(response.choices[0].message.content)
        
    result = "".join(descriptions)
    if DEBUG_MODE:
        with open(DESCRIPTIONS_CACHE_FILE, 'w', encoding='utf-8') as f:
            f.write(result)
    return result
