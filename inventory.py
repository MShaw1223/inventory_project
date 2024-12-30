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

    def updating(self, id, new, key="") -> None:
        for item in self.items:
            if item["id"] == id and key == "":
                item = new
            elif item["id"] == id and key in item:
                item[key] = new

    def get_items(self, id=0, key="") -> list:
        payload = []
        for item in self.items:
            if id == 0 and key == "":
                return self.items
            elif item["id"] == id and key == "":
                payload.append(item)
            elif item["id"] == id and key in item:
                payload.append(item[key])
        return payload
