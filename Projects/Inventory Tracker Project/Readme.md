# Inventory Tracker

## **About the Project**

The Inventory Tracker is a command-line application built with Python to manage inventory items, their quantities, and their prices.

This project combines Python concepts learned throughout my Data Science learning journey to create a practical application that allows users to add, remove, update, and view inventory items.

## **Features**

- **Add Items:** Add new inventory items with their quantities and prices.
- **Remove Items:** Remove existing items from the inventory.
- **Update Items:** Update the quantity or price of an existing item.
- **View Inventory:** Display all inventory items and their details.
- **Input Validation:** Handle invalid quantity and price inputs without crashing the program.
- **Menu-Driven Interface:** Navigate the application through an interactive command-line menu.

## **Technologies Used**

- Python
- Visual Studio Code
- Git and GitHub

## **Python Concepts Demonstrated**

- Dictionaries and nested dictionaries
- `while` loops
- `for` loops and `.items()`
- Conditional statements (`if`, `elif`, and `else`)
- User input with `input()`
- Dictionary methods such as `.get()` and `.pop()`
- Error handling with `try` and `except`
- Input validation and basic application logic

## **How to Run the Project**

**Prerequisite:** Python must be installed on your computer.

1. Open your terminal in the project folder.
2. Run the following command:

   ```bash
   python inventory_tracker.py
   ```

3. Follow the menu prompts to manage your inventory.

## **Example Inventory Structure**

The application uses a dictionary of dictionaries to store inventory items.

```python
inventory = {
    "pen": {"quantity": 10, "price": 50.0},
    "notebook": {"quantity": 5, "price": 300.0}
}
```

Each inventory item has a name, quantity, and price. The quantity and price can be accessed and updated through the item's nested dictionary.

## **Learning Objectives**

This project provides practical experience in combining Python data structures, loops, conditionals, user input, and error handling to solve a simple inventory management problem.

It also helps develop problem-solving skills, improve code organisation, and build confidence in creating interactive command-line applications.

## **Project Status**

**Status:** In Progress

This project will be updated as development continues. Future improvements may include calculating the total inventory value, warning when stock levels are low, and handling item names without case sensitivity.

## **Author's Note**

This project is part of my ongoing journey to learn Python and Data Science through consistent practice, experimentation, and hands-on project development.