import Stats
import math
import Moves


class Bulbasaur(Stats.Pokemon):
    def __init__(self, level, owner, wild):
        super().__init__(level)
        self.image = 'poke_pic/bulbasaur.png'
        self.wild = wild
        self.atk_stat_stage = 0
        self.def_stat_stage = 0
        self.set_iv()
        self.set_ev()
        self.set_nature()
        self.owner = owner
        self.exp = math.floor(
            (1.2 * (self.lvl ** 3)) - (15 * (self.lvl ** 2)) + (100 * self.lvl) - 140)
        self.growth_group = "med_slow"
        self.type = "Grass"
        self.BASE_EXP = 64
        self.BASE_HP = 45
        self.BASE_ATK = 49
        self.BASE_DEF = 49
        self.BASE_SP_ATK = 65
        self.BASE_SP_DEF = 65
        self.BASE_SPD = 45
        self.set_stats()
        self.attack_1 = Moves.Tackle()
        self.attack_2 = Moves.Growl()
        self.attack_3 = None
        self.attack_4 = None

    @staticmethod
    def effort(target):
        target.ev_sp_atk += 1


class Charmander(Stats.Pokemon):
    def __init__(self, level, owner, wild):
        super().__init__(level)
        self.wild = wild
        self.image = 'poke_pic/charmander.png'
        self.atk_stat_stage = 0
        self.def_stat_stage = 0
        self.set_iv()
        self.set_ev()
        self.set_nature()
        self.owner = owner
        self.exp = math.floor(
            (1.2 * (self.lvl ** 3)) - (15 * (self.lvl ** 2)) + (100 * self.lvl) - 140)
        self.growth_group = "med_slow"
        self.type = "Fire"
        self.BASE_EXP = 62
        self.BASE_HP = 39
        self.BASE_ATK = 52
        self.BASE_DEF = 43
        self.BASE_SP_ATK = 60
        self.BASE_SP_DEF = 50
        self.BASE_SPD = 65
        self.set_stats()
        self.attack_1 = Moves.Scratch()
        self.attack_2 = Moves.Growl()
        self.attack_3 = None
        self.attack_4 = None

    @staticmethod
    def effort(target):
        target.ev_spd += 1


class Squirtle(Stats.Pokemon):
    def __init__(self, level, owner, wild):
        super().__init__(level)
        self.wild = wild
        self.image = 'poke_pic/squirtle.png'
        self.atk_stat_stage = 0
        self.def_stat_stage = 0
        self.set_iv()
        self.set_ev()
        self.set_nature()
        self.owner = owner
        self.exp = math.floor(
            (1.2 * (self.lvl ** 3)) - (15 * (self.lvl ** 2)) + (100 * self.lvl) - 140)
        self.growth_group = "med_slow"
        self.type = "Water"
        self.BASE_EXP = 63
        self.BASE_HP = 44
        self.BASE_ATK = 48
        self.BASE_DEF = 65
        self.BASE_SP_ATK = 50
        self.BASE_SP_DEF = 64
        self.BASE_SPD = 43
        self.set_stats()
        self.attack_1 = Moves.Tackle()
        self.attack_2 = Moves.Tail_Whip()
        self.attack_3 = None
        self.attack_4 = None

    @staticmethod
    def effort(target):
        target.ev_def += 1


# Create the party to hold Pokemon
class party():
    def __init__ (self, starter):
        self.party = [starter]

    # Create function to add Pokemon to party
    def add_to_party(self, pokemon):
        if len(self.party) < 6:
            self.party.append(pokemon)
        else:
            print("Your party is full")
            

    # Create function to swap pokemon to front of party
    def swap_to_main(self, pokemon):
        self.party.insert(0, self.party.pop(pokemon))
        self.party.insert(pokemon, self.party.pop(1))
