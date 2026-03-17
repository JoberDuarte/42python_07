from .CreatureCard import CreatureCard


def main() -> None:
    print("\n=== DataDeck Card Foundation ===")
    print("\nTesting Abstract Base Class Design:")
    creature = CreatureCard("Fire Dragon", 5, "Legendary", 7, 5)
    print(f"\nCreatureCard Info: {creature.get_card_info()}")
    print("\nPlaying Fire Dragon with 6 mana available:")
    print(f"Playable: {creature.is_playable(6)}")
    print(f"Play result: {creature.play({})}")
    print("\nFire Dragon attacks Goblin Warrior:")
    print(f"Attack result: {creature.attack_target('Goblin Warrior')}")
    print("\nTesting insufficient mana (3 available):")
    print(f"Playable: {creature.is_playable(3)}")
    print("\nAbstract pattern successfully demonstrated!")


if __name__ == "__main__":
    main()
