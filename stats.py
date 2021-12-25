import random
import math


class Pokemon:
    def __init__(self, level):
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

    # Check experience when gained for level ups

    def level_up_check(self):
        if self.growth_group == "fast":
            for n in range(99):
                if self.exp >= math.floor(.8 * (self.lvl + 1) ** 3):
                    self.lvl += 1
                    print("level up! Lvl ", self.lvl)

        elif self.growth_group == "med_fast":
            for n in range(99):
                if self.exp >= math.floor((self.lvl + 1) ** 3):
                    self.lvl += 1
                    print("level up! lvl ", self.lvl)

        elif self.growth_group == "med_slow":
            for n in range(99):
                if self.exp >= math.floor((1.2 * ((self.lvl + 1) ** 3)) - (15 * ((self.lvl + 1) ** 2)) + (100 * (self.lvl + 1)) - 140):
                    self.lvl += 1
                    print("level up! lvl ", self.lvl)

        elif self.growth_group == "slow":
            for n in range(99):
                if self.exp >= 1.25 * (self.lvl + 1) ** 3:
                    self.lvl += 1
                    print("level up! lvl ", self.lvl)

    # Display IV's function
    def display_iv(self):
        print(f"\n{type(self).__name__}'s Individual Value's\n" +
              f"HP: {self.iv_hp}\n" +
              f"Attack: {self.iv_atk}\n" +
              f"Defense: {self.iv_def}\n" +
              f"Speed: {self.iv_spd}\n" +
              f"Sp. Attack: {self.iv_sp_atk}\n" +
              f"Sp. Defense: {self.iv_sp_def}")

    # Display EV's function
    def display_ev(self):
        print(f"\n{type(self).__name__}'s Effort Value's\n" +
              f"HP: {self.ev_hp}\n" +
              f"Attack: {self.ev_atk}\n" +
              f"Defense: {self.ev_def}\n" +
              f"Speed: {self.ev_spd}\n" +
              f"Sp. Attack: {self.ev_sp_atk}\n" +
              f"Sp. Defense: {self.ev_sp_def}")

    # Display battle stats
    def display_stats(self):
        print(f"\nSpecies: {type(self).__name__}\n" +
              f"Owner: {self.owner}\n" +
              f"Level: {self.lvl}\n" +
              f"Type: {self.type}\n" +
              f"Nature: {self.nature}\n" +
              f"HP: {self.hp_stat}\n" +
              f"Attack: {self.atk_stat}\n" +
              f"Defense: {self.def_stat}\n" +
              f"Speed: {self.spd_stat}\n" +
              f"Sp. Attack: {self.sp_atk_stat}\n" +
              f"Sp. Defense: {self.sp_def_stat}")


class Bulbasaur(Pokemon):
    def __init__(self, level, owner):
        super().__init__(level)
        self.set_iv()
        self.set_ev()
        self.set_nature()
        self.owner = owner
        self.growth_group = "med_slow"
        self.type = "Grass"
        self.BASE_HP = 45
        self.BASE_ATK = 49
        self.BASE_DEF = 49
        self.BASE_SP_ATK = 65
        self.BASE_SP_DEF = 65
        self.BASE_SPD = 45
        self.set_stats()


class Charmander(Pokemon):
    def __init__(self, level, owner):
        super().__init__(level)
        self.set_iv()
        self.set_ev()
        self.set_nature()
        self.owner = owner
        self.growth_group = "med_slow"
        self.type = "Fire"
        self.BASE_HP = 39
        self.BASE_ATK = 52
        self.BASE_DEF = 43
        self.BASE_SP_ATK = 60
        self.BASE_SP_DEF = 50
        self.BASE_SPD = 65
        self.set_stats()


