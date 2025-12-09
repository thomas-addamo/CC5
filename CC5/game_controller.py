from player import Player
from view import ConsoleView
from random import choice

class GameController:
    def __init__(self, view: ConsoleView, player1: Player, player2: Player):
        if not isinstance(view, ConsoleView):
            raise TypeError("view must be an instance of ConsoleView")
        if not isinstance(player1, Player):
            raise TypeError("player1 must be an instance of Player")
        if not isinstance(player2, Player):
            raise TypeError("player2 must be an instance of Player")

        self.__view = view
        self.__player1 = player1
        self.__player2 = player2

    def start_game_loop(self):
        self.__view.show_welcome()
        self.__view.show_initial_stats(self.__player1, self.__player2)
        attacker = self.who_start_first()
        defender = self.__player2 if attacker == self.__player1 else self.__player1

        while self.__player1.is_alive() and self.__player2.is_alive():
            turn = self.handle_turn(attacker, defender)
            if isinstance(turn, int):
                self.__view.show_attack_result(attacker.name, defender.name, turn)
            else:
                self.__view.show_potion_decision(attacker.name, turn.name)
            attacker, defender = defender, attacker

        winner = attacker if attacker.is_alive() else defender
        self.__view.show_winner(winner.name)

    def handle_turn(self, attacker: Player, defender: Player):
        decision = attacker.should_use_potion()

        if decision == "health":
            for potion in attacker.potions:
                if potion.effect == "health" and not potion.applied:
                    used = potion.apply_to(attacker)
                    if used:
                        return potion

        if decision in ("buff_str", "buff_dex"):
            for potion in attacker.potions:
                if potion.effect == decision and not potion.applied:
                    used = potion.apply_to(attacker)
                    if used:
                        return potion

        damage = attacker.attack(defender)
        return int(damage)


    def who_start_first(self):
        return choice([self.__player1, self.__player2])
    
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, '_instance'):
            cls._instance = super(GameController, cls).__new__(cls)
        return cls._instance

