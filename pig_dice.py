import random

player_score = 0
computer_score = 0

player_total = 0
computer_total = 0

game = True

while game == True:
    player_dice = random.randint(1,6)
    computer_dice = random.randint(1,6)
    computer_choice = random.randint(1,2)

    player_choice = input("Roll or Bank? ")

    if player_choice == "Roll" or "roll" or "r":
        if player_dice != 1:
            print("Dice: {}".format(player_dice))
            player_score = player_dice
            print("Your score is: {}".format(player_score))

            player_total += player_score
            print("Total: {}".format(player_total))

        else:
            player_score = 0
            print("That's too bad.")
            player_total += player_score
            print("Total: {}".format(player_total))
        
    else:
        print("End the turn")

    print("==================================")

    if computer_choice == 1:
        print("Computer chose to Roll")

        if computer_dice != 1:
            print("Computer Rolled", computer_dice)
            computer_score = computer_dice
            print("Computer Score is {}".format(computer_score))
            print("Computer Total: {}".format(computer_total))

        else:
            computer_score = 0
            print("Computer Rolled 1.")
            print("Computer Total: {}".format(computer_total))

        computer_total += computer_score
        
    else:
        print("Computer chose to Bank.")

    print("==================================")

    if player_total >= 100:
        print("You won!")
        gameActive = False
    
    else:
        pass
  
    if computer_total >= 100:
        print("Computer won!")
        gameActive = False

    else:
        pass
