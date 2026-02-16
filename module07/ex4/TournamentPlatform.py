from ex4.TournamentCard import TournamentCard


class TournamentPlatform:
    """Platform management system for tournament cards."""
    def __init__(self):
        self._registry = {}
        self._match_count = 0

    def register_card(self, card: TournamentCard) -> str:
        """Register a card and return its assigned id."""
        # "Fire Dragon" -> "dragon" and Ice Wizard -> "wizard"
        base_name = card.name.lower().split()[1]
        # add numb
        count = len(self._registry) + 1
        # "dragon_1"
        card_id = f"{base_name}_{count}"
        self._registry[card_id] = card
        return card_id

    def create_match(self, card1_id: str, card2_id: str) -> dict:
        """Simulates a match between two registered cards."""
        c1 = self._registry[card1_id]
        c2 = self._registry[card2_id]

        if c1.attack_val >= c2.attack_val:
            winner, loser = c1, c2
            winner_id, loser_id = card1_id, card2_id
        else:
            winner, loser = c2, c1
            winner_id, loser_id = card2_id, card1_id

        winner.update_wins(1)
        loser.update_losses(1)

        winner._rating += 16
        loser._rating -= 16

        self._match_count += 1
        return {
            "winner": winner_id,
            "loser": loser_id,
            "winner_rating": winner.calculate_rating(),
            "loser_rating": loser.calculate_rating()
        }

    def get_leaderboard(self) -> list:
        """Return leaderboard data."""
        cards = list(self._registry.values())
        leaderboard = []
        for i, card in enumerate(cards, 1):
            info = card.get_rank_info()
            entry = f"{i}. {card.name} - Rating: {info['rating']}"
            "({info['record']})"
            leaderboard.append(entry)
        return leaderboard

    def generate_tournament_report(self) -> dict:
        """Generate a tournament report."""
        """Platform-level summary report."""
        all_ratings = [c.calculate_rating() for c in self._registry.values()]
        avg = sum(all_ratings) / len(all_ratings) if all_ratings else 0
        return {
            "total_cards": len(self._registry),
            "matches_played": self._match_count,
            "avg_rating": int(avg),
            "platform_status": "active"
        }
