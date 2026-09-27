import pandas as pd
import numpy as np

def load_data(path):
    df = pd.read_csv(path)
    df["date"] = pd.to_datetime(df["date"])
    df["amount"] = pd.to_numeric(df["amount"], errors="coerce")
    df = df.dropna(subset=["date", "amount", "type", "category"])
    df["month"] = df["date"].dt.to_period("M").astype(str)
    return df

def create_monthly_summary(df):
    income = (
        df[df["type"] == "Income"]
        .groupby("month")["amount"]
        .sum()
        .rename("income")
    )
    expenses = (
        df[df["type"] == "Expense"]
        .groupby("month")["amount"]
        .sum()
        .rename("expenses")
    )

    summary = pd.concat([income, expenses], axis=1).fillna(0)
    summary["savings"] = summary["income"] - summary["expenses"]
    summary["savings_rate"] = np.where(
        summary["income"] > 0,
        (summary["savings"] / summary["income"]) * 100,
        0,
    )
    return summary.reset_index()

def category_summary(df):
    expenses = df[df["type"] == "Expense"]
    return (
        expenses.groupby("category")["amount"]
        .sum()
        .sort_values(ascending=False)
    )
