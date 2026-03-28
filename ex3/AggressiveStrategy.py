from ex3.GameStrategy import GameStrategy
from typing import Dict, List
import random


class AggressiveStrategy(GameStrategy):
    def execute_turn(self, hand: List, battlefield: List) -> Dict:
        cards_played = []
        mana_used = 0
        damage_dealt = 0
        sorted_hand = sorted(hand, key=lambda c: c.cost)
        available_mana = random.randint(5, 10)
        for card in sorted_hand:
            if card.cost <= available_mana:
                cards_played.append(card.name)
                mana_used += card.cost
                available_mana -= card.cost
                if card.name == "Goblin Warrior":
                    damage_dealt += 5
                elif "Bolt" in card.name:
                    damage_dealt += 3
                elif hasattr(card, 'attack'):
                    damage_dealt += card.attack
        for card in battlefield:
            if hasattr(card, 'attack'):
                damage_dealt += card.attack
        return {
            'cards_played': cards_played,
            'mana_used': mana_used,
            'targets_attacked': ['Enemy Player'],
            'damage_dealt': damage_dealt
        }

    def get_strategy_name(self) -> str:
        return "AggressiveStrategy"

    def prioritize_targets(self, available_targets: List) -> List:
        return available_targets
