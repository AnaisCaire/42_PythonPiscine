from ex3.GameEngine import GameEngine
from ex3.FantasyCardFactory import FantasyCardFactory
from ex3.AggressiveStrategy import AggressiveStrategy


def main():
    print("=== DataDeck Game Engine ==\n")

    # 1. Setup
    print("Configuring Fantasy Card Game...")
    factory = FantasyCardFactory()
    strategy = AggressiveStrategy()
    engine = GameEngine()
    engine.configure_engine(factory, strategy)

    # 2. Display Configuration
    status = engine.get_engine_status()
    print(f"Factory: {status['factory_name']}")
    print(f"Strategy: {status['strategy_name']}")
    print(f"Available types: {factory.get_supported_types()}")

    # 3. Prepare Hand for Display
    # We manually create a small hand to match your expected output
    hand = [
        factory.create_creature("dragon"),
        factory.create_creature("goblin warrior"),
        factory.create_spell("fire")
    ]

    print("\nSimulating aggressive turn...")
    hand_display = [f"{c.name} ({c.cost})" for c in hand]
    print(f"Hand: {hand_display}")

    # 4. Simulation Execution
    print("\nTurn execution:")
    turn_results = strategy.execute_turn(hand, [])
    print(f"Strategy: {strategy.get_strategy_name()}")
    print(f"Actions: {turn_results}")

    # 5. Final Report
    print("\nGame Report:")
    report = {
        "turns_simulated": 1,
        "strategy_used": strategy.get_strategy_name(),
        "total_damage": turn_results['damage_dealt'],
        "cards_created": len(hand)
    }
    print(report)
    print()
    print("Abstract Factory + Strategy Pattern: Maximum flexibility achieved!")


if __name__ == "__main__":
    main()
