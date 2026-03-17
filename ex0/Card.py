from abc import ABC, abstractmethod
from typing import Any, Dict


class Card(ABC):
    """Classe base abstrata - o contrato universal de todas as cartas."""

    def __init__(self, name: str, cost: int, rarity: str) -> None:
        self.name: str = name
        self.cost: int = cost
        self.rarity: str = rarity

    @abstractmethod
    def play(self, game_state: Dict[str, Any]) -> Dict[str, Any]:
        """Método abstrato: toda carta deve implementar como é jogada."""
        pass

    def get_card_info(self) -> Dict[str, Any]:
        """Método concreto herdado por todas as cartas."""
        return {
            "name": self.name,
            "cost": self.cost,
            "rarity": self.rarity,
            "type": "Card",
        }

    def is_playable(self, available_mana: int) -> bool:
        """Método concreto reutilizável."""
        return available_mana >= self.cost
