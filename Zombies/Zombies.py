#
#  Z o m b i e s . p y
#
#  By Edward Forgacs & Sejin Oh.
#


# Player

class Player:
    strength = 10
    defense = 10
    health = 100


# Inventory items


class Inventory:
    gun = False
    shield = False
    candies = False
    bullets = 0


# Enemies

# TODO: Implement HP for Zombie.

class Enemies:
    zombie_health = 100
    police_zombie_health = 200

# NPCs


class NPCs:
    man = True


def choose_path(number_of_paths):
    choice = 0
    while choice < 1 or choice > number_of_paths:
        print('1 to ' + str(number_of_paths) + '> ')
        try:
            choice = int(input())
        except ValueError:
            pass
    print('')
    print('')
    return int(choice)


def press_enter_to_continue():
    print('Press enter to continue.')
    input()


def character_select():
    print("Please select your character.")
    print("  1 Strength (easier to attack enemies)")
    print("  2 Defense (more damage can be taken)")
    # print("  3 Stealth (easier to hide among enemies)")
    # print("  4 Speed (easier to evade enemies)")
    path = choose_path(2)
    if path == 1:
        print("You have chosen strength.")
        input()
        Player.strength = 20
    if path == 2:
        print("You have chosen defense.")
        input()
        Player.defense = 20
    intro()


def intro():
    print('You are in the middle of the plaza. You notice that people around you have suddenly changed into zombies.')
    print('')
    press_enter_to_continue()
    plaza()


def plaza():
    print('In front of you is a horde of zombies.')
    print("On your left side a house.")
    print("Leaning against the house is a bicycle.")
    print('')
    print('What will you do?')
    print('  1 Remain standing in the street.')
    print('  2 Try to escape using the bicycle.')
    print('  3 Enter the house.')
    path = choose_path(3)
    if path == 1:
        remain_standing_in_street()
    if path == 2:
        escape_using_bicycle()
    if path == 3:
        enter_house()


def remain_standing_in_street():
    if Player.strength >= 20:
        print("You barely escaped from the zombies.")
        Player.health -= 70
        show_player_health()
    if Player.defense >= 20:
        print("You barely escaped from the zombies. Your defense helped you escape.")
        Player.health -= 50
        show_player_health()
    print('')
    print('What will you do?')
    print('  1 Go to the plaza.')
    path = choose_path(1)
    if path == 1:
        plaza()


# Display status functions

def show_player_health():
    print("")
    print("Your health is currently " + str(Player.health) + ".")
    print("")
    input()


def show_player_strength():
    print("")
    print("Your strength is currently " + str(Player.strength) + ".")
    input()


def show_player_defense():
    print("")
    print("Your defense is currently " + str(Player.defense) + ".")
    input()


def show_inventory_item_remaining(inventory_item, inventory_item_value):
    print("")
    print("You have " + str(inventory_item_value) + " " + str(inventory_item) + " remaining.")


def enter_house():
    pass
    # TODO: implement enter_house


def north_of_plaza():
    print("Oh no! A truck is heading your way!")
    input()
    print("The truck strikes you, toppling you from your bicycle.")
    input()
    Player.health -= 70
    show_player_health()
    input()
    print("Oh no! A zombie is coming!")
    input()
    print("The zombie has eaten you.")
    return death()


def steal_police_officers_gun():
    print("You take the gun and 10 bullets from the infected police officer.")
    Inventory.gun = True
    Player.strength += 100
    show_player_strength()
    east_of_plaza()


def steal_police_officers_shield():
    print("You take the shield from the infected police officer.")
    Inventory.shield = True
    Player.strength += 10
    Player.defense += 100
    east_of_plaza()


def kill_zombie_with_gun():
    if Inventory.gun is True:
        print("You fire a bullet using your handgun at the zombie.")
        print("You killed the zombie.")
        Inventory.bullets -= 1
    if Inventory.gun is False:
        print("You don't have a gun.")
        fight_zombie()
    if Inventory.bullets == 0:
        print("You don't have any bullets.")


