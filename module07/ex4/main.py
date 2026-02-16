from ex4.TournamentCard import TournamentCard
from ex4.TournamentPlatform import TournamentPlatform

def main():
    print("=== DataDeck Tournament Platform ===")
    platform = TournamentPlatform()

    # 1. Registering Tournament Cards
    print("Registering Tournament Cards...")
    
    dragon = TournamentCard("Fire Dragon", 5, "Legendary", 10)
    wizard = TournamentCard("Ice Wizard", 4, "Rare", 8)
    
    # We register them and get their unique IDs
    id1 = platform.register_card(dragon)
    id2 = platform.register_card(wizard)
    
    # Display individual card status as per example
    for cid in [id1, id2]:
        card = platform._registry[cid]
        info = card.get_rank_info()
        print(f"{card.name} (ID: {cid}):")
        print(f"- Interfaces: [Card, Combatable, Rankable]")
        print(f"- Rating: {info['rating']}")
        print(f"- Record: {info['record']}")

    # 2. Creating tournament match
    print("\nCreating tournament match...")
    match_result = platform.create_match(id1, id2)
    print(f"Match result: {match_result}")

    # 3. Tournament Leaderboard
    print("\nTournament Leaderboard:")
    leaderboard = platform.get_leaderboard()
    for entry in leaderboard:
        print(entry)

    # 4. Platform Report
    print("\nPlatform Report:")
    report = platform.generate_tournament_report()
    print(report)

    print("\n=== Tournament Platform Successfully Deployed! ===")
    print("All abstract patterns working together harmoniously!")

if __name__ == "__main__":
    main()