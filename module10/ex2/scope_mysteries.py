
def mage_counter() -> callable:
    """
    Return a function that counts how many times it’s been called
    • Each call should return the current count (starting from 1)
    • The counter should persist between calls
    • Use closure to maintain state without global variables
    """
    count = 0

    def mage_activation():
        nonlocal count
        count += 1
        return count
    return mage_activation


def spell_accumulator(initial_power: int) -> callable:
    """
    • Return a function that accumulates power over time
    • Each call adds the given amount to the total power
    • Return the new total power after each addition
    • Start with initial_power as the base
    """
    def power_multiplier(given_amount: int):
        nonlocal initial_power
        initial_power += given_amount
        return initial_power
    return power_multiplier


def enchantment_factory(enchantment_type: str) -> callable:
    """
    • Return a function that applies the specified enchantment
    • The returned function takes an item name and returns enchanted description
    • Format: "enchantment_type item_name" (e.g., "Flaming Sword")
    • Each factory creates functions with different enchantment types
    """
    def enchantement_description(item_name: str):
        description = f"{enchantment_type} {item_name}"
        return description
    return enchantement_description


def memory_vault() -> dict[str, callable]:
    """
    • Return a dict with ’store’ and ’recall’ functions
    • ’store’ function: takes (key, value) and stores the memory
    • ’recall’ function: takes (key) and returns stored value or "Memory not found"
    • Use closure to maintain private memory storage    
    """


if __name__ == "__main__":
    print(" === Memory Depths === \n")
    print("Mage counter visualisation....")
    counting = mage_counter()
    for i in range(4):
        i = counting()
        print(f"function was called: {i} times")

    print("spell accumulator per activation...")
    spell = spell_accumulator(initial_power=11)
    for i in range(4):
        i = spell(16)
        print(f"+{i}% more")

    enchantment_types = ['Windy', 'Earthen', 'Flowing']
    items_to_enchant = ['Sword', 'Cloak', 'Wand', 'Staff']
    # making all possible combinations
    """     for types in enchantment_types:
            creating = enchantment_factory(types)
            for item in items_to_enchant:
                final = creating(item)
                print(final)
    """
    print("Testing enchantement factory...")
    enchantment = enchantment_factory('Golden')
    to_enchant = enchantment('Fireball')
    print(to_enchant)

    print("Memory vault")