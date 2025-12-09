from game_controller import GameController
from view import View
from player import Player
from weapon import Weapon
from potion import Potion
import random as r

def create_weapon(player: Player) -> None:
    with open("weapons.txt", "r") as file:
        lines = file.readlines()
    melee = lines[melee]
    ranged = lines[ranged]
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
    names = ["Thomas", "Margherita", "Mattia", "Borgio", "Adam", "Loris", "Duvarrini", "Mazzetti", "Orlando", "Jhonson", "Gentile", "Samu", "Farina", "Porcaro", "Matteo", "Borgio", "Quarta", "Seconda", "Prima", "Giulia", "Pietro", "Maio", "Martina", "Luca", "Camia", "Zullo"]
    player = Player(r.choice(names), r.randint(50,100), r.randint(1,20), r.randint(1,20))
    create_weapon(player)
    create_potion(player)
    return player

if __name__ == "__prova__":
    player1 = create_player()
    player2 = create_player()
    view = View()
    game_controller = GameController(view, player1, player2)
    game_controller.start_game_loop()