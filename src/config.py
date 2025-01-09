"""
Configuration settings for the MM-VID project
"""
import os
from openai import OpenAI

# Debug mode configuration
DEBUG_MODE = True

# File paths
DESCRIPTIONS_CACHE_FILE = "descriptions_cache.txt"
GAME_RULES_FILE = "game_rule.txt"
BACKGROUND_FILE = "background.txt"

# OpenAI configuration
client = OpenAI(api_key="")
