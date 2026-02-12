from ex0.Card import Card


class SpellCard(Card):

    def __init__(self, name: str, cost: int, rarity: str, effect_type: str):
        super().__init__(name, cost, rarity)
        self.effect_type = effect_type

    def play(self, game_state: dict) -> dict:
        """ The play of a spell card """
        game_state = {
            "card_played": self.name,
            "mana_used": self.cost,
            "effect_type": self.effect_type}
        return game_state


    def resolve_effect(self, targets: list) -> dict:
        """ the impact of the spell played"""
        return {
            "spell": self.name,
            "effect_type": self.effect_type,
            "targets_affected": targets,
            "resolved": True}