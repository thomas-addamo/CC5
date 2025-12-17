from player import Player

from colorama import init, Fore, Style

# Inizializza Colorama (autoreset evita di dover resettare manualmente ogni volta)
init(autoreset=True)


class ConsoleView:
    def __init__(self):
        pass

    def show_welcome(self):
        title = "👑 WELCOME TO CODE COMBAT 👑"
        line = "═" * 52
        print(Fore.CYAN + line)
        print(Fore.CYAN + "║" + Style.BRIGHT + Fore.YELLOW + title.center(50) + Fore.CYAN + "║")
        print(Fore.CYAN + line)
        print()
        print(Style.BRIGHT + Fore.WHITE + "📃  Instructions")
        print(Fore.CYAN + "─" * 52)
        print(
            Fore.WHITE
            +   "  In this simulation, two characters will be created randomly\n"
                "  with various stats, a weapon and two potions.\n"
                "  The two characters will then fight each other."
        )
        print()
        print(Style.BRIGHT + Fore.MAGENTA + "== Combat simulation starts ==" + Style.RESET_ALL + "\n")

    def show_validation_error(self, component: str, message: str):
        print(Style.BRIGHT + Fore.RED + "⛔️  ERROR")
        print(Fore.RED + "─" * 52)
        print(Fore.WHITE + f"  Component: {Style.BRIGHT}{component}{Style.RESET_ALL}")
        print(Fore.WHITE + f"  Message:   {Style.BRIGHT}{message}{Style.RESET_ALL}\n")

    def show_default_weapon(self, player_name, default_weapon_name):
        if default_weapon_name is None:
            weapon = "Bare-handed attack"
        else:
            weapon = f"Attack with {default_weapon_name}"
        print(Fore.WHITE + f"{Style.BRIGHT}{player_name}{Style.RESET_ALL} uses: "
            f"{Fore.YELLOW}{weapon}{Style.RESET_ALL}")

    def show_initial_stats(self, p1: Player, p2: Player):
        print("\n" + Fore.CYAN + "═" * 52)
        print(Style.BRIGHT + Fore.CYAN + "🤺  Characters".center(52))
        print(Fore.CYAN + "═" * 52)

        for p in [p1, p2]:
            print(Style.BRIGHT + Fore.YELLOW + f"[{p.name}]".center(52))
            print(Fore.WHITE + f"  Health:    {Style.BRIGHT}{Fore.GREEN}{p.health}/{p.max_health}{Style.RESET_ALL}")
            print(Fore.WHITE + f"  Strength:  {Style.BRIGHT}{Fore.MAGENTA}{p.strength}{Style.RESET_ALL}")
            print(Fore.WHITE + f"  Dexterity: {Style.BRIGHT}{Fore.MAGENTA}{p.dexterity}{Style.RESET_ALL}")
            
            weapon_display = p.weapon.name if p.weapon else "Bare-handed"
            print(Fore.WHITE + f"  Weapon:    {Style.BRIGHT}{Fore.YELLOW}{weapon_display}{Style.RESET_ALL}")
            
            potions_display = ", ".join([pot.name for pot in p.potions]) if p.potions else "None"
            print(Fore.WHITE + f"  Potions:   {Style.BRIGHT}{Fore.CYAN}{potions_display}{Style.RESET_ALL}")
            print()

        print(Fore.CYAN + "═" * 52 + "\n")

    def show_player_stats(self, player: Player):
        print(Style.BRIGHT + Fore.WHITE + f"📊  {player.name} Stats")
        print(Fore.CYAN + "─" * 52)
        print(Fore.WHITE + f"  Health:    {Style.BRIGHT}{Fore.GREEN}{player.health}/{player.max_health}{Style.RESET_ALL}")
        print(Fore.WHITE + f"  Strength:  {Style.BRIGHT}{Fore.MAGENTA}{player.strength}{Style.RESET_ALL}")
        print(Fore.WHITE + f"  Dexterity: {Style.BRIGHT}{Fore.MAGENTA}{player.dexterity}{Style.RESET_ALL}")
        print(Fore.WHITE + f"  Weapon:    {Style.BRIGHT}{Fore.YELLOW}{player.weapon}{Style.RESET_ALL}")
        print(Fore.WHITE + f"  Potions:   {Style.BRIGHT}{Fore.CYAN}{player.potions}{Style.RESET_ALL}")

    def show_turn_header(self, turn_number):
        line = "─" * 52
        print("\n" + Fore.BLUE + line)
        print(Style.BRIGHT + Fore.BLUE + f"🔄  Turn {turn_number}".center(52))
        print(Fore.BLUE + line + "\n")

    def show_effect_finished(self, player_name, effect_desc):
        print(Fore.YELLOW + f"⏳  {Style.BRIGHT}{player_name}{Style.RESET_ALL}{Fore.YELLOW}'s effect has finished: "
            f"{Fore.WHITE}{effect_desc}")

    def show_player_turn(self, player_name):
        print(Fore.CYAN + f"➡️  It's {Style.BRIGHT}{player_name}{Style.RESET_ALL}{Fore.CYAN}'s turn.")

    def show_potion_decision(self, player_name, potion_name):
        print(Fore.CYAN + f"🍾  {Style.BRIGHT}{player_name}{Style.RESET_ALL}{Fore.CYAN} uses the potion: "
            f"{Style.BRIGHT}{Fore.YELLOW}{potion_name}{Style.RESET_ALL}")

    def show_action_failure(self, player_name, action_name, reason):
        print(Fore.RED + f"❌  {Style.BRIGHT}{player_name}{Style.RESET_ALL}{Fore.RED} fails to "
            f"{Style.BRIGHT}{action_name}{Style.RESET_ALL}{Fore.RED}: {Fore.WHITE}{reason}")

    def show_potion_success(self, player_name, effect_desc, current_hp_msg):
        print(Fore.GREEN + f"✅  {Style.BRIGHT}{player_name}{Style.RESET_ALL}{Fore.GREEN} uses a potion with effect: "
            f"{Fore.WHITE}{effect_desc}{Fore.GREEN}. {Fore.WHITE}{current_hp_msg}")

    def show_attack_result(self, attacker_name, defender_name, damage):
        dmg_color = Fore.GREEN if damage > 0 else Fore.YELLOW
        print(Fore.WHITE + "⚔️  "
            + Style.BRIGHT + Fore.YELLOW + f"{attacker_name}" + Style.RESET_ALL
            + Fore.WHITE + " attacks "
            + Style.BRIGHT + Fore.YELLOW + f"{defender_name}" + Style.RESET_ALL
            + Fore.WHITE + " dealing "
            + Style.BRIGHT + dmg_color + f"{damage}" + Style.RESET_ALL
            + Fore.WHITE + " damage.")

    def show_winner(self, winner_name):
        line = "═" * 52
        print("\n" + Fore.GREEN + line)
        print(Style.BRIGHT + Fore.GREEN + f"🏆  {winner_name} has won the fight!".center(52))
        print(Fore.GREEN + line + "\n")

    def get_user_input(self, prompt):
        return input(Style.BRIGHT + Fore.WHITE + prompt + Style.RESET_ALL)
