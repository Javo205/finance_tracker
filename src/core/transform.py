from src.models import MoneyMovement
from src.config.config import Config
import pandas as pd

class Transform:
    def __init__(self):
        self.config = Config()
        self.base_data = self.load_base_data()
    
    def load_base_data(self):
        data = pd.read_csv(self.config.movements_file)
        return data
    
    def add_movement(self, date, description, category, income, expense):
        last_row = self.base_data.iloc[-1]
        new_movement = MoneyMovement(last_row, date, description, category, income, expense)
        self.base_data = pd.concat([self.base_data, pd.DataFrame([new_movement.data])], ignore_index=True)
        return new_movement.data