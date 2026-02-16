from ex4.TournamentCard import TournamentCard
from ex4.TournamentPlatform import TournamentPlatform


def main():
    print("=== DataDeck Tournament Platform ===")
    platform = TournamentPlatform()

    print("Registering Tournament Cards...")

    dragon = TournamentCard("Fire Dragon", 5, "Legendary", 10)
    wizard = TournamentCard("Ice Wizard", 4, "Rare", 8)

    id1 = platform.register_card(dragon)
    id2 = platform.register_card(wizard)

    for cid in [id1, id2]:
        card = platform._registry[cid]
        info = card.get_rank_info()
        print(f"{card.name} (ID: {cid}):")
        print("- Interfaces: [Card, Combatable, Rankable]")
        print(f"- Rating: {info['rating']}")
        print(f"- Record: {info['record']}")

    print("\nCreating tournament match...")
    match_result = platform.create_match(id1, id2)
    print(f"Match result: {match_result}")

    print("\nTournament Leaderboard:")
    leaderboard = platform.get_leaderboard()
    for entry in leaderboard:
        print(entry)

    print("\nPlatform Report:")
    report = platform.generate_tournament_report()
    print(report)

    print("\n=== Tournament Platform Successfully Deployed! ===")
    print("All abstract patterns working together harmoniously!")


if __name__ == "__main__":
    main()
