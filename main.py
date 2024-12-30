from inventory import Inventory
from reports import Reports


def get_input() -> int:
    print(
        "Menu:\n1. Add Items\n2. Get all items\n3. Get a specific item or key\n4. Update an item or key\n5. Show Overview of Inventory\n6. Genrerate report\n7. Generate category Report\n8. Quit"
    )
    choice = int(input("> "))
    return choice


def main():
    inv = Inventory()
    report = Reports()

    while True:
        choice = get_input()

        match choice:
            case 1:
                while True:
                    inv.add_items(inv.adding())
                    print()
                    choice = input("Would you like to add more items ? Y/N\n> ")
                    if choice.lower() != "y":
                        break

            case 2:
                print(inv.get_all_items())

            case 3:
                id = int(input("Enter the ID to lookup:\n> "))
                key = input("Enter the key (press enter to show all details):\n> ")
                print(inv.get_items(id, key))

            case 4:
                id = int(input("Enter a new ID\n> "))
                key = input("Enter new key (press enter to update entire record):\n> ")
                if key == "":
                    new_data = inv.adding()
                else:
                    new_data = eval(
                        input("Enter the new data (wrap string in quotations):\n> ")
                    )
                inv.updating(id, new_data, key)

            case 5:
                items = inv.get_all_items()
                report.overview(items)

            case 6:
                category = input(
                    "Enter the category (press enter to show report for all):\n> "
                )

                items = inv.get_all_items()
                print(report.generate_report(items, category))

            case 7:
                items = inv.get_all_items()
                report.generate_category_report(items)

            case 8:
                break
            case _:
                print("Incorrect input.")


if __name__ == "__main__":
    main()
