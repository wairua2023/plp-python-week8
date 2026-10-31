
import time

# Welcome message
print("\n------")
print(" WELCOME TO MY PYTHON TOOLKIT!")
print("--------")
print("This program contains three useful tools.")


# Tool 1: Countdown Timer
# Allows the user to enter seconds and counts down to zero.
def countdown_timer():
    print("\n--- COUNTDOWN TIMER ---")

    try:
        seconds = int(input("Enter time in seconds: "))

        if seconds <= 0:
            print(f"Please enter a number greater than zero.")
            return

        while seconds > 0:
            print(f"Time remaining: {seconds} seconds")
            time.sleep(1)
            seconds -= 1

        print(f"Time is up!")

    except ValueError:
        print(f"Please enter a valid whole number.")


# Tool 2: Shopping List Manager
# Allows the user to add, remove and view shopping list items.
def shopping_list_manager():
    shopping_list = []

    while True:
        print("\n--- SHOPPING LIST MANAGER ---")
        print("1. Add item")
        print("2. Remove item")
        print("3. View shopping list")
        print("4. Return to main menu")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            item = input("Enter item to add: ")
            shopping_list.append(item)
            print(f"{item} has been added to your shopping list.")

        elif choice == "2":
            item = input("Enter item to remove: ")

            if item in shopping_list:
                shopping_list.remove(item)
                print(f"{item} has been removed.")
            else:
                print(f"{item} was not found in your shopping list.")

        elif choice == "3":
            if shopping_list:
                print("\nYour shopping list:")
                for item in shopping_list:
                    print(f"- {item}")
            else:
                print(f"Your shopping list is empty.")

        elif choice == "4":
            break

        else:
            print(f"Invalid choice. Please select 1-4.")


# Tool 3: Simple Calculator
# Allows the user to perform addition, subtraction, multiplication and division.
def simple_calculator():
    print("\n--- SIMPLE CALCULATOR ---")

    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))

        print("\nChoose an operation:")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            result = num1 + num2
            print(f"The sum is: {result}")

        elif choice == "2":
            result = num1 - num2
            print(f"The difference is: {result}")

        elif choice == "3":
            result = num1 * num2
            print(f"The product is: {result}")

        elif choice == "4":
            if num2 != 0:
                result = num1 / num2
                print(f"The division result is: {result}")
            else:
                print(f"Error: You cannot divide by zero.")

        else:
            print(f"Invalid operation selected.")

    except ValueError:
        print(f"Please enter valid numbers.")


# Main Menu
# Allows the user to select and run any of the three tools.
while True:
    print("\n===== MY PYTHON TOOLKIT =====")
    print("1. Countdown Timer")
    print("2. Shopping List Manager")
    print("3. Simple Calculator")
    print("4. Quit")

    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        countdown_timer()

    elif choice == "2":
        shopping_list_manager()

    elif choice == "3":
        simple_calculator()

    elif choice == "4":
        print("\nThank you for using my Python Toolkit!")
        print("Have a wonderful day. Goodbye!")
        break

    else:
        print(f"Invalid choice! Please choose between 1 and 4.")
