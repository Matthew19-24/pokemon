import random

class Pokemon:
    def __init__(self, level):
        self.LVL = level
      
    def IV_set(self):
        self.IV_HP = random.randrange(0,32)
        self.IV_ATK = random.randrange(0,32)
        self.IV_DEF = random.randrange(0,32)
        self.IV_SP_ATK = random.randrange(0,32)
        self.IV_SP_DEF = random.randrange(0,32)
        self.IV_SP_SPD = random.randrange(0,32)
        
    def STATS(self):
        print(f"Species: {type(self).__name__}\n" +
        f"Owner: {self.OWNER}\n" +
        f"Type: {self.TYPE}\n" +
        f"Level: {self.LVL}\n" +
        f"HP: {self.HP}\n" 
        f"Attack: {self.ATK}\n" +
        f"Deffense: {self.DEF}\n" +
        f"Special Attack: {self.SP_ATK}\n" +
        f"Special Deffense: {self.SP_DEF}\n" +
        f"Speed: {self.SPD}\n\n")
        
class Bulbasaur(Pokemon):
    def __init__(self, level, owner):
        self.LVL = level
        self.TYPE = "Grass"
        self.OWNER = owner
    
        #BASE STATS
        self.BASE_HP = 45
        self.BASE_ATK = 49
        self.BASE_DEF = 49
        self.BASE_SP_ATK = 65
        self.BASE_SP_DEF = 65
        self.BASE_SPD = 45

        self.IV_set()

bulb = Bulbasaur(3, "Matthew")
