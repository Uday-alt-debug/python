import random

while True:
    lower = int(input("Enter the Lower Bound number: "))
    upper = int(input("Enter the Upper Bound number: "))

    number = random.randint(lower, upper)
    chance = 6

    while chance > 0:
        guess = int(input("Enter your guess: "))
        
        if guess < number:
            print("Your guess is too low.")
        elif guess > number:
            print("Your guess is too high.")
        else:
            print("Congratulations! You've guessed the correct number!")
            break

        chance -= 1
        if chance > 0:
            print(f"You have {chance} chances left.")
        else:
            print(f"Your chances are completed. The correct number was: {number}")

  
    play_again = input("Do you want to play again? (yes/no): ").strip().lower()
    if play_again != 'yes':
        print("Thank you for playing!")
        break
