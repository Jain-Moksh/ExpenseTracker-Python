from expense import Expense


def main():
    print("Welcome to Titans Expense Tracker ")
    expense_file_path = "expenses.csv"
    budget = 50000
    # getting user input of its expense
    expense = get_user_expense()

    # saving the use expense to file
    save_expense_to_file(expense, expense_file_path)

    # summarizing expense to display the output
    summarize_expense(expense_file_path, budget)


def get_user_expense():
    expense_name = input("Enter the expense name : ")
    expense_amt = float(input("Enter the amount of the expense : "))
    expense_categories = ["Food", "Home", "Work", "Fun", "Other"]

    while True:
        print("Available Categories : ")
        for i, category_name in enumerate(expense_categories):
            print(f"  {i+1}. {category_name}")

        category_range = f"[1 - {len(expense_categories)}]"

        selected_category_index = (
            int(input(f"Enter the category number {category_range} : "))
        ) - 1

        if selected_category_index in range(len(expense_categories)):
            selected_category_name = expense_categories[selected_category_index]
            new_expense = Expense(
                name=expense_name, category=selected_category_name, amount=expense_amt
            )
            return new_expense
        else:
            print(f"Invalid input. Try again! ")


def save_expense_to_file(expense, expense_file_path):
    print(f" Saving the user Expense: {expense} to {expense_file_path}")
    with open(expense_file_path, "a") as f:
        f.write(f"-> {expense.name},{expense.category},{expense.amount}\n")


def summarize_expense(expense_file_path, budget):
    expenses = []
    with open(expense_file_path, "r") as f:
        lines = f.readlines()

        for line in lines:
            stripped_line = line.strip()

            expense_name, expense_category, expense_amount = stripped_line.split(",")

            line_expense = Expense(
                name=expense_name,
                category=expense_category,
                amount=float(expense_amount),
            )
            expenses.append(line_expense)

    amount_by_category = {}

    for each_expense in expenses:
        key = each_expense.category
        if key in amount_by_category:
            amount_by_category[key] += each_expense.amount
        else:
            amount_by_category[key] = each_expense.amount

    print("Your Expenses by Category are below :")
    for key, amount in amount_by_category.items():
        print(f"-> {key}: ${amount:.2f}")

    total_expenses = sum([x.amount for x in expenses])
    print(f"The total amount spent by you in this month is : {total_expenses}")

    remaining_budget = budget - total_expenses
    print(
        f"After all your expenses the amount of budget left to use is : {green(remaining_budget)}"
    )


def green(text):
    return f"\033[92m{text}\033[0m"


if __name__ == "__main__":
    main()
