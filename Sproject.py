import csv


def ExpINput():

  expenses = []

  try:
    n = int(input("enter the number of expenses to be added like 1,2 3.. : "))
  except ValueError:
    print("Enter a valid number")
    return expenses

  for _ in range(n):
    while True:
      try:
        expense = {}
        expense["date"] = input("\nEnter date in formar YYYY-MM-DD :")
        expense["category"] = input("Enter a category: Food or Travel:")
        expense["amount"] = float(input("Enter amount: "))
        expense["Description"] = input("Provide description: ")
        expenses.append(expense)
        break
      except ValueError:
        print("Enter valid details")

  return expenses


def calculate_expenses(exp, bud):
  total_expenses = float(0.0)
  # for expense in exp:
  #   expense["amount"] = float(expense["amount"])
  total_expenses = sum(float(expense["amount"]) for expense in exp)
  remaining_budget = bud - total_expenses
  if remaining_budget < 0:
    print("\nYou have exceeded your budget! \n")
  else:
    print(f"Remaining budget: {remaining_budget}")


def Print_expense(exps):
  for e in exps:
    print(e)


def Save_expenses(exps):
  with open("expenses.csv", "w") as file:
    writer = csv.DictWriter(
        file, fieldnames=["date", "category", "amount", "Description"])
    writer.writeheader()
    for expense in exps:
      writer.writerow(expense)


def Load_expenses():
  expenses = []
  with open("expenses.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
      expenses.append(row)
  return expenses


def main():
  exp = []
  Interactive(exp)


def Interactive(exp):
  while True:
    print("1. Add Expenses")
    print("2. View Expenses")
    print("3. Track Budget")
    print("4. Save Expenses")
    print("5. Exit")
    choice = input("Enter your choice: ")
    if choice == "1":
      exp = ExpINput() + Load_expenses()
    elif choice == "2":
      exp = Load_expenses()  # Load existing expenses from the file
      if len(exp) == 0:
        print("No expenses found. Please add expenses first.")
      else:
        Print_expense(exp)
    elif choice == "3":
      bud = Budget()
      exp = Load_expenses()
      print("expenses loaded")
      calculate_expenses(exp, bud)
    #exp = ExpINput()
    # exp.append(Load_expenses())
    #Print_expense(exp)
    #bud = Budget()
    #print("\nYour monthly income is: ", bud)
    elif choice == "4":
      Save_expenses(exp)
    else:
      print("Exiting the program.")
      break


def Budget():

  while True:
    try:
      budget = float(input("\nEnter your monthly income: "))
      break
    except ValueError:
      print("Enter valid number for income")
  return budget


if __name__ == "__main__":
  main()
