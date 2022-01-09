import math
from time import sleep


# Define superclass for all physical attacks
class Physical:
    def __init__(self):
        self.name = None
        self.power = None
        self.accuracy = None
        self.pp = None
        self.pp_full = None
        self.pp_max = None

    def attack(self, user, target):
        if self.pp > 0:
            self.pp -= 1
            damage = math.floor(
                math.floor(math.floor(2 * user.lvl / 5 + 2) * (user.atk_stat * user.attack_stat_stage()) * self.power / target.def_stat) / 50) + 2
            target.hp_stat -= damage
            sleep(1.5)
            print(f"\n{user.owner}'s {user.name} used {self.name} inflicting {str(damage)}")
            sleep(1.5)
            print(f"{target.owner}'s {target.name} has {target.hp_stat} HP left!")


class Tackle(Physical):
    def __init__(self):
        super().__init__()
        self.name = "Tackle"
        self.power = 40
        self.accuracy = 100
        self.pp = 35
        self.pp_full = 35
        self.pp_max = 56


class Scratch(Physical):
    def __init__(self):
        super().__init__()
        self.name = "Scratch"
        self.power = 40
        self.accuracy = 100
        self.pp = 35
        self.pp_full = 35
        self.pp_max = 56


class Growl:
    def __init__(self):
        self.name = "Growl"
        self.accuracy = 100
        self.pp = 40
        self.pp_full = 40
        self.pp_max = 64

    def attack(self, user, target):
        if self.pp > 0:
            self.pp -= 1
            target.atk_stat_stage -= 1
            sleep(1.5)
            print(f"\n{user.owner}'s {user.name} used {self.name}")
            sleep(1.5)
            print(f"{target.owner}'s {target.name}'s attack fell!")


class Tail_Whip:
    def __init__(self):
        self.name = "Tail Whip"
        self.accuracy = 100
        self.pp = 30
        self.pp_full = 30
        self.pp_max = 48

    def attack(self, user, target):
        if self.pp > 0:
            self.pp -= 1
            target.def_stat_stage -= 1
            sleep(1.5)
            print(f"\n{user.owner}'s {user.name} used {self.name}")
            sleep(1.5)
            print(f"{target.owner}'s {target.name}'s defense fell!")
