def generate_budget_insights(monthly_summary, category_totals):
    avg_income = monthly_summary["income"].mean()
    avg_expenses = monthly_summary["expenses"].mean()
    avg_savings = monthly_summary["savings"].mean()

    top_category = category_totals.index[0] if len(category_totals) else "N/A"

    insights = [
        f"Average monthly income: {avg_income:.2f}",
        f"Average monthly expenses: {avg_expenses:.2f}",
        f"Average monthly savings: {avg_savings:.2f}",
        f"Highest spending category: {top_category}",
    ]

    if avg_income > 0:
        savings_rate = (avg_savings / avg_income) * 100
        insights.append(f"Average savings rate: {savings_rate:.1f}%")

        if savings_rate < 20:
            insights.append(
                "Recommendation: review discretionary spending and target a higher savings rate."
            )
        else:
            insights.append(
                "Recommendation: maintain the current savings discipline and review the largest expense category."
            )

    return insights
