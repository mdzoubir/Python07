import random
import math
from ex0.Card import Card
from typing import List


class Deck:

    def __init__(self):
        self.cards: List[Card] = []

    def add_card(self, card: Card) -> None:
        self.cards.append(card)

    def remove_card(self, card_name: str) -> bool:
        for card in self.cards:
            if card.name == card_name:
                self.cards.remove(card)
                return True
        return False

    def shuffle(self) -> None:
        random.shuffle(self.cards)

    def draw_card(self) -> Card:
        if not self.cards:
            raise IndexError("Draw from empty deck")
        return self.cards.pop(0)

    def get_deck_stats(self) -> dict:
        stats = {
            'total_cards': len(self.cards),
            'creatures': 0,
            'spells': 0,
            'artifacts': 0,
            'avg_cost': 0.0
        }
        if not self.cards:
            return stats

        total_cost = 0
        from ex0.CreatureCard import CreatureCard
        from ex1.SpellCard import SpellCard
        from ex1.ArtifactCard import ArtifactCard

        for card in self.cards:
            total_cost += card.cost
            if isinstance(card, CreatureCard):
                stats['creatures'] += 1
            elif isinstance(card, SpellCard):
                stats['spells'] += 1
            elif isinstance(card, ArtifactCard):
                stats['artifacts'] += 1

        stats['avg_cost'] = float(math.ceil(total_cost / len(self.cards)))
        return stats
