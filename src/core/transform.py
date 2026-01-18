from src.models import MoneyMovement
from src.config import Config
import pandas as pd

class Transform:
    def __init__(self):
        self.config = Config()
        self.base_data = self.load_base_data()
    
    def load_base_data(self):
        # TODO: Specify header
        data = pd.read_csv(self.config.movements_file)
        return data
    
    def add_movement(self, date, description, category, income, expense):
        base_data = self.base_data
        new_movement = MoneyMovement(base_data, date, description, category, income, expense)
        self.base_data = pd.concat([self.base_data, pd.DataFrame([new_movement.data])], ignore_index=True)
        return new_movement.data
