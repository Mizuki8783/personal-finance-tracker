import sys
import os

from datetime import datetime
import pandas as pd

# Import our modules
from data_management import *
from budget_analysis import *
from visualization import *
from spending_analysis import *

import warnings
warnings.filterwarnings('ignore', category=FutureWarning)

pd.set_option('display.max_columns', None)

def initialize_app():
    while True:
        data_file_path = input("Enter the path to your CSV file: ")

        # Check if the file exists
        if not os.path.exists(data_file_path):
            print(f"Error: File '{data_file_path}' not found. Please provide a valid file path.")
            continue

        # Check if it's actually a file (not a directory)
        if not os.path.isfile(data_file_path):
            print(f"Error: '{data_file_path}' is not a valid file. Please provide a valid file path.")
            continue

        data = pd.read_csv(data_file_path)
        if data.empty:
            print("Error: The file is empty. Please provide a valid file path.")
            continue

        return data

def display_menu():
    """Display the main menu"""
    print("\n" + "="*40)
    print("    Personal Finance Tracker")
    print("="*40)
    print("1.  View Transactions")
    print("2.  View Transactions by Date Range")
    print("3.  Add a Transaction")
    print("4.  Edit a Transaction")
    print("5.  Delete a Transaction")
    print("6.  Analyze Spending by Category")
    print("7.  Calculate Average Monthly Spending")
    print("8.  Show Top Spending Category")
    print("9.  Set Monthly Income")
    print("10. Set Category Budget")
    print("11. Check Budget Status")
    print("12. Visualize Spending Trends")
    print("13. Save Transactions to CSV")
    print("14. Exit")
    print("="*40)



def get_user_choice():
    """Get and validate user menu choice"""
    try:
        choice = input("\nChoose an option (1-14): ").strip()
        if not choice:
            return None

        choice_num = int(choice)
        if 1 <= choice_num <= 14:
            return choice_num
        else:
            print("Please enter a number between 1 and 14.")
            return None

    except ValueError:
        print("Please enter a valid number.")
        return None

    except KeyboardInterrupt:
        print("\n\nExiting the Personal Finance Tracker. Goodbye!")
        sys.exit(0)

def main():
    data = initialize_app()

    income_budget_dict = {
        "Income": 0,
    }

    for category in data['Category'].unique():
        income_budget_dict[category] = 0


    while True:
        try:
            display_menu()
            choice = get_user_choice()

            if choice is None:
                continue
            elif choice == 1:
                 view_all_transactions(data)

            elif choice == 2:
                start_date = input("Enter start date (YYYY-MM-DD): ")
                end_date = input("Enter end date (YYYY-MM-DD): ")
                view_transactions_by_date(data, start_date, end_date)

            elif choice == 3:
                date = input("Enter date (YYYY-MM-DD): ")
                category = input("Enter category: ")
                description = input("Enter description: ")
                amount = input("Enter amount: ")
                data = add_transaction(data, date, category, description, amount)

            elif choice == 4:
                index = input("Enter the index of the transaction to edit: ")
                data = edit_transaction(data, index)

            elif choice == 5:
                index = input("Enter the index of the transaction to delete: ")
                data = delete_transaction(data, index)

            elif choice == 6:
                analyze_spending_by_category(data)

            elif choice == 7:
                calculate_average_monthly_spending(data)

            elif choice == 8:
                show_top_spending_category(data)

            elif choice == 9:
                income_budget_dict = set_monthly_income(income_budget_dict)

            elif choice == 10:
                income_budget_dict = set_category_budget(income_budget_dict)

            elif choice == 11:
                # Check if budgets have been set before checking status
                if sum(v for k, v in income_budget_dict.items() if k != 'income') == 0:
                    print("\nNo budgets set. Please set a budget first using option 10.")
                else:
                    check_budget_status(data, income_budget_dict)

            elif choice == 12:
                visualize_spending_trends(data, income_budget_dict)

            elif choice == 13:
                filename = input("Enter filename to save (e.g., transactions.csv): ")
                save_transactions(data, filename)

            elif choice == 14:
                print("\nExiting the Personal Finance Tracker. Goodbye!")
                break

        except Exception as e:
            print(f"An unexpected error occurred: {str(e)}")
            print("Please try again.")

if __name__ == "__main__":
    main()
