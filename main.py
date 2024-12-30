from inventory import Inventory


def main():
    inv = Inventory()
    print(inv.get_items())
    inv.add_items(inv.adding())
    print(inv.get_items())


if __name__ == "__main__":
    main()
