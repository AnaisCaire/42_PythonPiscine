
from ex0.CreatureCard import CreatureCard

if __name__ == "__main__":
    print("=== DataDeck Card Foundation ===")
    print("\nTesting Abstract Base Class Design:")
    print("\nCreatureCard Info:")
    dragon = CreatureCard(
        name="Fire Dragon",
        cost=5,
        rarity="Legendary",
        attack=7,
        health=5)
    print(dragon.get_card_info())

    print(f"\nPlaying {dragon.name} with 6 mana available:")
    print(f"Playable: {dragon.is_playable(6)}")
    print(f"Play result: {dragon.play({})}")

    print(f"\n{dragon.name} attacks Goblin Warrior:")
    print(f"Attack result: {dragon.attack_target(target='Goblin Warrior')}")

    print("\nTesting insufficient mana (3 available):")
    print(f"Playable: {dragon.is_playable(3)}")

    print("\nAbstract pattern successfully demonstrated!")
