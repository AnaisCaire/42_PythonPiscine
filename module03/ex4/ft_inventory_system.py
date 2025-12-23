# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_inventory_system.py                             :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: anaiscaire <anaiscaire@student.42.fr>      +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/12/23 09:41:18 by anaiscaire        #+#    #+#              #
#    Updated: 2025/12/23 13:17:00 by anaiscaire       ###   ########.fr        #
#                                                                              #
# **************************************************************************** #


def get_inventory_stats(inventory):
    """
    Calculates total value and total item count for any given inventory.
    """
    total_val = 0
    total_items = 0

    for details in inventory.values():
        total_val += details["qty"] * details["price"]
        total_items += details["qty"]
    return total_val, total_items


def DictionarySystem():
    """
    Iventory Master so organize storage
    """
    alice_inv = {
        "sword": {"type": "weapon", "rarity": "rare", "qty": 1, "price": 500},
        "potion": {"type": "consumable", "rarity": "common", "qty": 5, "price": 50},
        "shield": {"type": "armor", "rarity": "uncommon", "qty": 1, "price": 200}
    }
    bob_inv = { "magic_ring": {"type": "ring", "rarity": "rare", "qty": 1, "price": 25}}
    print("=== Player Inventory System ===")
    print("\n=== Alice's Inventory ===")
    total = 0
    inv_val = 0
    item_count = 0
    for item, details in alice_inv.items():
        total = details["qty"] * details["price"]
        print(item, f"({details["type"]}, {details["rarity"]}):",
              f"{details["qty"]}x @ {details["price"]} gold each",
              f"= {total} gold")

    inv_val, item_count = get_inventory_stats(alice_inv)
    print(f"\nIventory value: {inv_val} gold")
    print(f"Item count: {item_count} items")

    category_count = {}
    for details in alice_inv.values():
        category = details["type"]
        category_count[category] = category_count.get(category, 0) + details["qty"]

    print("Categories: ", end="")
    first = False
    for cat, qty in category_count.items():
        if first is True:
            print(", ", end="")
        first = True
        print(f"{cat}({qty})", end="")

    target_qty = 2
    item_name = "potion"
    print()
    print(f"\n=== Transaction: Alice gives Bob {target_qty} {item_name}")
    if item_name in alice_inv and alice_inv[item_name]["qty"] >= target_qty:
        alice_inv[item_name]["qty"] -= target_qty
        if item_name in bob_inv:
            bob_inv[item_name]["qty"] += target_qty
        else:
            bob_inv.update(
                {
                    item_name: {
                        "type": alice_inv[item_name]["type"],
                        "rarity": alice_inv[item_name]["rarity"],
                        "qty": target_qty,
                        "price": alice_inv[item_name]["price"]
                    }
                }
            )
        print("Transaction successful!")
    print("\n=== Updated Inventories ===")
    print(f"Alice {item_name}: {alice_inv[item_name]["qty"]}")
    print(f"Bob {item_name}: {bob_inv[item_name]["qty"]}")

    print("\n=== Inventory Analytics ===")

    # Get values for both
    a_val, a_count = get_inventory_stats(alice_inv)
    b_val, b_count = get_inventory_stats(bob_inv)

    if a_val > b_val:
        print(f"Most valuable player: Alice ({a_val} gold)")
    elif b_val > a_val:
        print(f"Most valuable player: Bob ({b_val} gold)")
    else:
        print(f"It's a tie! Both have {a_val} gold")

    if a_count > b_count:
        print(f"Most items: Alice ({a_count} items)")
    elif b_count > a_count:
        print(f"Most items: Bob ({b_count} items)")
    else:
        print(f"It's a tie! Both have {a_val} items")

    rare_lst = []
    for item, details in alice_inv.items():
        if details["rarity"] == "rare":
            rare_lst.append(item)
    for item, details in bob_inv.items():
        if details["rarity"] == "rare" and item not in rare_lst:
            rare_lst.append(item)

    print("Rarest items: ", end="")
    first = True
    for i in rare_lst:
        if first is True:
            print(f"{i}", end="")
            first = False
        else:
            print(f", {i}", end="")
    print()

if __name__ == "__main__":
    DictionarySystem()
