from inventory import Inventory
from reports import Reports


def get_input():
    print(
        "Menu:\n1. Add Items\n2. Get all items\n3. Get a specific item or key\n4. Update an item or key\n5. Show Overview of Inventory\n6. Genrerate report\n7. Generate category Report"
    )
    choice = int(input("> "))
    return choice


def main():
    inv = Inventory()
    report = Reports()

    print("\n --- show initialised list of items --- ")
    print(inv.get_all_items())

    while True:
        inv.add_items(inv.adding())
        print()
        choice = input("Would you like to add more items ? Y/N\n> ")
        if choice.lower() == "n":
            break

    print("\n --- show populated list of items --- ")
    print(inv.get_all_items())

    inv.updating(1, 15, key="price")
    inv.updating(
        1,
        {
            "id": 10,
            "details": {
                "price": 1,
                "category": "sports",
                "name": "bike",
                "quantity": 1,
            },
        },
    )

    print("\n --- show updated list of items --- ")
    print(inv.get_all_items())

    print("\n --- show specific item --- ")
    print(inv.get_items(id=2))
    print("\n --- show specific key from item --- ")
    print(inv.get_items(id=2, key="name"))

    items = inv.get_all_items()

    print("\n --- reports --- ")
    report.overview(items)
    print(report.generate_report(items=items))
    print(report.generate_report(items=items))
    print(report.generate_report(items=items, category="electronics"))
    report.generate_category_report(items=items)


if __name__ == "__main__":
    main()
