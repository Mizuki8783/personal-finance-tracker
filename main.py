import sys
import os

from datetime import datetime
import pandas as pd

# Import our modules
from data_management import *
from budget_analysis import *
from visualization import *

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
    print("1.  View All Transactions")
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
        print("\nOperation cancelled.")
        return None

def main():
    data = initialize_app()

    income_budget_dict = {  # Alf, you can modify categories here
        "income": 0,
        "food": 0,
        "housing": 0,
        "transportation": 0,
        "utilities": 0,
        "entertainment": 0,
        "other": 0
        }

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
                pass
                # analyze_spending_by_category()
            elif choice == 7:
                pass
                # calculate_average_monthly_spending()
            elif choice == 8:
                pass
                # show_top_spending_category()
            elif choice == 9:
                pass
                # set_monthly_income()
            elif choice == 10:
                pass
                # set_category_budget()
            elif choice == 11:
                pass
                # check_budget_status()
            elif choice == 12:
                pass
                # visualize_spending_trends()
            elif choice == 13:
                filename = input("Enter filename to save (e.g., transactions.csv): ")
                save_transactions(data, filename)
                
            elif choice == 14:
                print("\nExiting the Personal Finance Tracker. Goodbye!")
                break

        except KeyboardInterrupt:
            print("\n\nExiting the Personal Finance Tracker. Goodbye!")
            break
        except Exception as e:
            print(f"An unexpected error occurred: {str(e)}")
            print("Please try again.")

if __name__ == "__main__":
    main()
