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


class foo:
    # data = [{}]
    def __init__(self, data) -> None:
        pass


items = [
    {
        "id": 1,  # id of item
        "details": {
            "name": "t-shirt",
            "price": 10.00,
            "quantity": 5,
            "category": "clothing",
        },
    },
    {
        "id": 2,  # id of item
        "details": {
            "name": "t-shirt",
            "price": 10.00,
            "quantity": 5,
            "category": "clothing",
        },
    },
]
print(items[0]["id"])
print(items[0]["details"])
# miller inventory_project % python3 reports.py
# 1
# {'name': 't-shirt', 'price': 10.0, 'quantity': 5, 'category': 'clothing'}
