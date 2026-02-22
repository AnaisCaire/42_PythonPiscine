

def artifact_sorter(artifacts: list[dict]) -> list[dict]:
    """
    • Use sorted() with a lambda to sort by ’power’ level (descending)
    • Each artifact is a dict: {’name’: str, ’power’: int, ’type’: str}
    • Return the sorted list
    """
    artifact_sort = sorted(artifacts, key=lambda x: x["power"], reverse=True)
    return artifact_sort


def power_filter(mages: list[dict], min_power: int) -> list[dict]:
    """
    Use filter() with a lambda to find mages with power >= min_power
    """
    power_filt = list(filter(lambda x: x["power"] >= min_power, mages))
    return power_filt


def spell_transformer(spells: list[str]) -> list[str]:
    """
    • Use map() with a lambda to add "* " prefix and " *" suffix
    • Input: list of spell names (strings)
    """
    new_spell = list(map(lambda x: "* " + x + " *", spells))
    return new_spell


def mage_stats(mages: list[dict]) -> dict:
    """
    • Use lambdas with max(), min(), and sum() to find:
    • Most powerful mage’s power level
    • Least powerful mage’s power level
    • Average power level (rounded to 2 decimals)
    • Return dict: {’max_power’: int, ’min_power’: int, ’avg_power’: float}
    """
    max_power = max(mages, key=lambda x: x['power'])['power']
    min_power = min(mages, key=lambda x: x['power'])['power']
    avg_power = round(sum(map(lambda x: x['power'], mages)) / len(mages), 2)
    stats = {"max_power": max_power, "min_power": min_power, "avg_power": avg_power}
    return stats


if __name__ == "__main__":
    print("=== The Lambda Sanctum ===\n")
    # Lambda Sanctum Test Data
    artifacts = [{'name': 'Fire Staff', 'power': 107, 'type': 'focus'}, {'name': 'Light Prism', 'power': 93, 'type': 'accessory'}, {'name': 'Earth Shield', 'power': 75, 'type': 'accessory'}, {'name': 'Fire Staff', 'power': 87, 'type': 'focus'}]
    mages = [{'name': 'Nova', 'power': 81, 'element': 'earth'}, {'name': 'Jordan', 'power': 69, 'element': 'water'}, {'name': 'Kai', 'power': 50, 'element': 'lightning'}, {'name': 'Riley', 'power': 89, 'element': 'water'}, {'name': 'Sage', 'power': 67, 'element': 'ice'}]
    spells = ['freeze', 'blizzard', 'darkness', 'lightning']
    sorted_artifacts = artifact_sorter(artifacts)
    for i, artifact in enumerate(sorted_artifacts, start=1):
        print(i, artifact['name'], f"(power: {artifact['power']})")
    print()
    min_power = 69
    mages_power_filter = power_filter(mages, min_power)
    print("Testing power filtering function...")
    print(f"Theses mages have more than the minimum power recommended: {min_power}")
    for mage in mages_power_filter:
        print(f"{mage['name']} -> ({mage['power']})")
    print()
    spell_change = spell_transformer(spells)
    print("Testing the spell changing convention...")
    for spel in spell_change:
        print(spel)
    print()
    new_dict_power = mage_stats(mages)
    print("Giving the mage power stats...")
    for key, value in new_dict_power.items():
        print(f"{key}: {value}%")
