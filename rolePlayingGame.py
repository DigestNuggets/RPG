from random import randint
import random
from time import sleep
PAUSE = 1
user_health = 200
opponent_health = 200
hit = True
opp_hit = True
constant = True
rematch = True
bag = ["protractor", "pencil", "rubber"]
weather = ["rainy", "sunny", "foggy"]
room = ["Coleman Hall", "S16", "E5", "MU9"]
print("Teacher Fighting Simulator\n")
sleep(PAUSE)

start = True
while start == True:
    character = int(input(
        "Choose your character:\n1. Mr Ayebare\n2. Mr Keaney\n3. Mr Cundick\n4. Mr Carr"))
    sleep(PAUSE)
    start = False


while opponent_health > 0 and opponent_health > 0 and rematch == True:

    if character == 1:
        character_name = "Mr Ayebare"
        opponent = randint(2, 4)
        user_type = "fire"
        choice = int(
            input("\nChoose your move:\n1. Body Slam\n2. Visualise, factorise\n3. Fire Blast\n4. Earthquake"))
        if choice == 1:
            damage = 80
            accuracy = 66
            type = "normal"
            move = "Body Slam"
        elif choice == 2:
            damage = 100
            accuracy = 25
            type = "fire"
            move = "Visualise, Factorise"
        elif choice == 3:
            damage = 40
            accuracy = 100
            type = "fire"
            move = "Fire Blast"
        else:
            damage = 90
            accuracy = 90
            type = "ground"
            move = "Earthquake"
    elif character == 2:
        character_name = "Mr Keaney"
        list = [1, 3, 4]
        opponent = random.choice(list)
        user_type = "electric"
        choice = int(input(
            "\nChoose your move:\n1. Thunderbolt\n2. Charge Beam\n3. Burn in fire and blood and anguish\n4. Thunder Charge"))
        if choice == 1:
            damage = 80
            accuracy = 80
            type = "electric"
            move = "Thunderbolt"
        elif choice == 2:
            damage = 40
            accuracy = 90
            type = "electric"
            move = "Charge Beam"
        if choice == 3:
            damage = 80
            accuracy = 100
            type = "fire"
            move = "Burn in fire and blood and anguish"
        else:
            damage = 90
            accuracy = 70
            type = "electric"
            move = "Thunder Charge"
    elif character == 3:
        character_name = "Mr Cundick"
        list = [1, 2, 4]
        opponent = random.choice(list)
        user_type = "normal"
        choice = int(
            input("\nChoose your move:\n1. Rugby tackle\n2. Grunt\n3. Stomp\n4. Growl"))
        if choice == 1:
            damage = 95
            accuracy = 100
            type = "fighting"
            move = "Rugby Tackle"
        elif choice == 2:
            damage = 40
            accuracy = 100
            type = "fighting"
            move = "Grunt"
        elif choice == 3:
            damage = 50
            accuracy = 95
            type = "normal"
            move = "Stomp"
        else:
            damage = 30
            accuracy = 90
            type = "normal"
            move = "Growl"
    elif character == 4:
        character_name = "Mr Carr"
        opponent = randint(1, 3)
        user_type = "grass"
        choice = int(
            input("\nChoose your move:\n1. Leaf Storm\n2. Hit and Run\n3. Leaf Blade\n4. Close Combat"))
        if choice == 1:
            damage = 75
            accuracy = 90
            type = "grass"
            move = "Leaf Storm"
        elif choice == 2:
            damage = 100
            accuracy = 95
            type = "fighting"
            move = "Hit and Run"
        elif choice == 3:
            damage = 60
            accuracy = 100
            type = "grass"
            move = "Leaf Blade"
        else:
            damage = 100
            accuracy = 80
            type = "fighting"
            move = "Close Combat"

    while constant == True:
        if opponent == 1:
            opponent_name = "Mr Ayebare"
            constant = False
        elif opponent == 2:
            opponent_name = "Mr Keaney"
            constant = False
        elif opponent == 3:
            opponent_name = "Mr Cundick"
            constant = False
        elif opponent == 4:
            opponent_name = "Mr Carr"
            constant = False

    sleep(PAUSE)

    weather = random.choice(weather)
    room = random.choice(room)
    print("\nYou are", character_name, "and your opponent is", opponent_name)
    print("It is a", weather, "day in" ,room)
    sleep(PAUSE)
    print("\n", character_name, "health:", user_health)
    sleep(PAUSE)
    print(opponent_name, "health:", opponent_health)

    if opponent == 1:
        opponent_type = "fire"
        opp_choice = randint(1, 4)

        if opp_choice == 1:
            opp_damage = 80
            opp_accuracy = 66
            opp_type = "normal"
            opp_move = "Body Slam"
        elif opp_choice == 2:
            opp_damage = 100
            opp_accuracy = 25
            opp_type = "fire"
            opp_type = "Fire Blast"
        elif opp_choice == 3:
            opp_damage = 40
            opp_accuracy = 100
            opp_type = "fire"
            opp_move = "Visualise, Factorise"
        else:
            opp_damage = 90
            opp_accuracy = 90
            opp_type = "ground"
            opp_move = "Earthquake"

    elif opponent == 2:
        opponent_type = "electric"
        opp_choice = randint(1, 4)

        if opp_choice == 1:
            opp_damage = 80
            opp_accuracy = 80
            opp_type = "electric"
            opp_move = "Thunderbolt"
        elif opp_choice == 2:
            opp_damage = 40
            opp_accuracy = 90
            opp_type = "electric"
            opp_move = "Thunder Charge"
        if choice == 3:
            opp_damage = 80
            opp_accuracy = 100
            opp_type = "fire"
            opp_move = "Burn in Fire and Blood and Anguish"

        else:
            opp_damage = 90
            opp_accuracy = 70
            opp_type = "electric"
            opp_move = "Charge Beam"

    elif opponent == 3:
        opp_choice = randint(1, 4)
        opponent_type = "normal"

        if opp_choice == 1:
            opp_damage = 95
            opp_accuracy = 100
            opp_type = "fighting"
            opp_move = "Grunt"
        elif opp_choice == 2:
            opp_damage = 40
            opp_accuracy = 100
            opp_type = "fighting"
            opp_move = "Growl"
        elif opp_choice == 3:
            opp_damage = 50
            opp_accuracy = 95
            opp_type = "normal"
            opp_move = "Stomp"
        else:
            opp_damage = 30
            opp_accuracy = 90
            opp_type = "normal"
            opp_move = "Rugby Tackle"

    elif opponent == 4:
        opp_choice = randint(1, 4)
        opponent_type = "grass"

        if opp_choice == 1:
            opp_damage = 75
            opp_accuracy = 90
            opp_type = "grass"
            opp_move = "Leaf Blade"
        elif opp_choice == 2:
            opp_damage = 100
            opp_accuracy = 95
            opp_type = "fighting"
            opp_move = "Close Combat"

        elif opp_choice == 3:
            opp_damage = 60
            opp_accuracy = 100
            opp_type = "grass"
            opp_move = "Leaf Blade"
        else:
            opp_damage = 100
            opp_accuracy = 80
            opp_type = "fighting"
            opp_move = "Hit and Run"

    if type == opponent_type:
        effective = "not very effective"
    elif type == "fire" and opponent_type == "grass":
        effective = "super effective"
    elif type == "normal" and opponent_type == "fighting":
        effective = "not very effective"
    elif type == "electric" and opponent_type == "ground":
        effective = "not very effective"
    elif type == "grass" and opponent_type == "fire":
        effective = "not very effective"
    elif type == "fighting" and opponent_type == "normal":
        effective = "super effective"
    else:
        effective = "effective"

    if opp_type == user_type:
        effective2 = "not very effective"
    elif opp_type == "fire" and user_type == "grass":
        effective2 = "super effective"
    elif opp_type == "normal" and user_type == "fighting":
        effective2 = "not very effective"
    elif opp_type == "electric" and user_type == "ground":
        effective2 = "not very effective"
    elif opp_type == "grass" and user_type == "fire":
        effective2 = "not very effective"
    elif opp_type == "fighting" and user_type == "normal":
        effective2 = "super effective"
    else:
        effective2 = "effective"

    print("\n\n", character_name, "used", move,
          "and", opponent_name, "used", opp_move)

    if accuracy == 95:
        real_acc = randint(1, 20)
        if real_acc == 1:
            hit = False
            sleep(PAUSE)
            sleep(PAUSE)
            temporary_character_name = character_name + "'s"
            print(temporary_character_name, "move missed!")
        else:
            hit = True
    elif accuracy == 66:
        real_acc = randint(1, 3)
        if real_acc == 1:
            hit = False
            sleep(PAUSE)
            sleep(PAUSE)
            temporary_character_name = character_name + "'s"
            print(temporary_character_name, "move missed!")
        else:
            hit = True
    elif accuracy == 25:
        real_acc = randint(1, 4)
        if real_acc != 1:
            hit = False
            sleep(PAUSE)
            sleep(PAUSE)
            temporary_character_name = character_name + "'s"
            print(temporary_character_name, "move missed!")
        else:
            hit = True
    elif accuracy == 90:
        real_acc = randint(1, 10)
        if real_acc == 1:
            hit = False
            sleep(PAUSE)
            sleep(PAUSE)
            temporary_character_name = character_name + "'s"
            print(temporary_character_name, "move missed!")
        else:
            hit = True
    elif accuracy == 80:
        real_acc = randint(1, 5)
        if real_acc == 1:
            hit = False
            sleep(PAUSE)
            sleep(PAUSE)
            temporary_character_name = character_name + "'s"
            print(temporary_character_name, "move missed!")
        else:
            hit = True
    elif accuracy == 60:
        real_acc = randint(1, 10)
        if real_acc == 1 or real_acc == 2 or real_acc == 4 or real_acc == 3:
            hit = False
            sleep(PAUSE)
            sleep(PAUSE)
            temporary_character_name = character_name + "'s"
            print(temporary_character_name, "move missed!")
        else:
            hit = True
    elif accuracy == 70:
        real_acc = randint(1, 10)
        if real_acc != 1 or real_acc != 2 or real_acc != 3:
            hit = False
            sleep(PAUSE)
            sleep(PAUSE)
            temporary_character_name = character_name + "'s"
            print(temporary_character_name, "move missed!")
        else:
            hit = True

    if opp_accuracy == 95:
        opp_real_acc = randint(1, 20)
        if opp_real_acc == 1:
            opp_hit = False
            sleep(PAUSE)
            sleep(PAUSE)
            temporary_opponent_name = opponent_name + "'s"
            print(temporary_opponent_name, "move missed!")
        else:
            hit = True
    elif opp_accuracy == 66:
        opp_real_acc = randint(1, 3)
        if opp_real_acc == 1:
            opp_hit = False
            sleep(PAUSE)
            sleep(PAUSE)
            temporary_opponent_name = opponent_name + "'s"
            print(temporary_opponent_name, "move missed!")
        else:
            hit = True
    elif opp_accuracy == 25:
        opp_real_acc = randint(1, 4)
        if opp_real_acc != 1:
            opp_hit = False
            sleep(PAUSE)
            sleep(PAUSE)
            temporary_opponent_name = opponent_name + "'s"
            print(temporary_opponent_name, "move missed!")
        else:
            hit = True
    elif opp_accuracy == 90:
        opp_real_acc = randint(1, 10)
        if opp_real_acc == 1:
            opp_hit = False
            sleep(PAUSE)
            sleep(PAUSE)
            temporary_opponent_name = opponent_name + "'s"
            print(temporary_opponent_name, "move missed!")
        else:
            hit = True
    elif opp_accuracy == 80:
        opp_real_acc = randint(1, 5)
        if opp_real_acc == 1:
            opp_hit = False
            sleep(PAUSE)
            sleep(PAUSE)
            temporary_opponent_name = opponent_name + "'s"
            print(temporary_opponent_name, "move missed!")
        else:
            hit = True
    elif opp_accuracy == 60:
        opp_real_acc = randint(1, 10)
        if opp_real_acc == 1 or opp_real_acc == 2 or opp_real_acc == 4 or opp_real_acc == 3:
            opp_hit = False
            sleep(PAUSE)
            sleep(PAUSE)
            temporary_opponent_name = opponent_name + "'s"
            print(temporary_opponent_name, "move missed!")
        else:
            hit = True
    elif opp_accuracy == 70:
        opp_real_acc = randint(1, 10)
        if opp_real_acc != 1 or real_acc != 2 or real_acc != 3:
            opp_hit = False
            sleep(PAUSE)
            sleep(PAUSE)
            temporary_opponent_name = opponent_name + "'s"
            print(temporary_opponent_name, "move missed!")
        else:
            opp_hit = True
    else:
        hit = True

    if hit == True:
        sleep(PAUSE)
        sleep(PAUSE)
        print(character_name, "used", move, "and it was", effective)

    if opp_hit == True:
        sleep(PAUSE)
        sleep(PAUSE)
        print(opponent_name, "used", opp_move, "and it was", effective2)
    sleep(PAUSE)
    sleep(PAUSE)

    if effective == "not very effective":
        damage = damage / 2
    elif effective == "super effective":
        damage = damage * 2

    if effective2 == "not very effective":
        opp_damage = opp_damage / 2
    elif effective == "super effective":
        opp_damage = opp_damage * 2

        item_used = random.choice(bag)
        if item_used == "rubber":
            damage += 20
        elif item_used == "protractor":
            damage += 25
        elif item_used == "pencil":
            damage += 30
    

    if hit == True:
        opponent_health -= damage
    if opp_hit == True:
        user_health -= opp_damage
    print(character_name, "health:", user_health)
    print(opponent_name, "health:", opponent_health)


while user_health <= 0 or opponent_health <= 0:
    if user_health <= 0:
        sleep(PAUSE)
        print(character_name, "unfortunately died and you unfortunately lost the game")
    elif opponent_health <= 0:
        sleep(PAUSE)
        print(opponent_name, "died. Congratulations. You won the round!")
    rematch_option = str(input("Would you like to rematch. y/n"))
    if rematch_option == "y":
        rematch = True
        start = True
        user_health = 200
        opponent_health = 200
    elif rematch_option == "n":
        print("Thank you for playing")
        user_health = 200
        opponent_health = 200
        rematch = False
