
from .Card import Card
from .CreatureCard import CreatureCard

if __name__ == "__main__":

    dragon = CreatureCard(
        name="Fire Dragon",
        cost= 5,
        rarity="Legendary",
        attack=7,
        health=5)
    res = dragon.get_card_info()
    print(res)