class Potion:
    def __init__(self, name: str, effect: str, amount: int, duration: int):
        if name == "":
            raise ValueError("Potion name cannot be empty.")

        if effect not in ["heal","buff_str", "buff_dex"]:
            raise ValueError("Effect must be 'heal', 'buff_str', or 'buff_dex'.")

        if amount <= 0:
            raise ValueError("Amount must be greater than 0.")

        if duration < 0:
            raise ValueError("Duration cannot be negative.")
        
        self.__name = name
        self.__effect = effect
        self.__amount = amount
        self.__duration = duration
        self.__applied = False # To track if the potion has been applied

    @property
    def name(self):
        return self.__name

    @property
    def effect(self):
        return self.__effect
    
    @property
    def amount(self):
        return self.__amount
    
    @property
    def duration(self):
        if self.effect == "heal":
            return "instant"
        return self.__duration
    
    @property
    def applied(self):
        return self.__applied

# Methods 
    def apply_to(self, target):
        if self.__applied:
            return  # Potion has already been applied

        if self.effect == "heal":
            if hasattr(target, 'heal') and callable(getattr(target, 'heal')):
                target.heal(self.__amount)
                self.__applied = True

        elif self.effect == "buff_str" or self.effect == "buff_dex":
            if hasattr(target, 'buff') and callable(getattr(target, 'buff')):
                target.buff(self.__effect, self.__amount, self.__duration)
                self.__applied = True

        else:
            raise ValueError("Unknown effect type.")

    def __str__(self):
        return f"Name: {self.name}, effect: {self.effect}, amount: {self.amount}, duration: {self.duration}"
    
    def __repr__(self):
        return self.__str__()