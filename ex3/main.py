from ex3.FantasyCardFactory import FantasyCardFactory
from ex3.AggressiveStrategy import AggressiveStrategy
from ex3.GameEngine import GameEngine


def main():
    print("=== DataDeck Game Engine ===\n")
    factory = FantasyCardFactory()
    strategy = AggressiveStrategy()
    print("Configuring Fantasy Card Game...")
    print("Factory: FantasyCardFactory")
    print("Strategy: AggressiveStrategy")
    print(f"Available types: {factory.get_supported_types()}\n")
    engine = GameEngine()
    engine.configure_engine(factory, strategy)
    print("Simulating aggressive turn...")
    turn_data = engine.simulate_turn()
    hand = turn_data['hand']
    hand_str = ", ".join([f"{c.name} ({c.cost})" for c in hand])
    print(f"Hand: [{hand_str}]\n")
    print("Turn execution:")
    print("Strategy: AggressiveStrategy")
    print(f"Actions: {turn_data['actions']}\n")
    print("Game Report:")
    print(engine.get_engine_status())
    print("\nAbstract Factory + Strategy Pattern: "
          "Maximum flexibility achieved!")


if __name__ == "__main__":
    main()
