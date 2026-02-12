from ex0.CreatureCard import CreatureCard
from ex1.SpellCard import SpellCard
from ex1.ArtifactCard import ArtifactCard
from ex1.Deck import Deck

if __name__ == "__main__":
    print("=== DataDeck Deck Builder ===")
    
    # 1. Initialize Deck
    my_deck = Deck()
    
    # 2. Add different card types
    my_deck.add_card(CreatureCard("Fire Dragon", 5, "Legendary", 7, 5))
    my_deck.add_card(SpellCard("Lightning Bolt", 3, "Common", "damage"))
    my_deck.add_card(ArtifactCard("Mana Crystal", 2, "Rare", 3, "Permanent: +1 mana per turn"))
    
    # 3. Show Stats [cite: 305-306]
    print("\nBuilding deck with different card types...")
    stats = my_deck.get_deck_stats()
    print(f"Deck stats: {stats}")
    
    # 4. Demonstrate Drawing and Playing
    print("\nDrawing and playing cards:")
    my_deck.shuffle()
    
    try:
        for _ in range(3):
            card = my_deck.draw_card()
            print(f"Drew: {card.name} ({type(card).__name__})")
            # This is where your return value logic will be visible:
            print(f"Play result: {card.play({})}") 
    except IndexError as e:
        print(f"Error: {e}")

    print("\nPolymorphism in action: Same interface, different card behaviors!")