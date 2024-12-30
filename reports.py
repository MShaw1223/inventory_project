"""
reports on categories, prices
sort reports by attributes ie price

input --> dictionary :  item id, name, price, quantity, category
"""


class Reports:
    def overview(self, items):
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
            category = item["details"]["category"]
            if category not in categories:
                categories[category] = []
            categories[category].append(item)

        for category, items_in_category in categories.items():
            print(f"Category: {category}")
            for item in items_in_category:
                print(
                    f"ID: {item['id']}, Name: {item['details']['name']}, "
                    f"Price: ${item['details']['price']}, "
                    f"Quantity: {item['details']['quantity']}"
                )

    def generate_report(self, items, category="") -> list:
        msg = "Report: List of items in selected categories"
        print(msg)
        print("=" * len(msg))

        set_categories = set()
        for item in items:
            if item["details"]["category"] not in set_categories:
                set_categories.add(item["details"]["category"])

        search_result = []
        for cat in set_categories:
            if category == "":
                return items
            else:
                for item in items:
                    if item["details"]["category"] == cat:
                        search_result.append(item)

        return search_result
