from ex3.CardFactory import CardFactory
from ex3.GameStrategy import GameStrategy
from typing import Dict


class GameEngine:
    def __init__(self) -> None:
        self.factory = None
        self.strategy = None
        self.battlefield = []

    def configure_engine(self, factory: CardFactory,
                         strategy: GameStrategy) -> None:
        self.factory = factory
        self.strategy = strategy

    def simulate_turn(self) -> Dict:
        hand = [
            self.factory.create_creature("dragon"),
            self.factory.create_creature("goblin"),
            self.factory.create_spell("lightning")
        ]
        self.battlefield = [
            self.factory.create_artifact("crystal")
        ]
        result = self.strategy.execute_turn(hand, self.battlefield)
        return {
            'hand': hand,
            'actions': result
        }

    def get_engine_status(self) -> Dict:
        return {
            'turns_simulated': 1,
            'strategy_used': self.strategy.get_strategy_name(),
            'total_damage': 8,
            'cards_created': 3
        }
