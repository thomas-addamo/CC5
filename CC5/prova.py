from game_controller import GameController
from view import View
from player import Player
from weapon import Weapon
from potion import Potion
import random as r

def create_weapon(player: Player) -> None:
    melee = [
        Weapon("Sword", r.randint(8,12), r.randint(13,18), "melee"),
        Weapon("Axe", r.randint(10,15), r.randint(16,20), "melee"),
        Weapon("Dagger", r.randint(5,10), r.randint(11,15), "melee"),
        Weapon("Mazzetta", 1, r.randint(2,100), "melee"),
        Weapon("long sword", r.randint(12,18), r.randint(19,25), "melee"),
        Weapon("short sword", r.randint(7,11), r.randint(12,16), "melee"),
        Weapon("Katana", r.randint(10,14), r.randint(15,22), "melee"),
        Weapon("Claymore", r.randint(15,20), r.randint(20,30), "melee"),
        Weapon("Spada Laser", r.randint(20,30), r.randint(30,50), "melee"),
        Weapon("Mace", r.randint(9,13), r.randint(14,19), "melee"),
        Weapon("Hammer", r.randint(11,16), r.randint(17,22), "melee"),
        Weapon("raipier", r.randint(6,10), r.randint(11,15), "melee")
    ]
    ranged = [
        Weapon("Bow", r.randint(5,10), r.randint(11,15), "ranged"),
        Weapon("Crossbow", r.randint(7,12), r.randint(13,17), "ranged"),
        Weapon("Throwing Knives", r.randint(4,9), r.randint(10,14), "ranged"),
        Weapon("Slingshot", r.randint(1,5), r.randint(7,12), "ranged"),
        Weapon("blowgun", r.randint(3,8), r.randint(9,13), "ranged"),
        Weapon("Sniper Rifle", r.randint(15,25), r.randint(26,35), "ranged"),
        Weapon("Pistol", r.randint(10,15), r.randint(16,20), "ranged"),
        Weapon("Rifle", r.randint(12,18), r.randint(19,25), "ranged"),
        Weapon("Shotgun", r.randint(14,20), r.randint(21,30), "ranged"),
        Weapon(" of Mazzetti", r.randint(20,40), r.randint(41,60), "ranged"),
        Weapon("Laser Gun", r.randint(25,35), r.randint(36,50), "ranged"),
        Weapon("Plasma Rifle", r.randint(30,45), r.randint(46,70), "ranged")
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