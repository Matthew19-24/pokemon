import Stats

user_name = input("Username: ")
rival_name = input("Rival Name: ")
starter_num = input("\nPress [1] for Bulbasaur, the grass type,\n" +
                    "Press [2] for Squirtle, the water type,\n" +
                    "Press [3] for Charmander, the fire type.\n\n")

while True:
    if int(starter_num) == 1:
        starter = Stats.Bulbasaur(5, user_name)
        rival = Stats.Charmander(5, rival_name)
        break
    elif int(starter_num) == 2:
        starter = Stats.Squirtle(5, user_name)
        rival = Stats.Bulbasaur(5, rival_name)
        break
    elif int(starter_num) == 3:
        starter = Stats.Charmander(5, user_name)
        rival = Stats.Squirtle(5, rival_name)
        break

starter.display_stats()
rival.display_stats()
