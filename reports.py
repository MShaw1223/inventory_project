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

items = [
    {
        "id": 1,  # id of item
        "details": {
            "name": "t-shirt",
            "price": 10.00,
            "quantity": 5,
            "category": "clothing",
        },
    }
]
print(items[0]["id"])
print(items[0]["details"])
# miller inventory_project % python3 reports.py
# 1
# {'name': 't-shirt', 'price': 10.0, 'quantity': 5, 'category': 'clothing'}

class Reports:
    def generate_report(self, items):
        print("Inventory Report: List of all items")
        print("===============================")
        for item in items:
            print(f"ID: {item['id']}")
            print(f"Name: {item['details']['name']}")
            print(f"Price: ${item['details']['price']}")
            print(f"Quantity: {item['details']['quantity']}")
            print(f"Category: {item['details']['category']}")
            print("----------------")

    def generate_category_report(self, items):
        print("Category Report: List of all items in all categories")
        print("=====================================================")

        categories = {}
        for item in items:
            category = item['details']['category']
            if category not in categories:
                categories[category] = []
            categories[category].append(item)


        for category, items_in_category in categories.items():
            print(f"Category: {category}")
            for item in items_in_category:
                print(
                    f"ID: {item['id']}, Name: {item['details']['name']}, "
                    f"Price: ${item['details']['price']}, "
                    f"Quantity: {item['details']['quantity']}")


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
        "id": 2,
        "details": {
            "name": "jeans",
            "price": 30.00,
            "quantity": 3,
            "category": "clothing",
        }
    },
    {
        "id": 3,
        "details": {
            "name": "laptop",
            "price": 800.00,
            "quantity": 2,
            "category": "electronics",
        }
    },
    {
        "id": 4,
        "details": {
            "name": "headphones",
            "price": 50.00,
            "quantity": 10,
            "category": "electronics",
        }
    }
]


report = Reports()

report.generate_report(items=items)
report.generate_category_report(items=items)
