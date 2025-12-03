from player import Player
from weapon import Weapon
from potion import Potion
import random as r

def create_weapon(player: Player) -> None:
    melee = [
        Weapon("Sword", r.randint(8,12), r.randint(13,18), "melee"),
        Weapon("Axe", r.randint(10,15), r.randint(16,20), "melee"),
        Weapon("Dagger", r.randint(5,10), r.randint(11,15), "melee")
    ]
    ranged = [
        Weapon("Bow", r.randint(5,10), r.randint(11,15), "ranged"),
        Weapon("Crossbow", r.randint(7,12), r.randint(13,17), "ranged"),
        Weapon("Throwing Knives", r.randint(4,9), r.randint(10,14), "ranged")
    ]
    if player.strength < player.dexterity:
        player.weapon = r.choice(ranged)
    else:
        player.weapon = r.choice(melee)

def create_potion(player: Player) -> None:
    potion_health = Potion("Health Potion", "heal", r.randint(15,30), 0)
    potion_strength = Potion("Strength Elixir", "buff_str", r.randint(2,5), r.randint(3,6))
    potion_dexterity = Potion("Dexterity Draught", "buff_dex", r.randint(2,5), r.randint(3,6))
    
    player.potions.append(potion_health)
    if player.strength <= player.dexterity:
        player.potions = potion_dexterity
    else:
        player.potions = potion_strength

def create_player() -> Player:
    names = ["Arin", "Borin", "Cirin", "Dorin", "Erin", "Fin", "Gorin", "Hirin"]
    player = Player(r.choice(names), r.randint(50,100), r.randint(1,20), r.randint(1,20))
    create_weapon(player)
    create_potion(player)
    return player

def main():
    player1 = create_player()
    player2 = create_player()
    print("Player 1:")
    print(player1)
    print("\nPlayer 2:")
    print(player2)

    counter = 0
    while True:
        counter += 1
        print("\n" + "="*20)
        print(f"Turn: {counter}")

        print(f"\n{player1.name}'s Status: str: {player1.strength}, dex: {player1.dexterity}, health: {player1.health}")
        print(f"{player2.name}'s Status: str: {player2.strength}, dex: {player2.dexterity}, health: {player2.health}")

        if player1.tick_buffs():
            print(f"{player1.name} has finished the buff.")
        if player2.tick_buffs():
            print(f"{player2.name} has finished the buff.")

        # Start of the turn
        if player1.should_use_potion() == "health":
            for potion in player1.potions:
                if potion.effect == "heal":
                    potion.apply_to(player1)
                    print(f"{player1.name} uses {potion.name} and heals to {player1.health} health.")
                    break
        elif player1.should_use_potion() == "buff_str" or player1.should_use_potion() == "buff_dex":
            for potion in player1.potions:
                if potion.effect == player1.should_use_potion():
                    potion.apply_to(player1)
                    print(f"{player1.name} uses {potion.name} and buffs {potion.effect.split('_')[1]}.")
                    break

        damage = player1.attack(player2)
        print(f"{player1.name} attacks {player2.name} for {damage} damage. {player2.name} has {player2.health} health left.")
        if player2.is_alive() == False:
            print(f"{player2.name} has been defeated! {player1.name} wins!")
            break

        # Swap turns
        if player2.should_use_potion() == "health":
            for potion in player2.potions:
                if potion.effect == "heal":
                    potion.apply_to(player2)
                    print(f"{player2.name} uses {potion.name} and heals to {player2.health} health.")
                    break
        elif player2.should_use_potion() == "buff_str" or player2.should_use_potion() == "buff_dex":
            for potion in player2.potions:
                if potion.effect == player2.should_use_potion():
                    potion.apply_to(player2)
                    print(f"{player2.name} uses {potion.name} and buffs {potion.effect.split('_')[1]}.")
                    break

        damage = player2.attack(player2)
        print(f"{player2.name} attacks {player1.name} for {damage} damage. {player1.name} has {player1.health} health left.")
        if player1.is_alive() == False:
            print(f"{player1.name} has been defeated! {player2.name} wins!")
            break

if __name__ == "__main__":
    main()