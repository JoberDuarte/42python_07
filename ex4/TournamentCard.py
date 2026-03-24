from ex0.Card import Card, Rarity
from ex2.Combatable import Combatable
from ex4.Rankable import Rankable


class TournamentCard(Card, Combatable, Rankable):
    def __init__(
        self,
        name: str,
        cost: int,
        rarity: Rarity,
        damage: int,
        health: int,
        defense: int,
        card_id: str
    ) -> None:
        super().__init__(name, cost, rarity)

        if not isinstance(damage, int):
            raise TypeError("damage must be an integer")
        if not isinstance(health, int):
            raise TypeError("health must be an integer")
        if not isinstance(defense, int):
            raise TypeError("defense must be an integer")
        if not isinstance(card_id, str) or not card_id.strip():
            raise ValueError("card_id must be a non-empty string")

        self.damage = damage
        self.health = health
        self.defense = defense
        self.id = card_id

        self.wins = 0
        self.losses = 0
        self.rank = 0
        self.rating = self.calculate_rating()

    def play(self, game_state: dict) -> dict:
        if "mana" not in game_state:
            return {"error": "game_state must contain key 'mana'"}

        current_mana = game_state["mana"]
        if self.is_playable(current_mana):
            game_state["mana"] -= self.cost
            return {
                "card_played": self.name,
                "mana_used": self.cost,
                "effect": "Creature summoned to battlefield"
            }

        return {"error": "insufficient mana", "mana_available": current_mana}

    def attack(self, target) -> dict:
        if not isinstance(target, TournamentCard):
            raise TypeError("target must be a TournamentCard")

        dealt_damage = max(0, self.damage - target.defense)
        target.health -= dealt_damage

        return {
            "attacker": self.name,
            "target": target.name,
            "damage_dealt": dealt_damage
        }

    def defend(self, incoming_damage: int) -> dict:
        if not isinstance(incoming_damage, int):
            raise TypeError("incoming_damage must be an integer")

        blocked = min(self.defense, incoming_damage)
        taken = incoming_damage - blocked
        self.health -= taken

        return {
            "defender": self.name,
            "damage_taken": taken,
            "damage_blocked": blocked,
            "still_alive": self.health > 0
        }

    def get_combat_stats(self) -> dict:
        return {
            "name": self.name,
            "health": self.health,
            "defense": self.defense,
            "damage": self.damage
        }

    def calculate_rating(self) -> int:
        return 1000 + (self.cost * 20) + self.health

    def update_wins(self, wins: int) -> None:
        if not isinstance(wins, int) or wins < 0:
            raise ValueError("wins must be a non-negative integer")
        self.wins += wins
        self.rating += 16 * wins

    def update_losses(self, losses: int) -> None:
        if not isinstance(losses, int) or losses < 0:
            raise ValueError("losses must be a non-negative integer")
        self.losses += losses
        self.rating -= 16 * losses

    def get_rank_info(self) -> dict:
        return {
            "id": self.id,
            "name": self.name,
            "rank": self.rank,
            "rating": self.rating,
            "wins": self.wins,
            "losses": self.losses
        }

    def get_tournament_stats(self) -> dict:
        return {
            "name": self.name,
            "id": self.id,
            "wins": self.wins,
            "losses": self.losses,
            "rating": self.rating,
            "rank": self.rank
        }
