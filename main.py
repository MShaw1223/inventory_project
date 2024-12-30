from inventory import Inventory


def main():
    inv = Inventory()
    print(inv.get_items())

    while True:
        inv.add_items(inv.adding())
        print()
        choice = input("Would you like to add more items ? Y/N\n> ")
        if choice.lower() == "n":
            break

    print(inv.get_items())

    inv.updating(1, 15, key="price")

    print(inv.get_items())

    print(inv.get_items(id=2))
    print(inv.get_items(id=2, key="name"))


if __name__ == "__main__":
    main()
