# Personal Finance and Budgeting System (Machine Learning)

A Python-based personal finance analysis tool that uses income and expense data to generate budgeting insights, forecast expenses with Linear Regression, and visualize financial trends.

## Features
- Load and validate income/expense transaction data
- Preprocess financial data using Pandas and NumPy
- Engineer monthly and category-level features
- Analyze income, expenses, savings, and spending categories
- Forecast future monthly expenses using Linear Regression
- Generate basic savings recommendations from spending patterns
- Visualize income, expenses, savings, and forecasts with Matplotlib

## Tech Stack
Python, Pandas, NumPy, scikit-learn, Matplotlib

## Project Structure
```text
Personal-Finance-and-Budgeting-System/
├── data/
│   └── transactions.csv
├── outputs/
├── src/
│   ├── data_processing.py
│   ├── analysis.py
│   ├── model.py
│   └── visualizations.py
├── main.py
├── requirements.txt
└── README.md
```

## Run
```bash
pip install -r requirements.txt
python main.py
```

The generated charts are saved in `outputs/`.
