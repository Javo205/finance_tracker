import pandas as pd


def get_totals(df: pd.DataFrame) -> float:
    """From a financial df, compute the totals"""
    income = df["income"]
    expense = df["expense"]
    total = income.sum() - expense.sum()
    return total

def get_totals_months(df: pd.DataFrame) -> pd.DataFrame:
    """From a financial df, compute the totals of a certain month"""

    df_grouped_month = df.loc[:, ["month", "income", "expense"]].groupby("month").sum()
    df_grouped_month["total"] = df_grouped_month["income"] - df_grouped_month["expense"]
    return df_grouped_month

def get_totals_category(df: pd.DataFrame, category: str) -> float:
    """From a financial df, compute the totals of a certain category"""
    df_category = df.loc[df["category"] == category]
    total_category = get_totals(df_category)
    return total_category

def get_totals_column(df: pd.DataFrame, column: str) -> pd.DataFrame:
    """From a financial df, compute the totals of a certain column"""
    df_grouped_column = df.loc[:, [column, "income", "expense"]].groupby(column).sum()
    df_grouped_column["total"] = df_grouped_column["income"] - df_grouped_column["expense"]
    return df_grouped_column
