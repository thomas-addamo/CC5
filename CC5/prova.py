from game_controller import GameController
from view import ConsoleView
from player import Player
from weapon import Weapon
from potion import Potion
import random as r
from pathlib import Path

def create_weapon(player: Player) -> None:
    import json
    file_path = Path(__file__).parent / "weapons.json"
    with open(file_path, "r") as file:
        weapons = json.load(file)
    if player.strength < player.dexterity:
        weapon_data = r.choice(weapons["ranged"])
    else:
        weapon_data = r.choice(weapons["melee"])
    player.weapon = Weapon(weapon_data["name"], weapon_data["min_damage"], weapon_data["max_damage"], weapon_data["type"])

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
    file_path = Path(__file__).parent / "names.json"
    with open(file_path, "r") as file:
        names = [line.strip() for line in file.readlines()]
    player = Player(r.choice(names), r.randint(50,100), r.randint(1,20), r.randint(1,20))
    create_weapon(player)
    create_potion(player)
    return player


player1 = create_player()
player2 = create_player()
view = ConsoleView()
game_controller = GameController(view, player1, player2)
game_controller.start_game_loop()