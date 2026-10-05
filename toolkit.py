# PERSONAL MINI-TOOLKIT

# A simple program with four useful tools.

def calculator():
    print("\n--- Simple Calculator ---")
    number1 = float(input("Enter the first number: "))
    number2 = float(input("Enter the second number: "))
    operation = input("Enter +, -, * or /: ")

    if operation == "+":
        answer = number1 + number2
    elif operation == "-":
        answer = number1 - number2
    elif operation == "*":
        answer = number1 * number2
    elif operation == "/":
        if number2 == 0:
            print("You cannot divide by zero.")
            return
        answer = number1 / number2
    else:
        print("Invalid operation.")
        return

    print(f"The answer is {answer}.")


def todo_list(tasks):
    while True:
        print("\n--- To-Do List ---")
        print("1. Add task")
        print("2. Show tasks")
        print("3. Remove task")
        print("4. Back to main menu")

        choice = input("Choose an option: ")

        if choice == "1":
            task = input("Enter a task: ")
            tasks.append(task)
            print(f"Task '{task}' was added.")

        elif choice == "2":
            if len(tasks) == 0:
                print("Your to-do list is empty.")
            else:
                print("Your tasks:")
                for number, task in enumerate(tasks, 1):
                    print(f"{number}. {task}")

        elif choice == "3":
            if len(tasks) == 0:
                print("There are no tasks to remove.")
            else:
                task = input("Enter the task to remove: ")
                if task in tasks:
                    tasks.remove(task)
                    print(f"Task '{task}' was removed.")
                else:
                    print(f"Task '{task}' was not found.")

        elif choice == "4":
            print("Returning to the main menu.")
            break

        else:
            print(f"'{choice}' is not a valid option. Please choose 1, 2, 3, or 4.")


def guessing_game():
    secret_number = 7
    attempts = 0

    print("\n--- Number Guessing Game ---")
    print("I am thinking of a number from 1 to 10.")

    while True:
        guess = int(input("Enter your guess: "))
        attempts = attempts + 1

        if guess == secret_number:
            print(f"Correct! You got it in {attempts} attempts.")
            break
        elif guess < secret_number:
            print("Too low. Try again!")
        else:
            print("Too high. Try again!")


def name_formatter():
    print("\n--- Name Formatter ---")
    name = input("Enter your full name: ").strip()

    if name:
        formatted_name = name.title()
        print(f"Hello, {formatted_name}! Your name looks great.")
    else:
        print("You did not enter a name.")


tasks = []

print("======================================")
print(" Welcome to My Personal Mini-Toolkit!")
print("======================================")

while True:
    print("\n=== Personal Mini-Toolkit ===")
    print("1. Simple Calculator")
    print("2. To-Do List")
    print("3. Number Guessing Game")
    print("4. Name Formatter")
    print("5. Quit")

    choice = input("Choose an option: ")

    if choice == "1":
        calculator()

    elif choice == "2":
        todo_list(tasks)

    elif choice == "3":
        guessing_game()

    elif choice == "4":
        name_formatter()

    elif choice == "5":
        print("Thank you for using my Personal Mini-Toolkit. Goodbye!")
        break

    else:
        print(f"'{choice}' is not a menu option. Please choose 1, 2, 3, 4, or 5.")