def kill_zombie_with_shield():
    if Inventory.shield is True:
        # TODO: Make an enter press needed for every 10 HP that an enemy has.
        print("You hit the zombie using the shield.")
        input()
        print("You hit the zombie using the shield.")
        input()
        print("You hit the zombie using the shield.")
        input()
        print("You hit the zombie using the shield.")
        input()
        print("You hit the zombie using the shield.")
        input()
        print("You hit the zombie using the shield.")
        input()
        print("You hit the zombie using the shield.")
        input()
        print("You hit the zombie using the shield.")
        input()
        print("You hit the zombie using the shield.")
        input()
        print("You hit the zombie using the shield.")
        input()
        print("You finally killed the zombie.")

    if Inventory.shield is False:
        print("You don't have a shield.")
        fight_zombie()


def kill_zombie_with_bare_hands():
    # TODO: When fist fighting with bare hands, a keypress is needed for every 5 HP. Player takes 30 damage per fight.
    print("You attack the zombie with your bare hands.")


def fight_zombie():
    # TODO: When done fighting, sends player back to original location.
    # TODO: Figure out decision tree for current weapons.
    print("What will you use to fight the zombie?")
    print('  1 Your bare hands.')
    print('  2 Your gun.')
    print('  3 Your shield.')
    path = choose_path(3)
    if path == 1:
        kill_zombie_with_bare_hands()
    if path == 2:
        kill_zombie_with_gun()
    if path == 3:
        kill_zombie_with_shield()

# deprecated version of fight_zombie() function

# def fight_zombie():
#     print("What will you use to fight the zombie?")
#     if not Inventory.gun and not Inventory.shield:
#         print('  1 Your bare hands.')
#         path = choose_path()
#         if path == 1:
#             kill_zombie_with_bare_hands()
#     if Inventory.gun and not Inventory.shield:
#         print('  2 Your gun.')
#         if path == 2:
#             kill_zombie_with_gun()
#     if Inventory.shield and not Inventory.gun:
#         print('  2 Your shield.')
#         if path == 2:
#             kill_zombie_with_shield()


def enter_bank():
    print("You are inside the bank.")
    print("There is a police officer who has just been bitten by a zombie.")
    print("He appears to be infected!")
    if Inventory.gun is False and Inventory.shield is False:
        what_will_you_do()
        print('  1 Leave the bank.')
        print('  2 Steal the police officer\'s gun.')
        print('  3 Steal the police officer\'s riot shield.')
        path = choose_path(2)
        if path == 1:
            east_of_plaza()
        if path == 2:
            steal_police_officers_gun()
        if path == 3:
            steal_police_officers_shield()
    if Inventory.gun is True or Inventory.shield is True:
        print("Oh no! The zombie police officer is attacking you.")
        what_will_you_do()
        print('  1 Attack the zombie officer.')
        print('  2 Run away.')
        path = choose_path(2)
        if path == 1:
            fight_zombie()
        if path == 2:
            east_of_plaza()


def east_of_plaza():
    print("There is a bank and a candy store in front of you.")
    what_will_you_do()
    print('  1 Enter the bank.')
    print('  2 Enter the candy store.')
    print('  3 Go back to the plaza')
    path = choose_path(2)
    if path == 1:
        enter_bank()
    if path == 2:
        candy_store()
    if path == 3:
        plaza()


def what_will_you_do():
    print("")
    print('What will you do?')


def eat_candies():
    print("You have eaten the candies.")
    print("Your health increases by 50.")
    Player.health += 50
    show_player_health()
    east_of_plaza()


def candy_store():
    print("Do you want to eat some candies?")
    print('  1 Yes')
    print('  2 No')
    path = choose_path(2)
    if path == 1:
        eat_candies()
    if path == 2:
        east_of_plaza()


def south_of_road():
    pass
    # TODO: Implement south_of_road()


def west_of_road():
    pass
    # TODO: Implement west_of_road()


def escape_using_bicycle():
    print('You get on the bicycle.')
    print('')
    print('What will you do?')
    print('  1 Go north.')
    print('  2 Go east.')
    print('  3 Go south.')
    print('  4 Go west.')
    path = choose_path(2)
    if path == 1:
        north_of_plaza()
    if path == 2:
        east_of_plaza()
    if path == 3:
        south_of_road()
    if path == 4:
        west_of_road()


def death():
    print("")
    print("Your health is currently 0 percent.")
    input()
    print('')
    print('You are dead.')
    return


while True:

    # Start the game
    character_select()

    print('')
    print('Would you like to play again? Y/N')
    play_again = input()
    if play_again == 'Y' or play_again == 'y':
        continue
    if play_again == 'N' or play_again == 'n':
        break
    break
