from ex4.TournamentCard import TournamentCard
from typing import Dict, List


class TournamentPlatform:
    def __init__(self) -> None:
        self.cards = {}
        self.matches = []

    def register_card(self, card: TournamentCard) -> str:
        name_parts = card.name.lower().split()
        card_id = f"{name_parts[-1]}_001"
        self.cards[card_id] = card
        return card_id

    def create_match(self, card1_id: str, card2_id: str) -> Dict:
        card1 = self.cards[card1_id]
        card2 = self.cards[card2_id]
        if card1.attack_power >= card2.attack_power:
            winner, loser = card1, card2
            winner_id, loser_id = card1_id, card2_id
        else:
            winner, loser = card2, card1
            winner_id, loser_id = card2_id, card1_id
        winner.update_wins(1)
        loser.update_losses(1)
        result = {
            'winner': winner_id,
            'loser': loser_id,
            'winner_rating': winner.rating,
            'loser_rating': loser.rating
        }
        self.matches.append(result)
        return result

    def get_leaderboard(self) -> List[Dict]:
        cards = sorted(self.cards.values(),
                       key=lambda c: c.rating, reverse=True)
        return [
            {
                'rank': i,
                'name': c.name,
                'rating': c.rating,
                'record': f"{c.wins}-{c.losses}"
            }
            for i, c in enumerate(cards, 1)
        ]

    def generate_tournament_report(self) -> Dict:
        ratings = [c.rating for c in self.cards.values()]
        avg = sum(ratings) // len(ratings) if ratings else 0
        return {
            'total_cards': len(self.cards),
            'matches_played': len(self.matches),
            'avg_rating': avg,
            'platform_status': 'active'
        }
