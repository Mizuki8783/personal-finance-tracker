import pandas as pd
from datetime import datetime
import warnings
warnings.filterwarnings('ignore', category=FutureWarning)

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

        expense_df = df[df['Type'] == 'Expense'].copy()

        expense_df['Month'] = expense_df['Date'].astype("datetime64[ns]").dt.to_period('M')
        monthly_total_spending = expense_df.groupby('Month').agg({'Amount': 'sum'})

        monthly_average_spending = monthly_total_spending.resample('Y').mean().reset_index().rename(columns={'Month': 'Year'})

        print("\n--- Average Monthly Spending ---")
        print(f"{'Year':<10} {'Amount':<10}")
        print("-" * 20)
        for _, row in monthly_average_spending.iterrows():
            print(f"{str(row['Year']):<10} ${row['Amount']:.2f}")

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