class Squirtle(Pokemon):
    def __init__(self, level, owner):
        super().__init__(level)
        self.set_iv()
        self.set_ev()
        self.set_nature()
        self.owner = owner
        self.growth_group = "med_slow"
        self.type = "Water"
        self.BASE_HP = 44
        self.BASE_ATK = 48
        self.BASE_DEF = 65
        self.BASE_SP_ATK = 50
        self.BASE_SP_DEF = 64
        self.BASE_SPD = 43
        self.set_stats()
        self.nature = self.nature_list[random.randrange(25)]
        
        #Change nature variables based on nature type
        if self.nature_list == "Adamant":
            self.nature_hp = 1.1
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
            self.nature_spd == 1.1
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

    ##Set battle stats
    def set_stats(self):
        self.HP = math.floor((2 * self.BASE_HP + self.IV_HP + self.EV_HP) * self.LVL / 100 + self.LVL + 10)
        self.ATK = math.floor(math.floor((2 * self.BASE_ATK + self.IV_ATK + self.EV_ATK) * self.LVL / 100 + 5) * self.nature_atk)
        self.DEF = math.floor(math.floor((2 * self.BASE_DEF + self.IV_DEF + self.EV_DEF) * self.LVL / 100 + 5) * self.nature_def)
        self.SPD = math.floor(math.floor((2 * self.BASE_SPD + self.IV_SPD + self.EV_SPD) * self.LVL / 100 + 5) * self.nature_spd)
        self.SP_ATK = math.floor(math.floor((2 * self.BASE_SP_ATK + self.IV_SP_ATK + self.EV_SP_ATK) * self.LVL / 100 + 5) * self.nature_sp_atk)
        self.SP_DEF = math.floor(math.floor((2 * self.BASE_SP_DEF + self.IV_SP_DEF + self.EV_SP_DEF) * self.LVL / 100 + 5) * self.nature_sp_atk)


    ##Display IV's function
    def display_IV(self):
        print(f"{type(self).__name__}'s Individual Value's\n" +
        f"HP: {self.IV_HP}\n" +
        f"Attack: {self.IV_ATK}\n" +
        f"Defense: {self.IV_DEF}\n" +
        f"Speed: {self.IV_SPD}\n" +
        f"Sp. Attack: {self.IV_SP_ATK}\n" +
        f"Sp. Defense: {self.IV_SP_DEF}\n")

    ##Disply EV's function
    def display_EV(self):
        print(f"{type(self).__name__}'s Effort Value's\n" +
        f"HP: {self.EV_HP}\n" +
        f"Attack: {self.EV_ATK}\n" +
        f"Defense: {self.EV_DEF}\n" +
        f"Speed: {self.EV_SPD}\n" +
        f"Sp. Attack: {self.EV_SP_ATK}\n" +
        f"Sp. Defense: {self.EV_SP_DEF}\n")

    ##Display battle stats
    def display_stats(self):
        print(f"Species: {type(self).__name__}\n" +
        f"Owner: {self.OWNER}\n" +
        f"Level: {self.LVL}\n" +
        f"Type: {self.TYPE}\n" +
        f"Nature: {self.nature}\n" +
        f"HP: {self.HP}\n" +
        f"Attack: {self.ATK}\n" +
        f"Defense: {self.DEF}\n" +
        f"Speed: {self.SPD}\n" +
        f"Sp. Attack: {self.SP_ATK}\n" +
        f"Sp. Defense: {self.SP_DEF}\n")



class Bulbasaur(Pokemon):
    def __init__(self, level, owner):
        self.set_IV()
        self.set_EV()
        self.set_nature()
        self.LVL = level
        self.OWNER = owner
        self.TYPE = "Grass"
        #BASE STATS
        self.BASE_HP = 45
        self.BASE_ATK = 49
        self.BASE_DEF = 49
        self.BASE_SP_ATK = 65
        self.BASE_SP_DEF = 65
        self.BASE_SPD = 45
        self.set_stats()

class Charmander(Pokemon):
    def __init__(self, level, owner):
        self.set_IV()
        self.set_EV()
        self.set_nature()
        self.LVL = level
        self.OWNER = owner
        self.TYPE = "Fire"
        #BASE STATS
        self.BASE_HP = 39
        self.BASE_ATK = 52
        self.BASE_DEF = 43
        self.BASE_SP_ATK = 60
        self.BASE_SP_DEF = 50
        self.BASE_SPD = 65
        self.set_stats()

class Squirtle(Pokemon):
    def __init__(self, level, owner):
        self.set_IV()
        self.set_EV()
        self.set_nature()
        self.LVL = level
        self.OWNER = owner
        self.TYPE = "Water"
        #BASE STATS
        self.BASE_HP = 44
        self.BASE_ATK = 48
        self.BASE_DEF = 65
        self.BASE_SP_ATK = 50
        self.BASE_SP_DEF = 64
        self.BASE_SPD = 43
        self.set_stats()


user_name = input()
rival_name = input()
starter = input()

while True:
    if int(starter) == 1:
        starter = Bulbasaur(5, user_name)
        rival = Charmander(5, rival_name)
        break
    elif int(starter) == 2:
        starter = Squirtle(5, user_name)
        rival = Bulbasaur(5, rival_name)
        break
    elif int(starter) == 3:
        starter = Charmander(5, user_name)
        rival = Squirtle(5, rival_name)

starter.display_stats()
rival.display_stats()
