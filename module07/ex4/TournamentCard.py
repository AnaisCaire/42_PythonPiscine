from ex0.Card import Card
from ex2.Combatable import Combatable
from ex4.Rankable import Rankable


class TournamentCard(Card, Combatable, Rankable):
    """Card with tournament capabilities"""
    def __init__(self, name, cost, rarity, attack_val: int):
        super().__init__(name, cost, rarity)
        self.attack_val = attack_val
        # The ranking class values
        self._wins = 0
        self._losses = 0
        self._rating = 1200

    def play(self, game_state: dict) -> dict:
        """Process play and inject tournament rating into the state."""
        super().play(game_state)
        game_state.update({
                "tournament_ready": True,
                "current_rating": self._rating
            })
        return game_state

    def attack(self, target) -> dict:
        """Attack a target."""
        return {
            "attacker": self.name,
            "target": target,
            "attack_val": self.attack_val
        }

    def defend(self, incoming_damage: int) -> dict:
        """Defend against incoming damage."""
        return {
            "defender": self.name,
            "incoming_damage": incoming_damage
        }

    def get_combat_stats(self) -> dict:
        """Return combat-related stats."""
        return {"damage given": self.attack_val}

    def calculate_rating(self) -> int:
        """Calculate and return current rating."""
        return self._rating

    def update_wins(self, wins: int) -> None:
        """Update wins count."""
        self._wins += wins

    def update_losses(self, losses: int) -> None:
        """Update losses count."""
        self._losses += losses


    def get_rank_info(self) -> dict:
        """Return ranking info as a dict."""
        return {"rating": self._rating,
                "record": f"{self._wins}-{self._losses}"}

    def get_tournament_stats(self) -> dict:
        """Combined summary for the platform report."""
        stats = self.get_rank_info()
        stats.update({"name": self.name})
        return stats
