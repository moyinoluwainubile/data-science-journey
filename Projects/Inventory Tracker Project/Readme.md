# Inventory Tracker

## About the Project

The Inventory Tracker is a Python application for managing inventory items, their quantities, and their prices.

This project combines Python concepts learned throughout my Data Science learning journey to build a practical application that allows users to add, remove, update, and view inventory items.

The project began as a command-line application and is now being developed towards online deployment using Streamlit and Firebase.

## Features

- **Add Items:** Add inventory items with their quantities and prices.
- **Remove Items:** Remove existing inventory items.
- **Update Items:** Update the quantity or price of an existing item.
- **View Inventory:** Display all inventory items and their details.
- **Input Validation:** Handle invalid quantity and price inputs without crashing the program.
- **Case-Insensitive Item Names:** Handle item names consistently regardless of capitalisation or surrounding spaces.
- **Total Inventory Value:** Calculate the combined value of the inventory based on item quantities and prices.
- **Low-Stock Warning:** Display a warning when an item's quantity falls below five.
- **Menu-Driven Interface:** Navigate the application through an interactive menu.

## Technologies Used

- Python
- Visual Studio Code
- Git and GitHub

## Python Concepts Demonstrated

- Dictionaries and nested dictionaries
- `while` loops and `for` loops
- Dictionary iteration using `.items()`
- Conditional statements (`if`, `elif`, and `else`)
- User input with `input()`
- Type conversion using `int()` and `float()`
- Error handling with `try` and `except`
- Dictionary membership checks using `in`
- Dictionary item deletion using `del`
- String methods such as `.strip()` and `.lower()`
- Calculations using dictionary values
- Input validation and application logic

## How to Run the Command-Line Version

**Prerequisite:** Python must be installed on your computer.

1. Open a terminal in the folder containing `inventory_tracker.py`.
2. Run the following command:

   ```bash
   python inventory_tracker.py
   ```

3. Follow the menu prompts to manage your inventory.

## Example Inventory Structure

The application stores inventory items in a dictionary of dictionaries.

```python
inventories = {
    "pen": {"quantity": 10, "price": 50.0},
    "notebook": {"quantity": 5, "price": 300.0},
}
```

Each inventory item has a quantity and a price. These values can be accessed and updated through the item's nested dictionary.

## Learning Objectives

This project provides practical experience in combining Python data structures, loops, conditional statements, user input, and error handling to solve an inventory management problem.

It also develops problem-solving skills, encourages experimentation, and builds confidence in creating interactive applications.

## Project Status

**Status: In Progress**

The command-line version has been implemented and pushed to GitHub. Work is ongoing to publish the application using Streamlit and integrate Firebase, this will be contained in my "Self Practice" Repo.

Future improvements may include completing the online version, connecting the inventory data to a persistent database, and refining the application's interface and functionality.

## Author's Note

This project is part of my ongoing journey to learn Python and Data Science through consistent practice, experimentation, and hands-on project development.