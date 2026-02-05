
import alchemy.transmutation.advanced as advanced
import alchemy.transmutation.basic as basic
import alchemy.transmutation

print("\n=== Pathway Debate Mastery ===")
print("\nTesting Absolute Imports (from basic.py):")
print(f"Lead_to_gold(): {basic.lead_to_gold()}")
print(f"stone_to_gem(): {basic.stone_to_gem()}")
print("\nTesting Relative Imports (from advanced.py):")
print(f"philosophers_stone(): {advanced.philosophers_stone()}")
print(f"elixir_of_life(): {advanced.elixir_of_life()}")
print("\nTesting Package Access:")
# its package level because we call transmutation and not trans...advanced
print(f"alchemy.transmutation.lead_to_gold(): "
      f"{alchemy.transmutation.lead_to_gold()}")
print(f"alchemy.transmutation.philosophers_stone():"
      f"{alchemy.transmutation.philosophers_stone()}")
print("\nBoth pathways work! Absolute: clear, Relative: concise")
