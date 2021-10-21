inv = {"gold coin": 42, "rope": 1}
dragonLoot = ["gold coin", "dagger", "gold coin", "gold coin", "ruby"]


def displayInventory(inventory:dict) -> int:
    print("Inventory:")
    item_total = 0
    for k, v in inventory.items():
        print(f"{v} {k}")
        item_total += v
    return item_total


def addToInventory(inventory:dict, addedItems:list) -> dict:
    for i in range(len(addedItems)):
        if addedItems[i] in inventory:
            inventory[addedItems[i]] += 1
            continue
        inventory.update({addedItems[i] : 1})
    
    return inventory


inv = addToInventory(inv, dragonLoot)
total = displayInventory(inv)
print("Total number of items:", total)
