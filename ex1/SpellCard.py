from ex0.Card import Card


class SpellCard(Card):
    def __init__(self, name: str, cost: int, rarity: str,
                 effect_type: str) -> None:
        super().__init__(name, cost, rarity)
        self.effect_type = effect_type

    def play(self, game_state: dict) -> dict:
        if not self.is_playable(game_state.get('mana', 0)):
            raise ValueError("Not enough mana to play this card")
        game_state['mana'] -= self.cost
        return {
            'card_played': self.name,
            'mana_used': self.cost,
            'effect': self.resolve_effect([])['effect']
        }

    def resolve_effect(self, targets: list) -> dict:
        effects = {
            'damage': f'Deal {self.cost} damage to target',
            'heal': f'Heal {self.cost} health to target',
            'buff': f'Buff target with +{self.cost}/+{self.cost}',
            'debuff': f'Debuff target with -{self.cost}/-{self.cost}'
        }
        effect = effects.get(self.effect_type, 'Unknown effect')
        return {
            'spell_name': self.name,
            'effect': effect,
            'targets': targets
        }
