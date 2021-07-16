"""""
print("Start")
while(1):
    print("enter the number ")
    n = int(input())
    if n <= 100:
        print("number is less than 100")
        continue
    else:
        print("congo ")
        break
"""
# Excercise 3
secret_num = 18
print("Welcome in the Game")
no_of_guess = 9
guess = 0
while (True):
    print("Enter your number")
    num = int(input())
    if num < secret_num:
        print("increase number ")
        guess = guess + 1
        if guess > no_of_guess:
            print("Game over")
        else:
            continue
    elif num == secret_num:
        print("You won")
        guess= guess+1
        o=no_of_guess-guess
        print("guesses left", o)
        print("guesses took", guess)
        break
    else:
        print("decrease number ")
        guess = guess + 1
        if guess > no_of_guess:
            print("Game over")
        else:
            continue

print("Thanks for playing")
