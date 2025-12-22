import pandas as pd
class MoneyMovement:
    def __init__(self, row, date, description, category, income, expense):
        self.data = self.define_movement(row, date, description, category, income, expense)

        def define_movement(self, row, date, description, category, income, expense):
            month = self.return_month(date)
            relative_balance = float(income) - float(expense)
            absolute_balance = relative_balance + row["balance"]
            id = row["id"] + 1
            return pd.Series({
                "id": id,
                "date": date,
                "month": month,
                "description": description,
                "category": category,
                "income": float(income),
                "expense": float(expense),
                "balance": absolute_balance
            })

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
            