# backend/__init__.py

"""
Backend package for the Verse Code Generation Agent.

This package handles the agentic workflow for generating, correcting,
and validating Verse code.
"""

import os
import logging
from dotenv import load_dotenv
from pathlib import Path

# --- Setup Logging ---
logger = logging.getLogger(__name__)

# --- Load Environment Variables ---
# This looks for a .env file in the root directory of your project
env_path = Path(__file__).parent.parent / '.env'
if env_path.exists():
    logger.info(f"Loading environment variables from {env_path}")
    load_dotenv(dotenv_path=env_path)
else:
    logger.warning(f".env file not found at {env_path}. Using system environment variables.")

# --- Check for Critical Environment Variables ---
# This provides a helpful warning at startup if the key is missing.
if not os.getenv("GOOGLE_API_KEY"):
    logger.warning("CRITICAL: GOOGLE_API_KEY environment variable is not set.")

# --- Define the Public API for this Package ---

# Import the main agent class from your graph module
from .graph import CodeGenerationAgent

# This line controls what is imported with 'from backend import *'
# It makes your package cleaner to use.
__all__ = ["CodeGenerationAgent"]