import json
import os

class Config:
    # Configuration settings for the finance tracker application
    def __init__(self):
        # repository root is two levels up from src/config (repo/src/config -> repo)
        repo_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        self.project_root = repo_root
        self.src_dir = os.path.join(self.project_root, 'src')
        self.config_dir = os.path.dirname(os.path.abspath(__file__))
        self.data_dir = os.path.join(self.project_root, 'data')

        self.config_dict = self.get_config_dict()

        self.categories_file = os.path.join(self.data_dir, self.config_dict["categories_file_name"])
        self.movements_file = os.path.join(self.data_dir, self.config_dict["data_file_name"])

    def get_config_dict(self):
        dict_config_path = os.path.join(self.config_dir, 'config.json')
        with open(dict_config_path, 'r', encoding='utf-8') as f:
            return json.load(f)
