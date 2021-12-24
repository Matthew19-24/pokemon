import random
import math

class Pokemon:
    def __init__(self, level):
        self.LVL = level
        self.BASE_HP = 0
        self.BASE_ATK = 0
        self.BASE_DEF = 0
        self.BASE_SP_ATK = 0
        self.BASE_SP_DEF = 0
        self.BASE_SPD = 0
        self.OWNER = 0
        self.SPECIES = 0
        self.TYPE = 0


    ##Randomize IV stats
    def set_IV(self):
        self.IV_HP = random.randrange(0,32)
        self.IV_ATK = random.randrange(0,32)
        self.IV_DEF = random.randrange(0,32)
        self.IV_SPD = random.randrange(0,32)
        self.IV_SP_ATK = random.randrange(0,32)
        self.IV_SP_DEF = random.randrange(0,32)

    ##Declaring blank EV variables
    def set_EV(self):
        self.EV_HP = 0
        self.EV_ATK = 0
        self.EV_DEF = 0
        self.EV_SPD = 0
        self.EV_SP_ATK = 0
        self.EV_SP_DEF = 0

    ##Set nature variables
    def set_nature(self):
        self.nature_atk = 1
        self.nature_def = 1
        self.nature_spd = 1
        self.nature_sp_atk = 1
        self.nature_sp_def = 1

        #Randomize nature
        self.nature_list = ["Adamant", "Bashful", "Brave", "Bold", "Calm", "Careful", "Docile", "Gentle", "Hardy", "Hasty", "Impish", "Jolly", "Lax", "Lonely", "Mild", "Modest", "Naive", "Naughty", "Quiet", "Quirky", "Rash", "Relaxed", "Sassy", "Serious", "Timid"]
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
        self.SPECIES = Bulbasaur
        self.TYPE = "Grass"
    
        #BASE STATS
        self.BASE_HP = 45
        self.BASE_ATK = 49
        self.BASE_DEF = 49
        self.BASE_SP_ATK = 65
        self.BASE_SP_DEF = 65
        self.BASE_SPD = 45

        self.set_stats()

bulb = Bulbasaur(5, "Matthew")

bulb.display_IV()
bulb.display_EV()
bulb.display_stats()
