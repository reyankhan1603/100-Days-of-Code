#Hangman Game

import random
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']
word_list = ['abruptly', 'absurd', 'abyss','affix', 'askew','avenue','awkward','axiom','azure','bagpipes','bandwagon', 
'banjo','bayou','beekeeper','bikini','blitz','blizzard','boggle','bookworm','boxcar','boxful','buckaroo','buffalo', 
'buffoon','buxom','buzzard','buzzing','buzzwords','caliph','cobweb','cockiness','croquet','crypt','curacao','cycle', 
'daiquiri','dirndl','disavow','dizzying','duplex','dwarves','embezzle','equip','espionage','euouae','exodus','faking', 
'fishhook','fixable','fjord','flapjack','flopping','fluffiness','flyby','foxglove','frazzled','frizzled','fuchsia','funny', 
'gabby','galaxy','galvanize','gazebo','giaour','gizmo','glowworm','glyph','gnarly','gnostic','gossip', 'grogginess', 'haiku', 
'haphazard', 'hyphen', 'iatrogenic', 'icebox', 'injury', 'ivory', 'ivy', 'jackpot', 'jaundice', 'jawbreaker', 'jaywalk', 'jazziest', 
'jazzy', 'jelly', 'jigsaw', 'jinx', 'jiujitsu', 'jockey', 'jogging', 'joking', 'jovial', 'joyful', 'juicy', 'jukebox', 'jumbo', 'kayak', 
'kazoo', 'keyhole', 'khaki', 'kilobyte', 'kiosk', 'kitsch', 'kiwifruit', 'klutz', 'knapsack', 'larynx', 'lengths', 'lucky', 'luxury', 
'lymph', 'marquis', 'matrix', 'megahertz', 'microwave', 'mnemonic', 'mystify', 'naphtha', 'nightclub', 'nowadays', 'numbskull', 'nymph', 
'onyx', 'ovary', 'oxidize', 'oxygen', 'pajama', 'peekaboo', 'phlegm', 'pixel', 'pizazz', 'pneumonia', 'polka', 'pshaw', 'psyche', 'puppy', 
'puzzling', 'quartz', 'queue', 'quips', 'quixotic', 'quiz',  'quizzes', 'quorum', 'razzmatazz', 'rhubarb', 'rhythm', 'rickshaw', 
'schnapps', 'scratch', 'shiv', 'snazzy', 'sphinx', 'spritz', 'squawk', 'staff', 'strength', 'strengths', 'stretch', 'stronghold', 
'stymied', 'subway', 'swivel', 'syndrome', 'thriftless', 'thumbscrew', 'topaz', 'transcript', 'transgress', 'transplant', 'triphthong', 
'twelfth', 'twelfths', 'unknown', 'unworthy', 'unzip', 'uptown', 'vaporize', 'vixen', 'vodka', 'voodoo', 'vortex', 'voyeurism', 'walkway', 
'waltz', 'wave', 'wavy', 'waxy', 'wellspring', 'wheezy', 'whiskey', 'whizzing', 'whomever', 'wimpy', 'witchcraft', 'wizard', 'woozy', 
'wristwatch', 'wyvern', 'xylophone', 'yachtsman', 'yippee', 'yoked', 'youthful', 'yummy', 'zephyr', 'zigzag', 'zigzagging', 'zilch', 
'zipper', 'zodiac', 'zombie']
chosen_word = random.choice(word_list)

print('Welcome to the Hangman Game!')
print("Rules of the game: ")
print("1. A letter will be randomly selected from the word list.")
print("2. You'll have to guess the word by writing one letter at a time.")
print("3. If you guess the wrong letter you lose a life.")
print("4. A total of 6 lives will be given to the user. The game will be over if 0 life is left.")
print("Enjoy!")
print("=================================================================================================\n")

loop = True
word =""
lives = 6
print(stages[lives])
for i in range(len(chosen_word)):
    word += "_"
word = list(word)

for lett in word:
    print(lett, " ", end='')
print('')
print(chosen_word)

while loop:
    print("Guess a letter for the word: ")
    l = input().lower()
    if l not in chosen_word:
        lives-= 1
        print(stages[lives])
        print('Oops, you just lost a life.')
    if l in word:
        print('Word already entered, enter a new word.')
        continue
    for i in range(len(word)):
        if chosen_word[i]==l:
            print('Correct!')
            word[i]=l
        
    print(str(word))
    if lives==0:
        print('You Lost :(')
        loop = False
    if list(chosen_word) == word:
        print('You Won!')
        break