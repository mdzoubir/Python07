from ex2.EliteCard import EliteCard
from ex0.Card import Rarity


def main() -> None:
    print()
    print("=== DataDeck Ability System ===")
    print()

    print("EliteCard capabilities:")
    print("- Card: ['play', 'get_card_info', 'is_playable']")
    print("- Combatable: ['attack', 'defend', 'get_combat_stats']")
    print("- Magical: ['cast_spell', 'channel_mana', 'get_magic_stats']")
    print()

    warrior = EliteCard("Arcane Warrior", 6, Rarity.LEGENDARY.value, 5, 4)
    print(f"Playing {warrior.name} (Elite Card):")
    print()

    print("Combat phase:")
    print(f"Attack result: {warrior.attack('Enemy')}")
    print(f"Defense result: {warrior.defend(5)}")
    print()

    print("Magic phase:")
    targets = ['Enemy1', 'Enemy2']
    print(f"Spell cast: {warrior.cast_spell('Fireball', targets)}")
    print(f"Mana channel: {warrior.channel_mana(3)}")

    print()
    print("Multiple interface implementation successful!")


if __name__ == "__main__":
    main()
