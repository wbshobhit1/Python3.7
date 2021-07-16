# import random

#
# random_number = random.randint(0,5)
# # print(random_number)
#
# rand = random.random() *100
# print(rand)
#
# lst = ["mi","rcb","csk","rr", "kkr", "srh", "pk", "dc"]
# win = random.choice(lst)
# print(win)

# Excercise 6 ,Built a game name (Stone Paper Scissors)

import random

items = ["Stone", "Paper", "Scissors"]
computer_win = 0
player_win = 0
n = 0
while n < 10:

    comp = random.choice(items)
    player = input("Player Chosen input is :")
    if comp == "Stone" and player == "Paper":
        print("Computer input is", comp)
        player_win = player_win + 1
        print("YOU WIN\n")
    elif comp == "Paper" and player == "Stone":
        print("Computer input is", comp)
        computer_win = computer_win + 1
        print("YOU LOST\n")
    elif comp == "Paper" and player == "Scissors":
        print("Computer input is", comp)
        player_win = player_win + 1
        print("YOU WIN\n")
    elif comp == "Scissors" and player == "Paper":
        print("Computer input is", comp)
        computer_win = computer_win + 1
        print("YOU LOST\n")
    elif comp == "Scissors" and player == "Stone":
        print("Computer input is", comp)
        player_win = player_win + 1
        print("YOU WIN\n")
    elif comp == "Stone" and player == "Scissors":
        print("Computer input is", comp)
        computer_win = computer_win + 1
        print("YOU LOST\n")
    elif comp == player:
        print("Computer input is also "+comp+" So,Draw")
    else:
        print("Follow the rule")
        print("And you lost 1 of Your chances")
    n = n+1
    print("GO AGAIN\n")

print("Number of matches Win by Player", player_win)
print("Number of matches Win by Player", computer_win)
