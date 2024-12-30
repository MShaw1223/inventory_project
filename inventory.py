class Inventory:
    def __init__(self):
        self.items = []

    def adding(self) -> dict:
        payload = {}

        payload["id"] = int(input("Enter product id:\n> "))
        payload["name"] = input("Enter product name:\n> ")
        payload["price"] = float(input("Enter price of item:\n> "))
        payload["quantity"] = int(input("Enter the quantity in stock:\n> "))

        return payload

    def add_items(self, input_data) -> None:
        self.items.append(input_data)

    def updating(self):
        # iterate through items
        # search for key to change
        pass

    def get_items(self):
        return self.items
