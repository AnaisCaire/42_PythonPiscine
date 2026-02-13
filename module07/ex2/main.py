from ex0.Card import Card
from ex2.Combatable import Combatable
from ex2.Magical import Magical
from ex2.EliteCard import EliteCard

if __name__ == "__main__":
    print("\n=== DataDeck Ability System ===\n")

    print("Elite card capabilities:")
    elite_card = EliteCard(
        name = "Arcane Warrior",
        cost = 10,
        rarity = "rare",
        damage_done = 5,
        health = 10
    )
    # methods = [m for m in dir(EliteCard) if not m.startswith("_")]
    # print(methods)
    print(f"Card: ['play', 'get_card_info', 'is_playable']")
    print(f"Combatable: ['attack', 'defend', 'get_combat_stats']")
    print(f"Magical: ['cast_spell', 'channel_mana', 'get_magic_stats']")

    print(f"\nPlaying {elite_card.name} (Elite Card):")
    
    print("\nCombat phase:")
    print(f"Attack result: {elite_card.attack('Goblin')}")
    print(f"Defense results: {elite_card.defend(5)}")
    
    print("\nMagical phase:")
    print(f"Spell cast: {elite_card.cast_spell(
        "Fireball", 
        targets = ['Dragona', 'Vella'])}")
    print(f"Mana channeled: {elite_card.channel_mana(4)}")
    
    print("\nMultiple interface implementation successful!")