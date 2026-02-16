
from ex2.EliteCard import EliteCard

if __name__ == "__main__":
    print("\n=== DataDeck Ability System ===\n")

    print("Elite card capabilities:")
    elite_card = EliteCard(
        name="Arcane Warrior",
        cost=10,
        rarity="rare",
        damage_done=5,
        health=10
    )
    # methods = [m for m in dir(EliteCard) if not m.startswith("_")]
    # print(methods)
    print("Card: ['play', 'get_card_info', 'is_playable']")
    print("Combatable: ['attack', 'defend', 'get_combat_stats']")
    print("Magical: ['cast_spell', 'channel_mana', 'get_magic_stats']")

    print(f"\nPlaying {elite_card.name} (Elite Card):")

    print("\nCombat phase:")
    print(f"Attack result: {elite_card.attack('Goblin')}")
    print(f"Defense results: {elite_card.defend(5)}")

    print("\nMagical phase:")
    spell_cast = elite_card.cast_spell("Fireball", ['Dragona', 'Vella'])
    print(f"Spell cast: {spell_cast}")
    print(f"Mana channeled: {elite_card.channel_mana(4)}")

    print("\nMultiple interface implementation successful!")
