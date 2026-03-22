# utils.py

import os
import json
import logging
from datetime import datetime

# Create a logger
logger = logging.getLogger(__name__)

def get_current_timestamp():
    """Returns the current timestamp in ISO format."""
    return datetime.now().isoformat()

def get_project_root():
    """Returns the root directory of the project."""
    return os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def load_json(file_path):
    """Loads a JSON file and returns its contents."""
    try:
        with open(file_path, 'r') as file:
            return json.load(file)
    except json.JSONDecodeError as e:
        logger.error(f"Failed to load JSON from {file_path}: {e}")
        return None

def dump_json(data, file_path):
    """Dumps data to a JSON file."""
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)