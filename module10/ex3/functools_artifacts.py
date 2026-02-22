from functools import reduce, partial, lru_cache
import operator
# import time


def spell_reducer(spells: list[int], operation: str) -> int:
    """
    • Use functools.reduce to combine all spell powers
    • Support operations: "add", "multiply", "max", "min"
    • Use operator module functions (add, mul, etc.)
    • Return the final reduced value
    """
    try:
        if operation == "add":
            r = reduce(operator.add, spells)
        if operation == "multiply":
            r = reduce(operator.mul, spells)
        if operation == "max":
            r = reduce(lambda x, y: x if x > y else y, spells)
        if operation == "min":
            r = reduce(lambda x, y: x if x < y else y, spells)
        return r
    except Exception:
        return "supported operations are add, multiply, max, min"


def partial_enchanter(base_enchantment: callable) -> dict[str, callable]:
    """
    • Take a base enchantment function that needs (power, element, target)
    • Use functools.partial to create specialized versions
    • Return dict with keys: ’fire_enchant’, ’ice_enchant’, ’lightning_enchant’
    • Each should be a partial with power=50 and the respective element
    """
    enchant_dict = {
        "fire_enchant": partial(base_enchant, 50, "fire"),
        "ice_enchant": partial(base_enchant, 50, "ice"),
        "lightning_enchant": partial(base_enchant, 50, "lightning")
    }
    return enchant_dict


@lru_cache(maxsize=None)
def memoized_fibonacci(n: int) -> int:
    """
    • Use functools.lru_cache decorator for memoization
    • Implement fibonacci sequence calculation
    • The cache should improve performance for repeated calls
    • Return the nth fibonacci number
    """
    if n < 2:
        return n
    return memoized_fibonacci(n-1) + memoized_fibonacci(n-2)


def spell_dispatcher() -> callable:
    """
    • Use functools.singledispatch to create a spell system
    • Handle different types: int (damage spell), str (enchantment), list (multi-cast)
    • Return the dispatcher function
    • Each type should have appropriate spell behavior
    """
    pass


if __name__ == "__main__":
    print(" === Functools Treasures === \n")
    print("Testing spell reducer...")
    spell_powers: list = [42, 56, 78, 12, 4, 99, 27]
    print("Sum:", spell_reducer(spell_powers, "add"))
    print("Product:", spell_reducer(spell_powers, "multiply"))
    print("Max:", spell_reducer(spell_powers, "max"))
    print("Min:", spell_reducer(spell_powers, "min"))
    print("error test:", spell_reducer(spell_powers, "maAx"))

    print("\nTesting partial enchanter technique...")

    def base_enchant(power, element, target):
        return f"{element} with: {power} of power attacked {target}"

    enchant_dict = partial_enchanter(base_enchant)
    for key, value in enchant_dict.items():
        print(f"{key} ->", value("Gobling"))

    print("\nTesting memoized fibonacci...")
    print("Fib(10):", memoized_fibonacci(10))
    print("Fib(15):", memoized_fibonacci(15))

"""     begin = time.time()
    memoized_fibonacci(40)
    end = time.time()
    print("total time:", end - begin) """
