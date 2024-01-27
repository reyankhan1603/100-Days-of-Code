#Number Guessing Game

import random
num = random.randint(1,100)

print("Welcome to the number guessing game!")
print("I am thinking of a number between 1 and 100")
i = input("Choose a difficulty, Type 'easy' or 'hard'.\n")

if i.lower() == 'easy':
    chance = 10

elif i.lower() == 'hard':
    chance = 5

while chance > 0:
    print(f"You have {chance} attempts remaining to guess the number.")
    print("Make a guess: ", end = '')
    a = int(input())
    if a > num:
        print("Too High")
    elif a < num:
        print("Too Low")
    else:
        print("You got it! The answer is ",num)
        break
    chance -= 1
    if chance == 0:
        print("You have run out of guesses. You lost.")
        break

    print("Guess again.")
