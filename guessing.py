import random
import math

lower=int(input("Enter the Lower BOund number:-"))
upper=int(input("Enter the upper bound number:-"))

number=random.randint(lower,upper)

guess=0
chance=6

while guess!=number :
    guess=int(input("Enter the Guess number:"))

    if(guess<number):
        print("Your Guss is to Low")
    elif(guess>number):
        print("Your Guess is to High")
    else:
        print("YOU ARE CORRECT")

    chance -=1

    if chance>0:
        print(chance,"you have left")
    else:
        print("Your Chances Are Completed ,The Correct number is:",number)
