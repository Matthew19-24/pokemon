import Battle
import Pokedex
import MyGUI
from time import sleep

# Get username
print("Oak:\tHello there!"), sleep(1)
print("\t\tWelcome to the world of POKéMON!"), sleep(1.7)
print("\t\tMy name is OAK!"), sleep(1.3)
print("\t\tPeople call me the POKéMON PROF!"), sleep(1.7)
print("\t\tThis world is inhabited by creatures called POKéMON!"), sleep(2.2)
print("\t\tFor some people, POKéMON are pets."), sleep(1.7)
print("\t\tOthers use them for fights."), sleep(1.7)
print("\t\tMyself..."), sleep(1)
print("\t\tI study POKéMON as a profession."), sleep(1.7)
print("\t\tFirst, what is your name?\n"), sleep(1.5)
user_name = MyGUI.get_name()
user_name = user_name.upper()

# Have user chose rivals name
print("\nOak:\tRight!"), sleep(1)
print(f"\t\tSo your name is {user_name}."), sleep(1.5)
print("\t\tThis is my grandson."), sleep(1.5)
print("\t\tHe's been your rival since you were a baby."), sleep(1.7)
print("\t\t...Erm, what is his name again?\n"), sleep(1.5)
rival_name = MyGUI.get_name()
rival_name = rival_name.upper()

# Dialog to end intro
print("\nOak:\tThat's right!"), sleep(1)
print(f"\t\tHis name is {rival_name}!"), sleep(1.5)
print(f"\t\t{user_name}! Your very own POKéMON legend is about to unfold!"), sleep(2)
print("\t\tA world of dreams and adventures with POKéMON awaits!"), sleep(2)
print("\t\tLet's go!"), sleep(1)

# Add more to the script
# Waking up and going to Prof Oaks
# starter_num = input("\nPress [1] for Bulbasaur, the grass type,\n" +
#                    "Press [2] for Squirtle, the water type,\n" +
#                    "Press [3] for Charmander, the fire type.\n\n")
starter_num = MyGUI.starter_pick()

while True:
    if starter_num == 1:
        starter = Pokedex.Bulbasaur(5, user_name, False)
        rival = Pokedex.Charmander(5, rival_name, False)
        break
    elif starter_num == 2:
        starter = Pokedex.Charmander(5, user_name, False)
        rival = Pokedex.Squirtle(5, rival_name, False)
        break
    elif starter_num == 3:
        starter = Pokedex.Squirtle(5, user_name, False)
        rival = Pokedex.Bulbasaur(5, rival_name, False)
        break
    else:
        starter_num = input("Invalid entry: Try again\n")

MyGUI.id_card(starter)
Battle.battle(starter, rival)
starter.hp_stat = starter.hp_full
rival.hp_stat = rival.hp_full
