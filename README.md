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

---------

## How to Install and Run the Project
1. Clone the repository: 
```
git clone git@github.com:MShaw1223/inventory_project.git
````
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
> <span style="color: red;">enter your choice here</span>
</pre>

>**!Tip:**
> Add at least **3 items** at the beginning. This will allow you to test all functionalities 
> and generate reports effectively, as the initial inventory is empty! 
---
