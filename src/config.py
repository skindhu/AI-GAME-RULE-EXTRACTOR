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
client = OpenAI(api_key="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")
