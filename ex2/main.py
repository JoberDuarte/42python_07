from ex0.Card import Rarity
from ex2.EliteCard import EliteCard


def main() -> None:
    try:
        print("\n=== DataDeck Ability System ===\n")
        print("EliteCard capabilities:")
        print("- Card: ['play', 'get_card_info', 'is_playable']")
        print("- Combatable: ['attack', 'defend', 'get_combat_stats']")
        print("- Magical: ['cast_spell', 'channel_mana', 'get_magic_stats']")

        elite = EliteCard("Arcane Warrior", 6, Rarity.LEGENDARY, 8, 5, "melee",
                          8)
        print(f"\nPlaying {elite.name} (Elite Card):\n")

        print("Combat phase:")
        print(f"Attack result: {elite.attack('Enemy')}")
        print(f"Defense result: {elite.defend(5)}")

        print("\nMagic phase:")
        print(f"Spell cast: "
              f"{elite.cast_spell('Fireball', ['Enemy1', 'Enemy2'])}")
        print(f"Mana channel: {elite.channel_mana(3)}")
    except ValueError as e:
        print(e)
    except TypeError as e:
        print(e)
    except Exception as e:
        print(e)
    print("\nMultiple interface implementation successful!")


if __name__ == "__main__":
    main()
