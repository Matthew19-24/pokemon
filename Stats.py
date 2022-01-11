import random
import math
from time import sleep


class Pokemon:
    def __init__(self, level):
        self.name = type(self).__name__.upper()
        self.attack_1 = None
        self.attack_2 = None
        self.attack_3 = None
        self.attack_4 = None
        self.effort_yield = None
        self.BASE_EXP = None
        self.wild = None
        self.wild_eq = None
        self.atk_stat_stage = 0
        self.def_stat_stage = 0
        self.hp_full = None
        self.growth_group = None
        self.exp = None
        self.hp_stat = None
        self.atk_stat = None
        self.def_stat = None
        self.spd_stat = None
        self.sp_atk_stat = None
        self.sp_def_stat = None
        self.nature_atk = None
        self.nature_def = None
        self.nature_spd = None
        self.nature_sp_atk = None
        self.nature_sp_def = None
        self.nature_list = None
        self.nature = None
        self.ev_sp_def = None
        self.ev_sp_atk = None
        self.ev_spd = None
        self.ev_hp = None
        self.ev_atk = None
        self.ev_def = None
        self.iv_sp_def = None
        self.iv_sp_atk = None
        self.iv_spd = None
        self.iv_def = None
        self.iv_atk = None
        self.iv_hp = None
        self.lvl = level
        self.BASE_HP = None
        self.BASE_ATK = None
        self.BASE_DEF = None
        self.BASE_SP_ATK = None
        self.BASE_SP_DEF = None
        self.BASE_SPD = None
        self.owner = None
        self.species = None
        self.type = None

    # Attack stat stage calculation for battles
    def attack_stat_stage(self):
        if self.atk_stat_stage < -6:
            self.atk_stat_stage = -6
            print("")
        elif self.atk_stat_stage > 6:
            self.atk_stat_stage = 6
        elif self.atk_stat_stage == -6:
            return float(2 / 8)
        elif self.atk_stat_stage == -5:
            return float(2 / 7)
        elif self.atk_stat_stage == -4:
            return float(2 / 6)
        elif self.atk_stat_stage == -3:
            return float(2 / 5)
        elif self.atk_stat_stage == -2:
            return float(2 / 4)
        elif self.atk_stat_stage == -1:
            return float(2 / 3)
        elif self.atk_stat_stage == 0:
            return float(2 / 2)
        elif self.atk_stat_stage == 1:
            return float(3 / 2)
        elif self.atk_stat_stage == 2:
            return float(4 / 2)
        elif self.atk_stat_stage == 3:
            return float(5 / 2)
        elif self.atk_stat_stage == 4:
            return float(6 / 2)
        elif self.atk_stat_stage == 5:
            return float(7 / 2)
        elif self.atk_stat_stage == 6:
            return float(8 / 2)

    # Randomize IV stats
    def set_iv(self):
        self.iv_hp = random.randrange(0, 32)
        self.iv_atk = random.randrange(0, 32)
        self.iv_def = random.randrange(0, 32)
        self.iv_spd = random.randrange(0, 32)
        self.iv_sp_atk = random.randrange(0, 32)
        self.iv_sp_def = random.randrange(0, 32)

    # Declaring blank EV variables
    def set_ev(self):
        self.ev_hp = 0
        self.ev_atk = 0
        self.ev_def = 0
        self.ev_spd = 0
        self.ev_sp_atk = 0
        self.ev_sp_def = 0

    # Set nature variables
    def set_nature(self):
        self.nature_atk = 1
        self.nature_def = 1
        self.nature_spd = 1
        self.nature_sp_atk = 1
        self.nature_sp_def = 1

        # Randomize nature
        self.nature_list = ["Adamant", "Bashful", "Brave", "Bold", "Calm", "Careful", "Docile", "Gentle", "Hardy",
                            "Hasty", "Impish", "Jolly", "Lax", "Lonely", "Mild", "Modest", "Naive", "Naughty", "Quiet",
                            "Quirky", "Rash", "Relaxed", "Sassy", "Serious", "Timid"]
        self.nature = self.nature_list[random.randrange(25)]

        # Change nature variables based on nature type
        if self.nature_list == "Adamant":
            self.nature_atk = 1.1
            self.nature_sp_atk = 0.9
        elif self.nature_list == "Lonely":
            self.nature_atk = 1.1
            self.nature_def = 0.9
        elif self.nature_list == "Brave":
            self.nature_atk = 1.1
            self.nature_spd = 0.9
        elif self.nature_list == "Naughty":
            self.nature_atk = 1.1
            self.nature_sp_def = 0.9
        elif self.nature_list == "Bold":
            self.nature_def = 1.1
            self.nature_atk = 0.9
        elif self.nature_list == "Relaxed":
            self.nature_def = 1.1
            self.nature_spd = 0.9
        elif self.nature_list == "Impish":
            self.nature_def = 1.1
            self.nature_sp_atk = 0.9
        elif self.nature_list == "Lax":
            self.nature_def = 1.1
            self.nature_sp_def = 0.9
        elif self.nature_list == "Timid":
            self.nature_spd = 1.1
            self.nature_atk = 0.9
        elif self.nature_list == "Hasty":
            self.nature_spd = 1.1
            self.nature_def = 0.9
        elif self.nature_list == "Jolly":
            self.nature_spd = 1.1
            self.nature_sp_atk = 0.9
        elif self.nature_list == "Naive":
            self.nature_spd = 1.1
            self.nature_sp_def = 0.9
        elif self.nature_list == "Modest":
            self.nature_sp_atk = 1.1
            self.nature_atk = 0.9
        elif self.nature_list == "Mild":
            self.nature_sp_atk = 1.1
            self.nature_atk = 0.9
        elif self.nature_list == "Quiet":
            self.nature_sp_atk = 1.1
            self.nature_spd = 0.9
        elif self.nature_list == "Rash":
            self.nature_sp_atk = 1.1
            self.nature_sp_def = 0.9
        elif self.nature_list == "Calm":
            self.nature_sp_def = 1.1
            self.nature_atk = 0.9
        elif self.nature_list == "Gentle":
            self.nature_sp_def = 1.1
            self.nature_def = 0.9
        elif self.nature_list == "Sassy":
            self.nature_sp_def = 1.1
            self.nature_spd = 0.9
        elif self.nature_list == "Careful":
            self.nature_sp_def = 1.1
            self.nature_sp_atk = 0.9

    # Set battle stats
    def set_stats(self):
        self.hp_stat = math.floor((2 * self.BASE_HP + self.iv_hp + self.ev_hp) * self.lvl / 100 + self.lvl + 10)
        self.hp_full = self.hp_stat
        self.atk_stat = math.floor(
            math.floor((2 * self.BASE_ATK + self.iv_atk + self.ev_atk) * self.lvl / 100 + 5) * self.nature_atk)
        self.def_stat = math.floor(
            math.floor((2 * self.BASE_DEF + self.iv_def + self.ev_def) * self.lvl / 100 + 5) * self.nature_def)
        self.spd_stat = math.floor(
            math.floor((2 * self.BASE_SPD + self.iv_spd + self.ev_spd) * self.lvl / 100 + 5) * self.nature_spd)
        self.sp_atk_stat = math.floor(math.floor(
            (2 * self.BASE_SP_ATK + self.iv_sp_atk + self.ev_sp_atk) * self.lvl / 100 + 5) * self.nature_sp_atk)
        self.sp_def_stat = math.floor(math.floor(
            (2 * self.BASE_SP_DEF + self.iv_sp_def + self.ev_sp_def) * self.lvl / 100 + 5) * self.nature_sp_atk)
        if self.wild:
            self.wild_eq = 1
        elif not self.wild:
            self.wild_eq = 1.5

    # Check experience when gained for level ups
    def exp_gain(self, exp_gain):
        self.exp += exp_gain
        print(f"\n{self.name} gained {exp_gain:.0f} EXP. Points!")
        if self.growth_group == "fast":
            for n in range(99):
                if self.exp >= math.floor(.8 * (self.lvl + 1) ** 3):
                    self.lvl += 1
                    self.set_stats()
                    sleep(1.5)
                    print(f"{self.name} grew to level {self.lvl}")

        elif self.growth_group == "med_fast":
            for n in range(99):
                if self.exp >= math.floor((self.lvl + 1) ** 3):
                    self.lvl += 1
                    self.set_stats()
                    sleep(1.5)
                    print(f"{self.name} grew to level {self.lvl}")

        elif self.growth_group == "med_slow":
            for n in range(99):
                if self.exp >= math.floor(
                        (1.2 * ((self.lvl + 1) ** 3)) - (15 * ((self.lvl + 1) ** 2)) + (100 * (self.lvl + 1)) - 140):
                    self.lvl += 1
                    self.set_stats()
                    sleep(1.5)
                    print(f"{self.name} grew to level {self.lvl}")

        elif self.growth_group == "slow":
            for n in range(99):
                if self.exp >= 1.25 * (self.lvl + 1) ** 3:
                    self.lvl += 1
                    self.set_stats()
                    sleep(1.5)
                    print(f"{self.name} grew to level {self.lvl}")

    # Display IV's function
    def display_iv(self):
        print(f"\n{self.name}'s Individual Value's\n" +
              f"HP: {self.iv_hp}\n" +
              f"Attack: {self.iv_atk}\n" +
              f"Defense: {self.iv_def}\n" +
              f"Speed: {self.iv_spd}\n" +
              f"Sp. Attack: {self.iv_sp_atk}\n" +
              f"Sp. Defense: {self.iv_sp_def}")

    # Display EV's function
    def display_ev(self):
        print(f"\n{self.name}'s Effort Value's\n" +
              f"HP: {self.ev_hp}\n" +
              f"Attack: {self.ev_atk}\n" +
              f"Defense: {self.ev_def}\n" +
              f"Speed: {self.ev_spd}\n" +
              f"Sp. Attack: {self.ev_sp_atk}\n" +
              f"Sp. Defense: {self.ev_sp_def}")

    # Display battle stats
    def display_stats(self):
        print(f"\nSpecies: {self.name}\n" +
              f"Owner: {self.owner}\n" +
              f"Level: {self.lvl}\n" +
              f"Experience: {self.exp}\n" +
              f"Type: {self.type}\n" +
              f"Nature: {self.nature}\n" +
              f"HP: {self.hp_stat}\n" +
              f"Attack: {self.atk_stat}\n" +
              f"Defense: {self.def_stat}\n" +
              f"Speed: {self.spd_stat}\n" +
              f"Sp. Attack: {self.sp_atk_stat}\n" +
              f"Sp. Defense: {self.sp_def_stat}")

    # Attack battle functions
    def attack1(self, target):
        self.attack_1.attack(self, target)

    def attack2(self, target):
        self.attack_2.attack(self, target)
