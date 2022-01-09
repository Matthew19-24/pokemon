import random
from time import sleep


# Check if targets speed attacks first or last
def targets_attack_first(user, target):
    if user.spd_stat < target.spd_stat:
        atk = random.randrange(1, 3)
        if atk == 1:
            target.attack1(user)
        elif atk == 2:
            target.attack2(user)


# Check if targets speed attacks last or first
def targets_attack_second(user, target):
    if user.spd_stat >= target.spd_stat:
        atk = random.randrange(1, 3)
        if atk == 1:
            target.attack1(user)
        elif atk == 2:
            target.attack2(user)


def battle(user, target):
    print(f"{target.owner} wants to battle!")
    sleep(1.5)
    print(f"\n{target.owner} sent out {target.name}! (HP: {target.hp_stat})")
    sleep(1.5)
    print(f"{user.owner} sent out {user.name}! (HP: {user.hp_stat})")

    while user.hp_stat > 0 and target.hp_stat > 0:
        # Determine users attack
        while True:
            sleep(1.5)
            x = input(f'\nPress 1 to use {user.attack_1.name}' +
                      f'\nPress 2 to use {user.attack_2.name}')

            # Determine attack order based on speed, calling order functions
            if x == "1":
                targets_attack_first(user, target)
                if target.hp_stat <= 0 or user.hp_stat <= 0:
                    break
                user.attack1(target)
                if target.hp_stat <= 0 or user.hp_stat <= 0:
                    break
                targets_attack_second(user, target)
                break
            elif x == "2":
                targets_attack_first(user, target)
                if target.hp_stat <= 0 or user.hp_stat <= 0:
                    break
                user.attack2(target)
                if target.hp_stat <= 0 or user.hp_stat <= 0:
                    break
                targets_attack_second(user, target)
                break
            else:
                sleep(1.5)
                print('\nInvalid entry: Try again')

    # Determine the winner
    if user.hp_stat > target.hp_stat:
        print(f"\nEnemy {target.name} fainted!")
        sleep(1)
        user.exp_gain((user.BASE_EXP * target.lvl) * target.wild_eq / 7)
        target.effort(user)
    else:
        print(f"\n{user.name} fainted!")
        sleep(1)
        print(f"{user.owner} has no more Pokemon and blacked out!")
        sleep(5)
        exit()

    # Reset stat stages after battle
    user.atk_stat_stage = 0
    user.def_stat_stage = 0
    target.atk_stat_stage = 0
    target.def_stat_stage = 0
