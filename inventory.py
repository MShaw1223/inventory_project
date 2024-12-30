class Inventory:
    items = []

    def __init__(self, name, price, quantity, category, item_id):
        self.item_id = item_id
        self.item_name = name
        self.price = price
        self.quantity = quantity
        self.category = category

    def adding(self):
        pass

    def updating(self):
        pass

    def get_items(self):
        return Inventory.items
