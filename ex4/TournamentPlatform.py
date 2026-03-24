import random

from ex4.TournamentCard import TournamentCard


class TournamentPlatform:
    def __init__(self) -> None:
        """Initialize platform state."""
        self.cards = {}
        self.matches_played = 0

    def register_card(self, card: TournamentCard) -> str:
        if not isinstance(card, TournamentCard):
            raise TypeError("card must be a TournamentCard")
        if card.id in self.cards:
            raise ValueError("card id already registered")

        self.cards[card.id] = card
        return card.id

    def create_match(self, card1_id: str, card2_id: str) -> dict:
        if card1_id == card2_id:
            raise ValueError("card ids must be different")
        if card1_id not in self.cards or card2_id not in self.cards:
            raise ValueError("one or both card ids are not registered")

        card1 = self.cards[card1_id]
        card2 = self.cards[card2_id]
        score1 = card1.damage + card1.defense + random.randint(0, 6)
        score2 = card2.damage + card2.defense + random.randint(0, 6)

        if score1 == score2:
            score1 += random.randint(0, 2)
            score2 += random.randint(0, 2)

        if score1 >= score2:
            winner = card1
            loser = card2
        else:
            winner = card2
            loser = card1

        winner.update_wins(1)
        loser.update_losses(1)
        self.matches_played += 1

        return {
            "winner": winner.id,
            "loser": loser.id,
            "winner_rating": winner.rating,
            "loser_rating": loser.rating
        }

    def get_leaderboard(self) -> list:
        ordered = sorted(
            self.cards.values(),
            key=lambda card: card.rating,
            reverse=True
        )

        leaderboard = []
        for index, card in enumerate(ordered, start=1):
            card.rank = index
            leaderboard.append(
                f"{index}. {card.name} - Rating: {card.rating} "
                f"({card.wins}-{card.losses})"
            )
        return leaderboard

    def generate_tournament_report(self) -> dict:
        total_cards = len(self.cards)
        if total_cards == 0:
            average_rating = 0
            status = "inactive"
        else:
            total_rating = sum(card.rating for card in self.cards.values())
            average_rating = int(total_rating / total_cards)
            status = "active"

        return {
            "total_cards": total_cards,
            "matches_played": self.matches_played,
            "avg_rating": average_rating,
            "platform_status": status
        }
