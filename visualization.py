import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Point 12: Visualize Spending Trends
def plot_income_vs_spending(df, income_budget_dict):
    """
    Generates a line chart comparing monthly income to monthly spending. [cite: 84]
    """
    df['Date'] = pd.to_datetime(df['Date'])
    monthly_expenses = df[df['Type'].str.lower() == 'expense'].set_index('Date')['Amount'].resample('M').sum()
    monthly_income = df[df['Type'].str.lower() == 'income'].set_index('Date')['Amount'].resample('M').sum()

    plt.figure(figsize=(10, 6))
    plt.plot(monthly_income.index, monthly_income.values, marker='o', label='Total Income') 
    plt.plot(monthly_expenses.index, monthly_expenses.values, marker='o', label='Total Spending') 

    plt.title('Monthly Income vs. Spending')
    plt.xlabel('Months') 
    plt.ylabel('Amount')
    plt.legend()
    plt.grid(True)
    plt.show()

def plot_spending_vs_budget(df, income_budget_dict):
    """
    Generates a bar chart comparing actual spending to the budget for each category.
    """
    expenses_df = df[df['Type'].str.lower() == 'expense']
    if expenses_df.empty:
        print("No expense data to visualize.")
        return

    latest_month = expenses_df['Date'].max().to_period('M')
    spending_by_category = expenses_df[expenses_df['Date'].dt.to_period('M') == latest_month].groupby('Category')['Amount'].sum()

    budgets = {k.capitalize(): v for k, v in income_budget_dict.items() if k != 'income' and v > 0}
    categories = list(budgets.keys())
    budget_values = list(budgets.values())
    actual_values = [spending_by_category.get(cat, 0) for cat in categories]

    x = np.arange(len(categories))
    width = 0.35

    fig, ax = plt.subplots(figsize=(12, 7))
    ax.bar(x - width/2, actual_values, width, label='Actual Spending') 
    ax.bar(x + width/2, budget_values, width, label='Budget')

    ax.set_title('Category Spending vs. Budget')
    ax.set_xlabel('Categories') 
    ax.set_ylabel('Amount')
    ax.set_xticks(x)
    ax.set_xticklabels(categories)
    ax.legend()
    fig.tight_layout()
    plt.show() 

def plot_expense_distribution(df):
    """
    Generates a pie chart showing the distribution of expenses by category.
    """
    expenses_df = df[df['Type'].str.lower() == 'expense']
    if expenses_df.empty:
        print("No expense data to visualize.")
        return
        
    latest_month = expenses_df['Date'].max().to_period('M')
    spending_by_category = expenses_df[expenses_df['Date'].dt.to_period('M') == latest_month].groupby('Category')['Amount'].sum()

    if spending_by_category.empty:
        print("No spending in the last month.")
        return

    plt.figure(figsize=(8, 8))
    plt.pie(spending_by_category, labels=spending_by_category.index, autopct='%1.1f%%', startangle=140) 
    plt.title('Expense Distribution for the Current Month')
    plt.axis('equal')
    plt.show() 

def visualize_spending_trends(df, income_budget_dict):
    """
    Provides a sub-menu to choose from different financial visualizations. [cite: 83]
    """
    while True:
        print("\n--- Visualize Spending Trends ---")
        print("1. Line Chart for Monthly Income vs. Spending") 
        print("2. Bar Chart for Category Spending vs. Budget") 
        print("3. Pie Chart for Expense Distribution") 
        print("4. Back to Main Menu")
        
        choice = input("Choose a chart to display (1-4): ")
        
        if choice == '1':
            plot_income_vs_spending(df, income_budget_dict)
        elif choice == '2':
            plot_spending_vs_budget(df, income_budget_dict)
        elif choice == '3':
            plot_expense_distribution(df)
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please select a number from 1 to 4.")