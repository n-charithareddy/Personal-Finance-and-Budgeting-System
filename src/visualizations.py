import matplotlib.pyplot as plt

def plot_monthly_finances(summary, output_path):
    plt.figure(figsize=(10, 6))
    plt.plot(summary["month"], summary["income"], marker="o", label="Income")
    plt.plot(summary["month"], summary["expenses"], marker="o", label="Expenses")
    plt.plot(summary["month"], summary["savings"], marker="o", label="Savings")
    plt.title("Monthly Income, Expenses and Savings")
    plt.xlabel("Month")
    plt.ylabel("Amount")
    plt.xticks(rotation=45)
    plt.legend()
    plt.tight_layout()
    plt.savefig(output_path)
    plt.close()

def plot_category_spending(category_totals, output_path):
    plt.figure(figsize=(8, 5))
    category_totals.sort_values().plot(kind="barh")
    plt.title("Spending by Category")
    plt.xlabel("Amount")
    plt.ylabel("Category")
    plt.tight_layout()
    plt.savefig(output_path)
    plt.close()

def plot_expense_forecast(summary, forecast, output_path):
    historical_x = list(range(1, len(summary) + 1))
    future_x = list(range(len(summary) + 1, len(summary) + len(forecast) + 1))

    plt.figure(figsize=(10, 6))
    plt.plot(historical_x, summary["expenses"], marker="o", label="Historical Expenses")
    plt.plot(future_x, forecast, marker="o", linestyle="--", label="Forecast")
    plt.title("Expense Forecast using Linear Regression")
    plt.xlabel("Month Index")
    plt.ylabel("Expenses")
    plt.legend()
    plt.tight_layout()
    plt.savefig(output_path)
    plt.close()
