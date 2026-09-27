from pathlib import Path

from src.data_processing import load_data, create_monthly_summary, category_summary
from src.analysis import generate_budget_insights
from src.model import train_expense_model, forecast_expenses
from src.visualizations import (
    plot_monthly_finances,
    plot_category_spending,
    plot_expense_forecast,
)

BASE_DIR = Path(__file__).resolve().parent
DATA_PATH = BASE_DIR / "data" / "transactions.csv"
OUTPUT_DIR = BASE_DIR / "outputs"

OUTPUT_DIR.mkdir(exist_ok=True)

def main():
    df = load_data(DATA_PATH)

    monthly_summary = create_monthly_summary(df)
    category_totals = category_summary(df)

    print("\n=== PERSONAL FINANCE SUMMARY ===")
    print(monthly_summary.to_string(index=False))

    print("\n=== BUDGET INSIGHTS ===")
    for insight in generate_budget_insights(monthly_summary, category_totals):
        print("-", insight)

    model, metrics = train_expense_model(monthly_summary)

    print("\n=== LINEAR REGRESSION MODEL ===")
    print(f"MAE: {metrics['mae']:.2f}")
    print(f"R² Score: {metrics['r2']:.3f}")

    forecast = forecast_expenses(
        model,
        number_of_months=3,
        existing_months=len(monthly_summary),
    )

    print("\n=== NEXT 3-MONTH EXPENSE FORECAST ===")
    for i, value in enumerate(forecast, start=1):
        print(f"Month +{i}: {value:.2f}")

    plot_monthly_finances(
        monthly_summary,
        OUTPUT_DIR / "monthly_finances.png",
    )
    plot_category_spending(
        category_totals,
        OUTPUT_DIR / "category_spending.png",
    )
    plot_expense_forecast(
        monthly_summary,
        forecast,
        OUTPUT_DIR / "expense_forecast.png",
    )

    print("\nCharts saved to the outputs/ directory.")

if __name__ == "__main__":
    main()
