from ex3.GameStrategy import GameStrategy


class AggressiveStrategy(GameStrategy):
    """Strategy that prioritizes high damage and low-cost cards."""

    def execute_turn(self, hand: list, battlefield: list) -> dict:
        """
        Simplified aggressive turn: play cards and attack with battlefield.
        """
        mana_budget = 10
        played_names = []

        # Play cards from hand until no more mana
        for card in sorted(hand, key=lambda c: c.cost):
            if card.cost <= mana_budget:
                mana_budget -= card.cost
                played_names.append(card.name)
        attackers = [card.name for card in battlefield]
        return {
            "strategy": self.get_strategy_name(),
            "cards_played": played_names,
            "mana_used": 10 - mana_budget,
            "targets_attacked": ["Enemy Player"],
            "battlefield_attackers": attackers,
            "damage_dealt": (len(attackers) * 2) + 5
        }

    def get_strategy_name(self) -> str:
        return "AggressiveStrategy"

    def prioritize_targets(self, available_targets: list) -> list:
        """
        Targets enemy player directly first
        by making sure the Enemy Player is the first target in the list.
        """
        if "Enemy Player" in available_targets:
            available_targets.remove("Enemy Player")
            available_targets.insert(0, "Enemy Player")
        return available_targets
