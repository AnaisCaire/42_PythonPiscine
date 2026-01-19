
def ft_seed_inventory(seed_type: str, quantity: int, unit: str):
    if unit == "packets":
        unit = "packets available"
    elif unit == "grams":
        unit = "grams total"
    elif unit == "area":
        unit = "square meters"
    else:
        print("Unknown unit type")
        return
    print(seed_type.capitalize(), "seeds:", quantity, unit)
