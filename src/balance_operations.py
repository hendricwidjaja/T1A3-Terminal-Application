from datetime import datetime
from file_operations import save_balance


FILE_PATH = "../data/debt_balances.json"

# View a summary of all balances (if balance names are the same, add all entry amounts)
def balance_summaries(entries):
    # Initialize empty dictionary to contain summary of each balance
    total_balance = {}
    # For each entry in the JSON file, access the "Balance Name" & "Entry" values and store them into the variables: balance_name & entry_amount
    for entry in entries: 
        balance_name = entry["Balance Name"]
        entry_amount = entry["Entry"]
        # If a balance_name (e.g. Alice) is already in the total_balance dictionary, add its corresponding entry_amount to the existing entry total
        if balance_name in total_balance:
            total_balance[balance_name] += entry_amount
        # Else, if the balance_name is not yet a key in the total_balance dictionary, create a new key-value pair and set the value to the corresponding entry_amount
        else:
            total_balance[balance_name] = entry_amount
    # .items() method to iterate through total_balance dictionary and assign each balance_name with its corresponding total. Then print.
    for balance_name, total in total_balance.items():
        print(f"{balance_name}: ${total:.2f}")


# Create a balance (if balance name does not exist, create 1st entry (incl. balance name, entry amount & date))
def create_balance(entries):
    print("Please enter the following details")
    balance_name = input("Balance Name: ")
    if any(entry["Balance Name"] == balance_name for entry in entries):
        print("Balance name already exists. Please create a balance with a unique name")
        return
    balance_amount = float(input("Balance Amount: "))
    print("------------------")
    print("Leaving the date input blank will return today's date")
    print("------------------")
    balance_date = input("Date (YYYY-MM-DD):")

    # If balance_date variable holds no value, insert today's date in string format (JSON file cannot hold date values)
    if not balance_date:
        balance_date = datetime.today().strftime('%Y-%m-%d')

    # Store new entry in "new_balance" variable
    new_balance = {"Balance Name": balance_name, "Entry": balance_amount, "Date": balance_date}
    # Append "new_balance" to entries
    entries.append(new_balance)
    # Use save_balance function to rewrite entries (incl. new_balance)
    save_balance(FILE_PATH, entries)
    print(f"Your entry for '{balance_name}' has been created successfully.")


# Delete a balance (if balance name = "x", delete entry)

# Select a balance (Allow user to view balance history)