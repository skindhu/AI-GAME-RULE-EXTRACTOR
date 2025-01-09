"""
Game rule generation module using GPT-4
"""
import os
import logging
from src.config import client, BACKGROUND_FILE, GAME_RULES_FILE

logger = logging.getLogger(__name__)

def read_background():
    """
    Read game background information from file
    
    Returns:
        str: Background information text
    """
    try:
        with open(BACKGROUND_FILE, 'r', encoding='utf-8') as f:
            return f.read().strip()
    except FileNotFoundError:
        logger.warning(f"{BACKGROUND_FILE} not found. Proceeding without background information.")
        return ""

def generate_rules(clip_descriptions):
    """
    Generate game rules based on clip descriptions and background information
    
    Args:
        clip_descriptions (str): Combined descriptions of all video clips
        
    Returns:
        str: Generated game rules document
    """
    try:
        # Delete existing rules file
        if os.path.exists(GAME_RULES_FILE):
            os.remove(GAME_RULES_FILE)

        # Read background information
        background_info = read_background()
        
        # Build prompt
        prompt = (
            "You are a master game designer tasked with creating the most comprehensive and detailed game documentation possible. "
            "Based on the provided gameplay analysis and background information, create an exhaustive game rule document that "
            "aligns with the game's setting and design philosophy.\n\n"
        )
        
        if background_info:
            prompt += "Game Background Information:\n" + background_info + "\n\n"
        
        prompt += (
            "Create a detailed game rule document covering every aspect of the game:\n\n"
            "1. Core Game Mechanics:\n"
            "   - Detailed explanation of the fundamental gameplay loop\n"
            "   - Complete list of player actions and their effects\n"
            "   - Precise control schemes and input methods\n"
            "   - Timing mechanics and action sequences\n"
            "   - Movement systems and physics interactions\n\n"
            "2. Game Systems:\n"
            "   - Comprehensive scoring mechanism explanation\n"
            "   - Detailed progress tracking systems\n"
            "   - Complete resource management rules\n"
            "   - Experience and leveling systems\n"
            "   - Economy and currency systems\n\n"
            "3. Combat and Interaction:\n"
            "   - Detailed combat mechanics\n"
            "   - Damage calculation systems\n"
            "   - Character or unit interactions\n"
            "   - Status effects and their duration\n"
            "   - Combo systems and special moves\n\n"
            "4. Special Mechanics:\n"
            "   - All power-ups and their effects\n"
            "   - Special abilities and cooldowns\n"
            "   - Unique gameplay elements\n"
            "   - Environmental interactions\n"
            "   - Hidden mechanics and secrets\n\n"
            "5. Game Flow:\n"
            "   - Detailed round/match structure\n"
            "   - Complete win/loss conditions\n"
            "   - Level progression requirements\n"
            "   - Game modes and variations\n"
            "   - Tournament or competitive rules\n\n"
            "6. User Interface:\n"
            "   - Complete HUD element descriptions\n"
            "   - Menu system navigation\n"
            "   - Status indicators and meanings\n"
            "   - Visual and audio feedback systems\n\n"
            "7. Advanced Mechanics:\n"
            "   - Expert-level techniques\n"
            "   - Strategic considerations\n"
            "   - Meta-game elements\n"
            "   - Advanced scoring strategies\n\n"
            "Format this as a professional game design document with clear sections, subsections, and examples.\n"
            "Include specific numbers, timings, and conditions wherever possible.\n"
            "Explain both basic and advanced concepts in detail.\n"
            "Ensure all rules and mechanics align with the provided background information.\n\n"
            "Game Footage Analysis:\n"
        )
        prompt += clip_descriptions
        
        logger.debug("Sending prompt to GPT-4")
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            max_tokens=4000,
        )
        
        result = response.choices[0].message.content
        
        # Save results to file
        with open(GAME_RULES_FILE, 'w', encoding='utf-8') as f:
            f.write(result)
        
        logger.debug("Successfully generated and saved game rules")
        return result
        
    except Exception as e:
        logger.error(f"Error generating game rules: {str(e)}")
        raise
