class Inventory:
    def __init__(self):
        self.items = []

    def adding(self) -> dict:
        payload = {}

        payload["id"] = int(input("Enter product id:\n> "))

        details = {}
        details["name"] = input("Enter product name:\n> ")
        details["price"] = float(input("Enter price of item:\n> "))
        details["quantity"] = int(input("Enter the quantity in stock:\n> "))
        details["category"] = input("Enter category of product:\n> ")

        payload["details"] = details

        return payload

    def add_items(self, input_data) -> None:
        self.items.append(input_data)

    def updating(self, id, new, key="") -> None:
        for i in range(len(self.items)):
            if self.items[i]["id"] == id and key == "":
                self.items[i] = new
            elif self.items[i]["id"] == id:
                if key != "id" and key in self.items[i]["details"]:
                    self.items[i]["details"][key] = new
                elif key in self.items[i] and key == "id":
                    self.items[i]["id"] = new

    def get_all_items(self) -> list:
        return self.items

    def get_items(self, id, key="") -> list:
        for item in self.items:
            if item["id"] == id and key == "":
                return [item]
            elif item["id"] == id and key in item["details"]:
                return [item["details"][key]]
        else:
            return []
