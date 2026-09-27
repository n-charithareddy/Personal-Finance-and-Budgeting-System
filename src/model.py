import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, r2_score

def train_expense_model(monthly_summary):
    X = np.arange(1, len(monthly_summary) + 1).reshape(-1, 1)
    y = monthly_summary["expenses"].values

    model = LinearRegression()
    model.fit(X, y)

    predictions = model.predict(X)

    metrics = {
        "mae": mean_absolute_error(y, predictions),
        "r2": r2_score(y, predictions),
    }

    return model, metrics

def forecast_expenses(model, number_of_months, existing_months):
    future_X = np.arange(
        existing_months + 1,
        existing_months + number_of_months + 1
    ).reshape(-1, 1)

    return model.predict(future_X)
