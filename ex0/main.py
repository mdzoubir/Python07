from ex0.CreatureCard import CreatureCard
from ex0.Card import Rarity


def main() -> None:
    print()
    print("=== DataDeck Card Foundation ===")
    print()
    print("Testing Abstract Base Class Design:")
    print()
    dragon = CreatureCard("Fire Dragon", 5, Rarity.LEGENDARY.value, 7, 5)
    print("CreatureCard Info:")
    print(dragon.get_card_info())
    print()
    game_state = {'mana': 6}
    print(
        f"Playing {dragon.name} with {game_state['mana']} mana available:"
    )
    print(f"Playable: {dragon.is_playable(game_state['mana'])}")
    if dragon.is_playable(game_state['mana']):
        print(f"Play result: {dragon.play(game_state)}")
    print()
    target_name = "Goblin Warrior"
    print(f"{dragon.name} attacks {target_name}:")
    print(f"Attack result: {dragon.attack_target(target_name)}")
    print()
    game_state['mana'] = 3
    print(f"Testing insufficient mana ({game_state['mana']} available):")
    print(f"Playable: {dragon.is_playable(game_state['mana'])}")
    print()
    print("Abstract pattern successfully demonstrated!")


if __name__ == "__main__":
    main()
