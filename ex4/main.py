from ex0.Card import Rarity
from ex4.TournamentCard import TournamentCard
from ex4.TournamentPlatform import TournamentPlatform


def main() -> None:
    try:
        print("=== DataDeck Tournament Platform ===\n")
        print("Registering Tournament Cards...\n")

        card1 = TournamentCard(
            "Fire Dragon", 5, Rarity.LEGENDARY, 7, 100, 4, "dragon_001"
        )
        card2 = TournamentCard(
            "Ice Wizard", 5, Rarity.RARE, 3, 3, 6, "wizard_001"
        )

        tournament = TournamentPlatform()

        tournament.register_card(card1)
        tournament.register_card(card2)

        interfaces = ["Card", "Combatable", "Rankable"]
        print(f"{card1.name} (ID: {card1.id}):")
        print(f"- Interfaces: {interfaces}")
        print(f"- Rating: {card1.rating}")
        print("- Record: 0-0")

        print(f"\n{card2.name} (ID: {card2.id}):")
        print(f"- Interfaces: {interfaces}")
        print(f"- Rating: {card2.rating}")
        print("- Record: 0-0")

        print("\nCreating tournament match...")
        match = tournament.create_match(card1.id, card2.id)
        print(f"Match result: {match}")

        print("\nTournament Leaderboard:")
        for line in tournament.get_leaderboard():
            print(line)

        report = tournament.generate_tournament_report()
        print("\nPlatform Report:")
        print(report)

        print("\n=== Tournament Platform Successfully Deployed! ===")
        print("All abstract patterns working together harmoniously!")

    except (TypeError, ValueError) as error:
        print(f"Error: {error}")
    except Exception as error:
        print(f"Unexpected error: {error}")


if __name__ == "__main__":
    main()
