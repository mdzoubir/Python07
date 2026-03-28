from ex0.Card import Card
from ex2.Combatable import Combatable
from ex4.Rankable import Rankable


class TournamentCard(Card, Combatable, Rankable):
    def __init__(self, name: str, cost: int, rarity: str, attack_power: int,
                 health: int, base_rating: int = 1000) -> None:
        Card.__init__(self, name, cost, rarity)
        self.attack_power = attack_power
        self.health = health
        self.wins = 0
        self.losses = 0
        self.rating = base_rating

    def play(self, game_state: dict) -> dict:
        game_state.setdefault('history', []).append(self.name)
        return {
            'card_played': self.name,
            'mana_used': self.cost,
            'type': 'Tournament Card'
        }

    def attack(self, target: str) -> dict:
        return {
            'attacker': self.name,
            'target': target,
            'damage': self.attack_power
        }

    def defend(self, incoming_damage: int) -> dict:
        return {
            'defender': self.name,
            'damage_taken': incoming_damage
        }

    def get_combat_stats(self) -> dict:
        return {
            'attack_power': self.attack_power,
            'health': self.health
        }

    def calculate_rating(self) -> int:
        return self.rating

    def update_wins(self, wins: int) -> None:
        self.wins += wins
        self.rating += 16

    def update_losses(self, losses: int) -> None:
        self.losses += losses
        self.rating -= 16

    def get_rank_info(self) -> dict:
        return {
            'name': self.name,
            'rating': self.rating,
            'wins': self.wins,
            'losses': self.losses
        }

    def get_tournament_stats(self) -> dict:
        return {
            'name': self.name,
            'rating': self.rating,
            'record': f"{self.wins}-{self.losses}",
            'interfaces': ['Card', 'Combatable', 'Rankable']
        }
