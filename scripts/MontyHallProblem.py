import random

win = 0
counter = 0
win_rate = 0
retry = True

while retry:
    jackpot = ["car", "goat", "goat"]
    choice_array = ["", "", ""]
    random.shuffle(jackpot)

    print "\nSuppose you\'re on a game show, there are 3 doors, behind which are two goats and a car."
    print(choice_array)

    # PHASE 1 =======================================================================
    choice_1 = None
    while choice_1 != "1" and choice_1 != "2" and choice_1 != "3":
        choice_1 = raw_input("Which of the 3 doors do you choose? ")
    choice_1 = int(choice_1)-1
    choice_array[choice_1] = "X"
    print(choice_array)

    # PHASE 2 =======================================================================
    print ("The host, Monty Hall, will then open one of the other doors.")
    host = True
    random_choice = None
    while host:
        random_choice = random.randint(0, 2)
        if (choice_1 != random_choice) and (jackpot[random_choice] != "car"):
            host = False
    choice_array[random_choice] = jackpot[random_choice]
    print(choice_array)

    # PHASE 3 =======================================================================
    choice_2 = None
    while choice_2 != str(choice_array.index('X')+1) and choice_2 != str(choice_array.index('')+1):
        choice_2 = raw_input("Do you stay with original door(door " + str(choice_array.index('X')+1) + ")"
                             ", or switch (door " + str(choice_array.index('')+1) + ")? ")
    choice_2 = int(choice_2)-1
    print jackpot

    # PHASE 4 =======================================================================
    counter += 1
    if jackpot[choice_2] == "car":
        print "You win!"
        win += 1
    else:
        print "You lose!"

    # RESULTS =======================================================================
    win_rate = 100 * float(win)/float(counter)
    print "Coins: " + str(counter) + " Win rate: " + str(round(win_rate, 2)) + "%"

    choice_3 = raw_input("Insert coin? (press Enter)")
    retry = True if choice_3 == "" else False









