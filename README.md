# Personal Mini-Toolkit

A menu-driven Python command-line application that brings together three useful everyday tools in one program.

## What This Toolkit Does
1. **To-Do List Manager:** Allows you to add, view, and remove tasks using a dynamic list during your session.
2. **Number Guessing Game:** Picks a random secret number between 1 and 20 and gives hints until you guess it right.
3. **Simple Calculator:** Performs addition, subtraction, multiplication, and division while handling division by zero safely.

## How to Run It
1. Make sure **Python 3** is installed on your computer.
2. Download or clone this repository (`plp-python-week8`).
3. Open a terminal inside the project folder and run:
   ```bash
   python toolkit.py
   ```

## Reflection
Planning the tools and exact menu layout in `toolkit_plan.txt` before writing any code made structuring the main `while` loop much smoother. The hardest part of this project was managing nested loops inside the To-Do List Manager so returning to the main menu wouldn't accidentally close the entire program. The bug that took longest to fix was handling non-numeric user inputs in the calculator and guessing game, which caused crashes until I added input validation checks. Testing every menu branch—including invalid entries and quitting—ensured the program stays polite and stable. If I had one more week, I would save the To-Do list to a text file so tasks remain stored after closing the app.
