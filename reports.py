class Reports:
    def overview(self, items):
        if not items:
            print("Inventory Report: No items available.")
            print("The inventory is currently empty.")
        else:
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
                    f"Quantity: {item['details']['quantity']}, "
                    f"Category: {item['details']['category']}"
                )
        if categories == {}:
            print("The inventory is currently empty.")

    def generate_report(self, items, category="") -> list:
        if not items:
            print("The inventory is currently empty.")
            return
        elif category:
            print(f"\nReport: List of items in {category} category:")
            print("=================================================")
        else:
            print("\nReport: List of all items:")
            print("=================================================")

        set_categories = set()
        for item in items:
            if item["details"]["category"] not in set_categories:
                set_categories.add(item["details"]["category"])

        search_result = []

        for cat in set_categories:
            if category == "":
                for item in items:
                    print(
                        f"ID: {item['id']}, Name: {item['details']['name']}, "
                        f"Price: ${item['details']['price']}, "
                        f"Quantity: {item['details']['quantity']}"
                    )
                break
            elif category == cat:
                for item in items:
                    if item["details"]["category"] == cat:
                        search_result.append(item)
                        print(
                            f"ID: {item['id']}, Name: {item['details']['name']}, "
                            f"Price: ${item['details']['price']}, "
                            f"Quantity: {item['details']['quantity']}"
                        )

        if  category not in set_categories:
            print(f"No items found in the {category} category.")

