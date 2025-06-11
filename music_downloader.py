import os
import requests
from config_manager import ConfigManager

class MusicDownloader:
    def __init__(self, config_file_path):
        self.config_manager = ConfigManager(config_file_path)

    def get_music_file_path(self):
        music_file_path = self.config_manager.get_config("AudioConfig", "music_file_path")
        if os.path.exists(music_file_path):
            return music_file_path
        else:
            print(f"Music file not found at: {music_file_path}. Please ensure the path is correct in config.ini")
            return None



