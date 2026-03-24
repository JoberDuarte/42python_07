from ex0.Card import Card, Rarity
from ex2.Combatable import Combatable
from ex2.Magical import Magical


class EliteCard(Card, Combatable, Magical):
    def __init__(self, name: str, cost: int, rarity: Rarity,
                 healthy: int, damage: int, combat_type: str,
                 mana: int) -> None:
        super().__init__(name, cost, rarity)
        if damage <= 0:
            raise ValueError("Damage has to be positive")
        if healthy <= 0:
            raise ValueError("Healthy has to be positive")
        if mana <= 0:
            raise ValueError("Mana has to be positive")
        self.damage = damage
        self.health = healthy
        self.mana = mana
        self.combat_type = combat_type
        self.defense = 3

    def play(self, game_state: dict | str) -> dict:
        val = 0
        if "mana" not in game_state and "Mana" not in game_state:
            return {"error": "The key has to be mana!"}

        mana_key = "mana" if "mana" in game_state else "Mana"
        val = game_state[mana_key]

        if self.is_playable(val):
            game_state[mana_key] -= self.cost
            return {
                'card_played': self.name,
                'mana_used': self.cost,
                'effect': "Creature summoned to battlefield"
            }
        return {
            "insufficient mana": game_state.get("Mana")
        }

    def attack(self, target: Card) -> dict:
        return {
            'attacker': self.name,
            'target': target,
            'damage': self.damage,
            'combat_type': self.combat_type
            }

    def defend(self, incoming_damage: int) -> dict:
        try:
            incoming_damage + 0
        except TypeError:
            return {"Error": "Damage must be a number"}

        if self.defense <= incoming_damage:
            damage_blocked = self.defense
        else:
            damage_blocked = incoming_damage
        damage_taken = incoming_damage - damage_blocked

        self.health -= damage_taken
        return {
            'defender': self.name,
            'damage_taken': damage_taken,
            'damage_blocked': damage_blocked,
            'still_alive': self.health > 0
            }

    def get_combat_stats(self) -> dict:
        return {'name': self.name,
                'defense': self.defense,
                'health': self.health
                }

    def cast_spell(self, spell_name: str, targets: list) -> dict:
        mana_used = 4
        self.mana -= mana_used
        return {
            'caster': self.name,
            'spell': spell_name,
            'targets': targets,
            'mana_used': mana_used
            }

    def channel_mana(self, amount: int) -> dict:
        self.mana += amount
        return {'channeled': amount, 'total_mana': self.mana}

    def get_magic_stats(self) -> dict:
        return {'name': self.name, 'mana': self.mana}
