import pandas as pd

# 1. View All Transactions
def view_all_transactions(df):
    if df.empty:
        print("No transactions available.")
    else:
        df_display = df.copy()
        df_display['Date'] = pd.to_datetime(df_display['Date']).dt.strftime('%Y-%m-%d')
        print("\n--- All Transactions ---")
        print(df_display.reset_index(drop=True))

# 2. View Transactions by Date Range
def view_transactions_by_date(df, start_date, end_date):
    try:
        mask = (df['Date'] >= start_date) & (df['Date'] <= end_date)
        filtered = df.loc[mask].copy()
        filtered['Date'] = pd.to_datetime(filtered['Date']).dt.strftime('%Y-%m-%d')
        if filtered.empty:
            print("No transactions found in this date range.")
        else:
            print(filtered.reset_index(drop=True))
    except Exception as e:
        print(f"Error filtering transactions: {e}")

# 3. Add a Transaction
def add_transaction(df, date, category, description, amount):
    try:
        trans_type = input("Enter transaction type (Income or Expense): ").strip()

        new_transaction = {
            'Date': pd.to_datetime(date).strftime('%Y-%m-%d'),
            'Category': category,
            'Description': description,
            'Amount': float(amount),
            'Type': trans_type
        }

        df = pd.concat([df, pd.DataFrame([new_transaction])], ignore_index=True)
        print("Transaction added successfully!")
        return df
    except Exception as e:
        print(f"Error adding transaction: {e}")
        return df

# 4. Edit a Transaction
def edit_transaction(df, index):
    try:
        index = int(index)
        if index < 0 or index >= len(df):
            print("Invalid index.")
            return df

        print("Current Transaction:")
        print(df.iloc[index])

        new_date = input("New date (YYYY-MM-DD) or press Enter to keep: ")
        new_category = input("New category or press Enter to keep: ")
        new_description = input("New description or press Enter to keep: ")
        new_amount = input("New amount or press Enter to keep: ")
        new_type = input("New type (Income or Expense) or press Enter to keep: ")

        if new_date:
            df.at[index, 'Date'] = pd.to_datetime(new_date).strftime('%Y-%m-%d')
        if new_category:
            df.at[index, 'Category'] = new_category
        if new_description:
            df.at[index, 'Description'] = new_description
        if new_amount:
            df.at[index, 'Amount'] = float(new_amount)
        if new_type:
            df.at[index, 'Type'] = new_type

        print("Transaction updated successfully!")
        return df

    except Exception as e:
        print(f"Error editing transaction: {e}")
        return df

# 5. Delete a Transaction
def delete_transaction(df, index):
    try:
        index = int(index)
        if index < 0 or index >= len(df):
            print("Invalid index.")
            return df

        df = df.drop(index).reset_index(drop=True)
        print("Transaction deleted successfully!")
        return df

    except Exception as e:
        print(f"Error deleting transaction: {e}")
        return df

# 13. Save Transactions to CSV
def save_transactions(df, filename):
    try:
        df.to_csv(filename, index=False)
        print(f"Transactions saved to {filename} successfully!")
    except Exception as e:
        print(f"Error saving transactions: {e}")
