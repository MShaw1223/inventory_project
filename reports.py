"""
reports on categories, prices
sort reports by attributes ie price

input --> dictionary :  item id, name, price, quantity, category
items = {
            1: # id of item
            {
            "name":"t-shirt",
            "price":10.00,
            "quantity": 5,
            "category": "clothing"
            }
        }
"""

# miller inventory_project % python3 reports.py
# 1
# {'name': 't-shirt', 'price': 10.0, 'quantity': 5, 'category': 'clothing'}


class Reports:

    def generate_report(self, items):
        print("Inventory Report: List of all items")
        print("================")
        for item in items:
            print(item)
            print(f"ID: {item['id']}")
            print(f"Name: {item['details']['name']}")
            print(f"Price: ${item['details']['price']}")
            print(f"Quantity: {item['details']['quantity']}")
            print(f"Category: {item['details']['category']}")
            print("----------------")

    def generate_category_report(self, items):
        print("Category Report: List of all items in all categories")
        print("=====================")

        categories = {}
        for item in items:
            category = item['details']['category']
            if category not in categories:
                categories[category] = []
            categories[category].append(item)

        print(categories)

        for category, items_cat in categories.items():
            print(f"Category: {category}")
            for item in items_cat:
                print(
                    f"ID: {item['id']}, Name: {item['details']['name']}, "
                    f"Price: ${item['details']['price']},"
                    f" Quantity: {item['details']['quantity']}")


    def generate_category_report_input(self, items):
        category_input = input(
            "Enter the category you want the report for (e.g., 'clothing', 'electronics'): ").strip().lower()

        categories = {}
        for item in items:
            category = item['details']['category']
            if category not in categories:
                categories[category] = []
            categories[category].append(item)

        if category_input not in categories.items():
            print(category_input)




        print("our categories", categories)
        print("input",category_input)


items = [
    {
        "id": 1,
        "details": {
            "name": "t-shirt",
            "price": 10.00,
            "quantity": 5,
            "category": "clothing",
        }
    },
    {
        "id": 2,  # id of item
        "details": {
            "name": "t-shirt",
            "price": 15.00,
            "quantity": 6,
            "category": "electronics",
        }
    }
]


report = Reports()
# report.generate_report(items=items)
# report.generate_category_report(items=items)
report.generate_category_report_input(items=items)