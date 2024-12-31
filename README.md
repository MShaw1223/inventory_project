# Inventory Management System

## Overview

The **Inventory Management System** is a Python-based application designed to manage inventory.
The system offers functionalities for adding, updating, and generating detailed reports about the inventory.

This system applies object-oriented programming (OOP) concepts and modular design for better maintainability and extensibility.

---

## Features

1. **Add Items**  
   Asks the user to enter details for a new item to the inventory, including details like id, name, price, quantity, and category
   Returns this information as a dictionary.

2. **View All Items**  
   Display all items currently stored in the inventory.

3. **View Specific Item or Key**  
   Retrieve details about a specific item by its ID or fetch the value of a specific key.

4. **Update Items**  
   Updates a item's details in the inventory using its `ID`.
   You can update specific details (like `price` or `quantity`) or the entire item.

5. **Inventory Overview**  
   Generates a report of all items in the inventory, listing their ID, name, price, quantity, and category.
   If the inventory is empty, it prints a message indicating that it's empty.

6. **Generate Reports**  
   Generate the reports of all items or filter them by category.
   If no items match the category or the inventory is empty, a message is printed.

7. **Generate Category Reports**  
   Generates a report that shows all items in the inventory, group by their categories.
   If there are no items in the inventory, it will display a message saying that it's empty.

8. **Exit**  
   Quit the application.

---

## How to Install and Run the Project

1. Clone the repository:

```
git clone git@github.com:MShaw1223/inventory_project.git
```

2. Navigate to the project directory:

```
cd inventory-management
```

3. Execute the program using the command:

```
python3 main.py
```

4. Follow the on-screen menu to interact with the inventory system.
   <pre>
   Menu:
   1. Add Items
   2. Get all items
   3. Get a specific item or key
   4. Update an item or key
   5. Show Overview of Inventory
   6. Generate report
   7. Generate category Report
   8. Quit
   > <span style="color: red;">Enter your choice here</span>
   </pre>

> **!Tip:**
> Add at least **3 items** at the beginning. This will allow you to test all functionalities
> and generate reports effectively, as the initial inventory is empty!

---

## Classes and methods

### Inventory

- The data collection class for the Inventory Management System(IMS) application.

### Inventory Methods:

- `__init__(self) -> None`

  - Init takes a parameter `self` and assigns the field `items` to the class.

  - The init constructor initialises an `items` as an empty list, to store the item dictionaries (see next) in the inventory.

- `adding(self) -> dict`

  - The `adding` method returns an item dictionary, structured as following:

  ```

     {
     "id": int,
     "details": {
        "price": float,
        "category": string,
        "name": string,
        "quantity": int,
        },
     }
  ```

- `add_items(self, input_data) -> None`
  - Appends the `input_data` param, which is a dictionary, to the `items` list.
  - By taking in self as a parameter, add_items is able to add data to the field via `self.items.append(input_data)`.
- `updating(self, id, new, key="") -> None`
  - The method `updating` takes in `self`, to enable the items list data to be updated.
  - `Key` is an optional parameter in-case an entire item dictionary is updated. Additionally it allows specific keys in the `item` dictionary to be updated.
  - The method uses a brute force search to find the dictionary with the matching ID based on the `id` parameter.
    - This can be optimised to a more efficient algorithm; however, as it will deal with small data volume it suffices.
- `get_all_items(self) -> list`
  - Returns the field items which is a list of item dictionaries.
    ```
       return self.items
    ```
- `get_items(self, id, key="") -> list`
  - `get_items` iterates through the list `self.items`, brute force searching for a matching id in the list.
  - Additionally a key to search for can be provided as a parameter to find specific information in the `details` field of the dictionary.

---

### Reports

- Data formatting and insight class, of the IMS application.

### Reports methods

- `overview(self, items) -> None`
  - `overview` takes in items, which is a list of item dictionaries.
  - It prints out a formatted overview of the whole list.
- `generate_category_report(self, items) -> None`

  - Generates a categorised report of each item.
  - Example output:

  ```
   Category: Toys
   ID: 1, Name: Ball, Price: 10.99, Quantity: 2, Category: Toys

  ```

- `generate_report(self, items, category="") -> None`
  - Extended functionality of `generate_category_report`, allowing the printing of a report on a single category of items.
  - To speed up lookup time, we create a set of the categories. Then we iterate through the `items` list, and if a category is provided, will print the matching items from `self.items`.
