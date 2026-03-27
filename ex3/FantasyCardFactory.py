from ex3.CardFactory import CardFactory
from ex0.CreatureCard import CreatureCard
from ex1.SpellCard import SpellCard
from ex1.ArtifactCard import ArtifactCard
from ex0.Card import Rarity


class FantasyCardFactory(CardFactory):

    def __init__(self):
        self.creatures = {
            'dragon': ("Fire Dragon", 5, Rarity.LEGENDARY.value, 7, 5),
            'goblin': ("Goblin Warrior", 2, Rarity.COMMON.value, 2, 2)
        }
        self.spells = {
            'fireball': ("Fireball", 4, Rarity.COMMON.value, "damage"),
            'lightning': ("Lightning Bolt", 3, Rarity.COMMON.value, "damage")
        }
        self.artifacts = {
            'crystal': ("Mana Crystal", 2, Rarity.RARE.value, 5,
                        "Permanent: +1 mana per turn"),
            'staff': ("Magic Staff", 3, Rarity.RARE.value, 3, "+2 spell power")
        }

    def create_creature(self, name_or_power: str | int | None = None):
        if isinstance(name_or_power, str):
            key = 'goblin' if 'goblin' in name_or_power.lower() else 'dragon'
        elif isinstance(name_or_power, int):
            key = 'goblin' if name_or_power <= 3 else 'dragon'
        else:
            key = 'dragon'
        data = self.creatures[key]
        return CreatureCard(*data)

    def create_spell(self, name_or_power: str | int | None = None):
        if isinstance(name_or_power, str):
            key = 'fireball' if 'fireball' in name_or_power.lower() \
                else 'lightning'
            data = self.spells[key]
            return SpellCard(*data)
        elif isinstance(name_or_power, int):
            return SpellCard("Lightning Bolt", name_or_power,
                             Rarity.COMMON.value, "damage")
        else:
            data = self.spells['lightning']
            return SpellCard(*data)

    def create_artifact(self, name_or_power: str | int | None = None):
        if isinstance(name_or_power, str):
            key = 'staff' if 'staff' in name_or_power.lower() else 'crystal'
            data = self.artifacts[key]
            return ArtifactCard(*data)
        elif isinstance(name_or_power, int):
            return ArtifactCard("Mana Crystal", name_or_power,
                                Rarity.RARE.value, 5,
                                "Permanent: +1 mana per turn")
        else:
            data = self.artifacts['crystal']
            return ArtifactCard(*data)

    def create_themed_deck(self, size: int) -> dict:
        return {'size': size, 'theme': 'Fantasy'}

    def get_supported_types(self) -> dict:
        return {
            'creatures': ['dragon', 'goblin'],
            'spells': ['fireball'],
            'artifacts': ['mana_ring']
        }
