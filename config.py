# config.py
import os
from google.colab import drive

# Mount Google Drive and setup directories
try:
    drive.mount('/content/drive')
    base_dir = '/content/drive/MyDrive/Civitai_Data'
    DATA_DIRS = {
        'creators': os.path.join(base_dir, 'creators'),
        'models': os.path.join(base_dir, 'models'),
        'csv': os.path.join(base_dir, 'csv'),
        'logs': os.path.join(base_dir, 'logs'),
        'checkpoints': os.path.join(base_dir, 'checkpoints'),
        'images': os.path.join(base_dir, 'images')
    }

    for dir_path in DATA_DIRS.values():
        os.makedirs(dir_path, exist_ok=True)
except Exception as e:
    raise Exception(f"Failed to setup Google Drive and directories: {e}")