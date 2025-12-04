from player import Player
from view import View
from random import choice

class GameController:
    def __init__(self, view: 'View', player1: Player, player2: Player):
        if not isinstance(view, View):
            raise TypeError("view must be an instance of View")
        if not isinstance(player1, Player):
            raise TypeError("player1 must be an instance of Player")
        if not isinstance(player2, Player):
            raise TypeError("player2 must be an instance of Player")

        self.__view = view
        self.__player1 = player1
        self.__player2 = player2

    def start_game_loop(self):
        attacker = self.who_start_first()
        defender = self.__player2 if attacker == self.__player1 else self.__player1

        self.__view.display_welcome_message(self.__player1, self.__player2)

        while self.__player1.is_alive() and self.__player2.is_alive():
            self.__view.display_turn_info(attacker, defender)
            self.handle_turn(attacker, defender)

            attacker, defender = defender, attacker

        winner = attacker if attacker.is_alive() else defender

    def handle_turn(self, attacker: Player, defender: Player):
        turn = True
        while turn:
            if attacker.should_use_potion() == "health":
                for potion in attacker.potions:
                    if potion.effect == "health":
                        potion_used = potion.apply_to(attacker)
                        if potion_used:
                            turn = False
            if not turn:
                break

            if attacker.should_use_potion() == "buff_str" or attacker.should_use_potion() == "buff_dex":
                for potion in attacker.potions:
                    if potion.effect == attacker.should_use_potion():
                        potion_used = potion.apply_to(attacker)
                        if potion_used:
                            turn = False
            if not turn:
                break

            damage = attacker.attack(defender)
    
    def who_start_first(self):
        return choice([self.__player1, self.__player2])
    
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, '_instance'):
            cls._instance = super(GameController, cls).__new__(cls)
        return cls._instance

