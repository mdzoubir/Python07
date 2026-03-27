from ex0.Card import Rarity
from ex4.TournamentCard import TournamentCard
from ex4.TournamentPlatform import TournamentPlatform


def main() -> None:
    print("=== DataDeck Tournament Platform ===")
    print("Registering Tournament Cards...")
    dragon = TournamentCard(
        "Fire Dragon", 5, Rarity.LEGENDARY.value, 7, 5, 1200
    )
    wizard = TournamentCard(
        "Ice Wizard", 4, Rarity.RARE.value, 5, 6, 1150
    )
    platform = TournamentPlatform()
    dragon_id = platform.register_card(dragon)
    wizard_id = platform.register_card(wizard)

    print(f"{dragon.name} (ID: {dragon_id}):")
    print("- Interfaces: [Card, Combatable, Rankable]")
    print(f"- Rating: {dragon.rating}")
    print(f"- Record: {dragon.wins}-{dragon.losses}")
    print(f"{wizard.name} (ID: {wizard_id}):")
    print("- Interfaces: [Card, Combatable, Rankable]")
    print(f"- Rating: {wizard.rating}")
    print(f"- Record: {wizard.wins}-{wizard.losses}")

    print("Creating tournament match...")
    result = platform.create_match(dragon_id, wizard_id)
    print(f"Match result: {result}")
    print("Tournament Leaderboard:")
    for i in platform.get_leaderboard():
        print(
            f"{i['rank']}. {i['name']} - "
            f"Rating: {i['rating']} ({i['record']})"
        )
    print("Platform Report:")
    print(platform.generate_tournament_report())
    print("=== Tournament Platform Successfully Deployed! ===")
    print("All abstract patterns working together harmoniously!")


if __name__ == "__main__":
    main()
