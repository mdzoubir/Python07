from ex0.CreatureCard import CreatureCard
from ex0.Card import Rarity


def main() -> None:
    print()
    print("=== DataDeck Card Foundation ===")
    print()
    print("Testing Abstract Base Class Design:")
    print()

    try:
        dragon = CreatureCard("Fire Dragon", 5, Rarity.LEGENDARY.value, 7, 5)
        print("CreatureCard Info:")
        print(dragon.get_card_info())
        print()

        mana = 6
        print(f"Playing {dragon.name} with {mana} mana available:")
        print(f"Playable: {dragon.is_playable(mana)}")
        if dragon.is_playable(mana):
            print(f"Play result: {dragon.play({})}")
        print()

        target_name = "Goblin Warrior"
        print(f"{dragon.name} attacks {target_name}:")
        print(f"Attack result: {dragon.attack_target(target_name)}")
        print()

        mana = 3
        print(f"Testing insufficient mana ({mana} available):")
        print(f"Playable: {dragon.is_playable(mana)}")
        print()

        print("Abstract pattern successfully demonstrated!")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
