import random

# Welcome message when the program starts
print("========================================")
print("  Welcome to your Personal Mini-Toolkit!")
print("========================================")

# Create an empty list to store tasks across multiple visits to the To-Do tool
todo_list = []

# Main program loop that runs until the user chooses to quit
while True:
    print("\n========================================")
    print("        PERSONAL MINI-TOOLKIT")
    print("========================================")
    print("1. To-Do List Manager")
    print("2. Number Guessing Game")
    print("3. Simple Calculator")
    print("4. Quit")
    print("----------------------------------------")
    
    choice = input("Choose an option (1-4): ").strip()

    # ---------------------------------------------------------
    # TOOL 1: TO-DO LIST MANAGER
    # Manages a dynamic list where users can add, view, or remove tasks.
    # ---------------------------------------------------------
    if choice == "1":
        print("\n--- To-Do List Manager ---")
        while True:
            print("\nOptions: [1] View Tasks  [2] Add Task  [3] Remove Task  [4] Back to Main Menu")
            todo_choice = input("What would you like to do? ").strip()

            if todo_choice == "1":
                if len(todo_list) == 0:
                    print("Your to-do list is currently empty!")
                else:
                    print("\nYour Current Tasks:")
                    for index, task in enumerate(todo_list, start=1):
                        print(f"{index}. {task}")

            elif todo_choice == "2":
                new_task = input("Enter the task you want to add: ").strip()
                if new_task:
                    todo_list.append(new_task)
                    print(f"Added '{new_task}' to your list!")
                else:
                    print("Task cannot be empty.")

            elif todo_choice == "3":
                if len(todo_list) == 0:
                    print("Nothing to remove—your list is empty!")
                else:
                    for index, task in enumerate(todo_list, start=1):
                        print(f"{index}. {task}")
                    remove_input = input("Enter the number of the task to remove: ").strip()
                    if remove_input.isdigit():
                        task_num = int(remove_input)
                        if 1 <= task_num <= len(todo_list):
                            removed = todo_list.pop(task_num - 1)
                            print(f"Removed '{removed}' from your list!")
                        else:
                            print(f"Please enter a number between 1 and {len(todo_list)}.")
                    else:
                        print("Invalid input. Please enter a valid task number.")

            elif todo_choice == "4":
                print("Returning to the main menu...")
                break

            else:
                print(f"'{todo_choice}' is not a valid option. Please pick 1, 2, 3, or 4.")

    # ---------------------------------------------------------
    # TOOL 2: NUMBER GUESSING GAME
    # Picks a random number from 1 to 20 and loops until the user guesses it.
    # ---------------------------------------------------------
    elif choice == "2":
        print("\n--- Number Guessing Game ---")
        secret_number = random.randint(1, 20)
        attempts = 0
        print("I am thinking of a number between 1 and 20. Can you guess it?")

        while True:
            guess_input = input("Enter your guess: ").strip()
            
            # Ensure the user typed a valid number
            if not guess_input.isdigit():
                print("Please enter a valid whole number!")
                continue

            guess = int(guess_input)
            attempts += 1

            if guess < secret_number:
                print(f"{guess} is too low! Try again.")
            elif guess > secret_number:
                print(f"{guess} is too high! Try again.")
            else:
                print(f"Congratulations! You guessed {secret_number} in {attempts} attempts!")
                break

    # ---------------------------------------------------------
    # TOOL 3: SIMPLE CALCULATOR
    # Takes two numbers and an operator, then calculates and displays the result.
    # ---------------------------------------------------------
    elif choice == "3":
        print("\n--- Simple Calculator ---")
        num1_input = input("Enter the first number: ").strip()
        operator = input("Choose an operation (+, -, *, /): ").strip()
        num2_input = input("Enter the second number: ").strip()

        # Check if inputs are valid numbers (allowing decimals and negative signs)
        try:
            num1 = float(num1_input)
            num2 = float(num2_input)

            if operator == "+":
                print(f"Result: {num1} + {num2} = {num1 + num2}")
            elif operator == "-":
                print(f"Result: {num1} - {num2} = {num1 - num2}")
            elif operator == "*":
                print(f"Result: {num1} * {num2} = {num1 * num2}")
            elif operator == "/":
                if num2 == 0:
                    print("Error: You cannot divide by zero!")
                else:
                    print(f"Result: {num1} / {num2} = {num1 / num2:.2f}")
            else:
                print(f"Sorry, '{operator}' is not a supported operator. Please use +, -, *, or /.")
        except ValueError:
            print("Invalid number entered. Please make sure you type numeric values.")

    # ---------------------------------------------------------
    # OPTION 4: QUIT PROGRAM
    # ---------------------------------------------------------
        elif choice == "4":
        print("\nThanks for using the Personal Mini-Toolkit. Goodbye!")
        break

    # ---------------------------------------------------------
    # INVALID MENU CHOICE HANDLER
    # ---------------------------------------------------------
    else:
        print(f"\nOops! '{choice}' is not on the menu. Please enter 1, 2, 3, or 4.")

