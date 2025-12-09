class ConsoleView:
    def __init__(self):
        pass

    def show_welcome(self):
        print("=" * 40)
        print("-- 👑 WELCOME TO CODE COMBAT 👑 --")
        print("=" * 40)
        print("")
        print("📃 | Instructions:")
        print(
            "  In this simulation, two characters will be created randomly\n"
            "  with various stats, a weapon and two potions.\n"
            "  The two characters will then fight each other."
        )
        print("")
        print("== Combat simulation starts ==\n")

    def show_validation_error(self, component: str, message: str):
        print("⛔️ | ERROR:")
        print(f"  Component: {component}")
        print(f"  Message: {message}\n")

    def show_default_weapon(self, player_name, default_weapon_name):
        if default_weapon_name is None:
            weapon = "Bare-handed attack"
        else:
            weapon = f"Attack with {default_weapon_name}"
        print(f"{player_name} uses: {weapon}")

    # Nuovo contratto: usa DTO (dizionari) ma mantiene i vecchi nomi interni
    def show_initial_stats(self, p1_state: dict, p2_state: dict):
        # --- Unpack Player 1 state (stessi nomi di variabili di prima) ---
        p1_name = p1_state["p1_name"]
        p1_hp = p1_state["p1_hp"]
        p1_mhp = p1_state["p1_mhp"]
        p1_str = p1_state["p1_str"]
        p1_dex = p1_state["p1_dex"]
        p1_weap = p1_state["p1_weap"]
        p1_pot = p1_state["p1_pot"]

        # --- Unpack Player 2 state ---
        p2_name = p2_state["p2_name"]
        p2_hp = p2_state["p2_hp"]
        p2_mhp = p2_state["p2_mhp"]
        p2_str = p2_state["p2_str"]
        p2_dex = p2_state["p2_dex"]
        p2_weap = p2_state["p2_weap"]
        p2_pot = p2_state["p2_pot"]

        print("\n" + "=" * 40)
        print("🤺 | Characters:")
        print("=" * 40)

        p1_stats = (
            f"| {p1_name}: HP {p1_hp}/{p1_mhp}, "
            f"Strength {p1_str}, Dexterity {p1_dex}, "
            f"Weapon: {p1_weap}, Potions: {p1_pot} |"
        )
        p2_stats = (
            f"| {p2_name}: HP {p2_hp}/{p2_mhp}, "
            f"Strength {p2_str}, Dexterity {p2_dex}, "
            f"Weapon: {p2_weap}, Potions: {p2_pot} |"
        )

        max_len = max(len(p1_stats), len(p2_stats))
        border = "-" * max_len

        # Adjust lines to same length for a neat box
        p1_stats = p1_stats.ljust(max_len)
        p2_stats = p2_stats.ljust(max_len)

        print(border)
        print(p1_stats)
        print(p2_stats)
        print(border + "\n")

    def show_turn_header(self, turn_number):
        print("\n" + "-" * 40)
        print(f"--- 🔄 Turn {turn_number} 🔄 ---")
        print("-" * 40 + "\n")

    def show_potion_decision(self, player_name, potion_name):
        print(f"🍾 | {player_name} uses the potion: {potion_name}")

    def show_action_failure(self, player_name, action_name, reason):
        print(f"❌ | {player_name} fails to {action_name}: {reason}")

    def show_potion_success(self, player_name, effect_desc, current_hp_msg):
        print(f"✅ | {player_name} uses a potion with effect: {effect_desc}. {current_hp_msg}")

    def show_attack_result(self, attacker_name, defender_name, damage):
        print(f"⚔️ | {attacker_name} attacks {defender_name} dealing {damage} damage.")

    def show_winner(self, winner_name):
        print("\n" + "=" * 40)
        print(f"🏆 | {winner_name} has won the fight!")
        print("=" * 40 + "\n")

    def get_user_input(self, prompt):
        return input(prompt)
