import random

num = random.randint(1, 10)


def guess(num):
    guess = input("guess a number between 1 and 10: ")
    guess = int(guess)

    if guess == num:
        print("congratulations! you won!")
        
    else:
        print("the guessed number is ",num,"your number is ",guess)
        print("WRONG GUESS...sorry. try again!")
    
guess(num)