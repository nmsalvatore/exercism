"""Functions to keep track and alter inventory."""


def create_inventory(items):
    """Create a dict that tracks the amount (count) of each element on the `items` list."""
    inventory = {}

    for item in items:
        if item not in inventory:
            inventory[item] = items.count(item)

    return inventory


def add_items(inventory, items):
    """Add or increment items in inventory using elements from the items `list`."""
    for item in items:
        if item in inventory:
            inventory[item] += 1
        else:
            inventory[item] = 1

    return inventory


def decrement_items(inventory, items):
    """Decrement items in inventory using elements from the `items` list."""
    for item in items:
        if item in inventory and inventory[item] > 0:
            inventory[item] -= 1

    return inventory


def remove_item(inventory, item):
    """Remove item from inventory if it matches `item` string."""
    inventory.pop(item, item)
    return inventory


def list_inventory(inventory):
    """Create a list containing all (item_name, item_count) pairs in inventory."""
    inventory_list = []

    for item, count in inventory.items():
        if count > 0:
            inventory_list.append((item, count))

    return inventory_list
