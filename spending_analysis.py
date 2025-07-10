import pandas as pd
from datetime import datetime

def analyze_spending_by_category(df):
    """Analyze total spending by category"""

    try:
        if df.empty:
            print("No transactions found.")
            return

        # Filter only expense transactions
        expense_df = df[df['Type'] == 'Expense']

        if expense_df.empty:
            print("No expense transactions found.")
            return

        # Group by category and sum amounts
        category_spending = expense_df.groupby('Category')['Amount'].sum().sort_values(ascending=False)

        # Display the output
        print("\n--- Total Spending by Category ---")
        print(f"{'Category':<20} {'Amount':<10}")
        print("-" * 30)
        for category, amount in category_spending.items():
            print(f"{category:<20} ${amount:.2f}")

    except Exception as e:
        print(f"Error analyzing spending by category: {str(e)}")

def calculate_average_monthly_spending(df):
    """Calculate average monthly spending"""
    try:
        if df.empty:
            print("No transactions found.")
            return

        # Filter only expense transactions
        expense_df = df[df['Type'] == 'Expense']

        if expense_df.empty:
            print("No expense transactions found.")
            return

        # Extract year-month from dates
        expense_df = expense_df.copy()
        expense_df['Month'] = expense_df['Date'].astype("datetime64[ns]").dt.to_period('M')

        # Calculate monthly totals
        monthly_average_spending = expense_df.groupby('Month')['Amount'].mean()

        print("\n--- Average Monthly Spending ---")
        print(f"{'Month':<20} {'Amount':<10}")
        print("-" * 30)
        for month, amount in monthly_average_spending.items():
            print(f"{str(month):<20} ${amount:.2f}")

    except Exception as e:
        print(f"Error calculating average monthly spending: {str(e)}")

def show_top_spending_category(df):
    """Show the category with highest total spending"""
    try:
        if df.empty:
            print("No transactions found.")
            return

        # Filter only expense transactions
        expense_df = df[df['Type'] == 'Expense']

        if expense_df.empty:
            print("No expense transactions found.")
            return

        # Group by category and sum amounts
        category_spending = expense_df.groupby('Category')['Amount'].sum().sort_values(ascending=False)

        # Get top category
        top_category = category_spending.index[0]
        top_amount = category_spending.iloc[0]

        print("\n--- Top Spending Category ---")
        print(f"{'Category':<20} {'Amount':<10}")
        print("-" * 30)
        print(f"{top_category:<20} ${top_amount:.2f}")

    except Exception as e:
        print(f"Error finding top spending category: {str(e)}")
