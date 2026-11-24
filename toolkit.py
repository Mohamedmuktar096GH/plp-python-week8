import random

# Welcoming start message
print("====================================")
print("   WELCOME TO MY MINI-TOOLKIT!")
print("====================================")

# List to store tasks that changes while the program runs
todo_list = []

# Main menu loop that runs until the user chooses to quit
while True:
    print("\nPlease choose a tool from the menu:")
    print("1. To-Do List Manager")
    print("2. Number Guessing Game")
    print("3. Simple Calculator")
    print("4. Quit")

    choice = input("Choose an option (1-4): ").strip()

    # ---------------------------------------------------------
    # TOOL 1: TO-DO LIST MANAGER
    # Lets users view, add, and remove tasks using a dynamic list.
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
                    print("You cannot add an empty task.")

            elif todo_choice == "3":
                if len(todo_list) == 0:
                    print("Nothing to remove — your list is empty!")
                else:
                    for index, task in enumerate(todo_list, start=1):
                        print(f"{index}. {task}")
                    task_num = input("Enter the task number to remove: ").strip()
                    if task_num.isdigit() and 1 <= int(task_num) <= len(todo_list):
                        removed = todo_list.pop(int(task_num) - 1)
                        print(f"Removed '{removed}' from your list!")
                    else:
                        print("Invalid task number. Please try again.")

            elif todo_choice == "4":
                print("Returning to the main menu...")
                break
            else:
                print("Oops! Please pick 1, 2, 3, or 4.")

    # ---------------------------------------------------------
    # TOOL 2: NUMBER GUESSING GAME
    # Picks a random number from 1-20 and gives hints until guessed.
    # ---------------------------------------------------------
    elif choice == "2":
        print("\n--- Number Guessing Game ---")
        secret_number = random.randint(1, 20)
        attempts = 0
        print("I am thinking of a number between 1 and 20.")

        while True:
            guess_input = input("Take a guess: ").strip()
            if not guess_input.isdigit():
                print("Please enter a whole number between 1 and 20.")
                continue

            guess = int(guess_input)
            attempts += 1

            if guess < secret_number:
                print(f"{guess} is too low! Try again.")
            elif guess > secret_number:
                print(f"{guess} is too high! Try again.")
            else:
                print(f"Spot on! You guessed {secret_number} in {attempts} tries!")
                break

    # ---------------------------------------------------------
    # TOOL 3: SIMPLE CALCULATOR
    # Performs basic arithmetic (+, -, *, /) on two numbers.
    # ---------------------------------------------------------
    elif choice == "3":
        print("\n--- Simple Calculator ---")
        num1_input = input("Enter the first number: ").strip()
        operator = input("Choose an operation (+, -, *, /): ").strip()
        num2_input = input("Enter the second number: ").strip()

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
                    print(f"Result: {num1} / {num2} = {num1 / num2}")
            else:
                print(f"Sorry, '{operator}' is not a valid operator.")
        except ValueError:
            print("Please enter valid numbers next time!")

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
