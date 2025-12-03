import random as r

class Weapon:
    def __init__(self, name: str, min_damage: int, max_damage: int, weapon_type: str):
        if name == "":
            raise ValueError("Name cannot be empty.")

        if min_damage < 1 and min_damage > max_damage:
            raise ValueError("Minimum damage must be at least 1 and less than maximum damage.")

        if max_damage <= min_damage:
            raise ValueError("Maximum damage must be at least equal to minimum damage.")

        if not weapon_type == "melee" and not weapon_type == "ranged":
            raise ValueError("Type must be either 'melee' or 'ranged'.")

        self.__name = name
        self.__min_damage = min_damage
        self.__max_damage = max_damage
        self.__type = weapon_type

    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, new_name):
        if new_name == "":
            raise ValueError("The new name cannot be empty.")
        else:
            self.__name = new_name

    @property
    def min_damage(self):
        return self.__min_damage

    @property
    def max_damage(self):
        return self.__max_damage
    
    @property
    def type(self):
        return self.__type

# Methods
    def get_damage(self) -> int:
        return r.randint(self.__min_damage, self.__max_damage)

    def __str__(self) -> str:
        return f"Name: {self.__name}, Type: {self.__type}, Damage: {self.__min_damage}-{self.__max_damage}"
