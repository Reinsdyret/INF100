# inventory.py
stuff = {"rope": 1, "torch": 6, "gold coin": 42, "dagger": 1, "arrow": 12}


def displayInventory(inventory):
    print("Inventory:")
    item_total = 0
    for k, v in inventory.items():
        print(f"{v} {k}")
        item_total += v
    return item_total


# check
print(displayInventory(stuff))
