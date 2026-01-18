import pandas as pd
class MoneyMovement:
    def __init__(self, base_data, date, description, category, income, expense):

        if not base_data.empty:
            row = base_data.iloc[-1]
            self.data = self.define_movement(row, date, description, category, income, expense)
        else:
            self.data = self.define_first_movement(date, description, category, income, expense)
        self.data["date"] = self.data["date"].to_datetime()


    def define_movement(self, row, date, description, category, income, expense):
        month = self.return_month(date)
        income, expense = self.check_none(income, expense)
        relative_balance = float(income) - float(expense)
        absolute_balance = relative_balance + row["balance"]
        row_id = row["id"] + 1
        return pd.Series({
            "id": row_id,
            "date": date,
            "month": month,
            "description": description,
            "category": category,
            "income": float(income),
            "expense": float(expense),
            "balance": absolute_balance
        })


    def define_first_movement(self, date, description, category, income, expense):
        month = self.return_month(date)
        income, expense = self.check_none(income, expense)
        relative_balance = float(income) - float(expense)
        row_id = 1
        return pd.Series({
            "id": row_id,
            "date": date,
            "month": month,
            "description": description,
            "category": category,
            "income": float(income),
            "expense": float(expense),
            "balance": relative_balance
        })

    @staticmethod
    def return_month(date):
        month = date.split("/")[1]
        dict_month = {
            "01": "enero",
            "02": "febrero",
            "03": "marzo",
            "04": "abril",
            "05": "mayo",
            "06": "junio",
            "07": "julio",
            "08": "agosto",
            "09": "septiembre",
            "10": "octubre",
            "11": "noviembre",
            "12": "diciembre"
        }
        return dict_month[month]

    @staticmethod
    def check_none(income, expense):
        if income is None:
            income = 0
        if expense is None:
            expense = 0
        return income, expense
        