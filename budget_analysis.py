import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Point 9: Set Monthly Income
def set_monthly_income(income_budget_dict):
    """
    Prompts the user to enter their total monthly income and updates the dictionary.
    This corresponds to feature 9 in the project description.
    """
    try:
        income = float(input("Enter your total monthly income: "))
        if income < 0:
            print("Income must be a positive number.")
            return income_budget_dict
        
        income_budget_dict['income'] = income
        print(f"Your monthly income is set to: ${income:,.2f}") 
    except ValueError:
        print("Invalid input. Please enter a valid number.")
    
    return income_budget_dict

# Point 10: Set Category Budget
def set_category_budget(income_budget_dict):
    """
    Allows the user to set a budget for each expense category.
    This corresponds to feature 10 in the project description. 
    """
    print("\n--- Set Category Budgets ---")
    # Iterate over all keys in the dictionary except for 'income'
    for category in income_budget_dict:
        if category == 'income':
            continue
        try:
            # Prompt user for the budget of each category 
            budget_input = input(f"Enter your budget for {category.capitalize()}: ")
            budget = float(budget_input)
            
            if budget < 0:
                print("Budget must be a positive number. Setting to 0.")
                income_budget_dict[category] = 0
            else:
                income_budget_dict[category] = budget
        except ValueError:
            print("Invalid input. Setting budget for this category to 0.")
            income_budget_dict[category] = 0
            
    print("\nYour budgets have been set:") 
    for category, budget in income_budget_dict.items():
        if category != 'income' and budget > 0:
            print(f"- {category.capitalize()}: ${budget:,.2f}") 
            
    return income_budget_dict

# Point 11: Check Budget Status
def check_budget_status(df, income_budget_dict):
    """
    Compares actual spending against the set budget for the most recent month.
    It provides alerts and suggestions based on spending patterns. 
    """
    print("\n--- Budget Status ---") 
    
    # Ensure 'Date' column is in datetime format
    df['Date'] = pd.to_datetime(df['Date'])
    expenses_df = df[df['Type'].str.lower() == 'expense'].copy()
    
    if expenses_df.empty:
        print("No expense transactions found.")
        return

    # Calculate spending per category for the most recent month
    latest_month = expenses_df['Date'].max().to_period('M')
    monthly_expenses = expenses_df[expenses_df['Date'].dt.to_period('M') == latest_month]
    spending_by_category = monthly_expenses.groupby('Category')['Amount'].sum()

    suggestions = []
    all_good = True

    # Compare spending with budget for each category
    for category, budget in income_budget_dict.items():
        if category == 'income' or budget <= 0:
            continue

        actual = spending_by_category.get(category.capitalize(), 0)
        status_msg = f"{category.capitalize()}: ${actual:,.2f} / ${budget:,.2f}"
        
        # Check if spending exceeds budget 
        if actual > budget:
            status_msg += " (Alert: Exceeded budget!)"
            suggestions.append(f"- Consider reducing {category} spending or adjusting the budget.") # [cite: 13, 68]
            all_good = False
        # Check if spending is close to the budget (within 10%) 
        elif actual >= budget * 0.9:
            status_msg += " (Warning: Close to budget!)"
            suggestions.append(f"- Monitor {category} spending closely to avoid exceeding the budget.") # [cite: 80]
            all_good = False
        
        print(status_msg)

    print("\nSuggestions:")
    if suggestions:
        for s in suggestions:
            print(s)
    if all_good:
        print("- You are within budget for other categories. Keep up the good work!") 

