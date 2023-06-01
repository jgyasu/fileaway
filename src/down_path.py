import os
from pathlib import Path


def down_path():
    try:
        path = str(Path.home() / 'Downloads')
        if os.path.exists(path):
            return path
        else:
            return False
    except:
        return False