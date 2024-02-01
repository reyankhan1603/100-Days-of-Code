#Blackjack Capstone Project
#The blackjack game has rules that each player will have a deck of cards, the sum of 
#the numbers on the deck must not exceed 21 and should not be less that 17
#in the end the player who has the greatest sum will win however the sum must not
#exceed 21, else the player will lose immediately.


import sys
import random

print("Do you want to play the game of blackjack? Press 'y' or 'n'")
ans = input()

if ans == 'n':
    print("Goodbye!!!")
    sys.exit

else:
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    print("""
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""
                   )
    
    p1_deck = [random.choice(cards)]
    p1_deck.append(random.choice(cards))

    p2_deck = [random.choice(cards)]

    print("Your current cards are: ")
    print(p1_deck)
    if sum(p1_deck)>21:
        print("You lose :(")
        sys.exit()

    print("Computer cards are: ")
    print(p2_deck)
    p2_deck.append(random.choice(cards))

    loop = True

    while loop:
        print("Hit(draw more cards) or Stand(Lock current cards)?")
        choice = input()
        if choice.lower() =='hit':
            p1_deck.append(random.choice(cards))
            print(p1_deck)
            if sum(p1_deck)> 21:
                print('Computer Deck: ',p2_deck)
                print('Your Deck: ',p1_deck)
                print("You lose.")
                sys.exit()

        elif choice.lower() == 'stand':
            loop = False
        else:
            print('Sorry thats not a valid input.')

    while sum(p2_deck)<17:
        p2_deck.append(random.choice(cards))

    if sum(p2_deck)>21:
        print('Computer Deck: ',p2_deck)
        print('Your Deck: ',p1_deck)
        print("You won")
        sys.exit()

    print('Computer Deck: ',p2_deck)
    print('Your Deck: ',p1_deck)

    if sum(p1_deck)>sum(p2_deck):
        print('You Won')

    elif sum(p1_deck)<sum(p2_deck):
        print('You lose.')

    else:
        print("Its a draw.")