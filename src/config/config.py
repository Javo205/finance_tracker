import json
import os

class Config:
    # Configuration settings for the finance tracker application
    def __init__(self):
        self.main_dir = os.path.dirname(os.path.abspath(__file__))
        self.data_dir = os.path.join(self.main_dir, 'data')
        self.src_dir = os.path.join(self.main_dir, 'src')
        self.config_dir = os.path.join(self.src_dir, 'config')

        self.config_dict = self.get_config_dict()

        self.categories_file = os.path.join(self.config_dir, self.config_dict["categories_file_name"])
        self.movements_file = os.path.join(self.data_dir, self.config_dict["data_file_name"])

    def get_config_dict(self):
        dict_config_path = os.path.join(self.config_dir, 'config.json')
        with open(dict_config_path, 'r', encoding='utf-8') as f:
            return json.load(f)
