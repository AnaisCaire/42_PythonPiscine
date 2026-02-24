

def spell_combiner(spell1: callable, spell2: callable) -> callable:
    """
    • Return a new function that calls both spells with the same arguments
    • The combined spell should return a tuple of both results
    • Example: combined = spell_combiner(fireball, heal)
    """
    def combined_spell(*args, **kwargs):
        """ we use *args to make sure if a spell requires more arguments,
        that they are passed down."""
        return1 = spell1(*args, **kwargs)
        return2 = spell2(*args, **kwargs)
        result = (return1, return2)
        return result
    # Return the inner function ITSELF (no parentheses!)
    return combined_spell


def power_amplifier(base_spell: callable, multiplier: int) -> callable:
    """
    • Return a new function that multiplies the base spell’s
        result by multiplier
    • Assume base spell returns a number (damage, healing, etc.)
    • Example: mega_fireball = power_amplifier(fireball, 3)
    """
    def multiplication(*args, **kwargs):
        base_spell_num = base_spell(*args, **kwargs)
        return base_spell_num * multiplier

    return multiplication


def conditional_caster(condition: callable, spell: callable) -> callable:
    """
    • Return a function that only casts the spell if condition returns True
    • If condition fails, return "Spell fizzled"
    • Both condition and spell receive the same arguments
    """
    def condition_spell(*args, **kwargs):
        condition_bool = condition(*args, **kwargs)
        if condition_bool:
            spell_res = spell(*args, **kwargs)
            return spell_res
        else:
            return "Spell fizzled"

    return condition_spell


def spell_sequence(spells: list[callable]) -> callable:
    """
    • Return a function that casts all spells in order
    • Each spell receives the same arguments
    • Return a list of all spell results
    """
    def cast_sorted(*args, **kwargs):
        result = []
        for spell in spells:
            result.append(spell(*args, **kwargs))
        return result
    return cast_sorted


if __name__ == "__main__":

    print(" === First-class citizenship === ")
    # Simple spells for testing

    def fire(target):
        return f"Fireball hits {target}"

    def heal(target):
        return f"Heals {target}"

    def water(target):
        return f"{target} was splashed by water by someone"

    print("\nTesting spell combiner...")
    combine = spell_combiner(fire, heal)
    result = combine("Dragon")
    print("Combined spell result:", result)

    # test multiplier
    print("\nTesting multiplier...")

    def base_spell(num: int):
        return num

    mega_fireball = power_amplifier(base_spell, 3)
    res = mega_fireball(15)
    print("Starting value:", base_spell(15),
          "\nAfter amplifier:", res)

    # conditional caster
    print("\nTesting conditional caster...")

    def is_alive(health: int, name: str) -> bool:

        if health > 2:
            print(f"{name} is alive!")
            return True
        print(f"{name} is dead")
        return False

    def trade_spell(health: int, name: str):
        return f"{name} trades {health} health points to someone!"

    dragon_spell_test = conditional_caster(is_alive, trade_spell)
    res = dragon_spell_test(2, "Dragon")
    print("health too low means:", res)
    res_yes = dragon_spell_test(12, "Dragona")
    print("Health is fine!:", res_yes)

    # spell sequence
    print("\nTesting spell sequence function...")
    spells = [fire, heal, water]
    combo_spell = spell_sequence(spells)
    result = combo_spell("Goblin")
    for i, res in enumerate(result, start=1):
        print(f"Spell {i}: {res}")
