#Treasure Island Game
print('Welcome to the Treasure Island')
print('''  ____________________________________________________________________
/ \-----     ---------  -----------     -------------- ------    ----\
\_/__________________________________________________________________/
|~ ~~ ~~~ ~ ~ ~~~ ~ _____.----------._ ~~~  ~~~~ ~~   ~~  ~~~~~ ~~~~|
|  _   ~~ ~~ __,---'_       "         `. ~~~ _,--.  ~~~~ __,---.  ~~|
| | \___ ~~ /      ( )   "          "   `-.,' (') \~~ ~ (  / _\ \~~ |
|  \    \__/_   __(( _)_      (    "   "     (_\_) \___~ `-.___,'  ~|
|~~ \     (  )_(__)_|( ))  "   ))          "   |    "  \ ~~ ~~~ _ ~~|
|  ~ \__ (( _( (  ))  ) _)    ((     \\//    " |   "    \_____,' | ~|
|~~ ~   \  ( ))(_)(_)_)|  "    ))    //\\ " __,---._  "  "   "  /~~~|
|    ~~~ |(_ _)| | |   |   "  (   "      ,-'~~~ ~~~ `-.   ___  /~ ~ |
| ~~     |  |  |   |   _,--- ,--. _  "  (~~  ~~~~  ~~~ ) /___\ \~~ ~|
|  ~ ~~ /   |      _,----._,'`--'\.`-._  `._~~_~__~_,-'  |H__|  \ ~~|
|~~    / "     _,-' / `\ ,' / _'  \`.---.._          __        " \~ |
| ~~~ / /   .-' , / ' _,'_  -  _ '- _`._ `.`-._    _/- `--.   " " \~|
|  ~ / / _-- `---,~.-' __   --  _,---.  `-._   _,-'- / ` \ \_   " |~|
| ~ | | -- _    /~/  `-_- _  _,' '  \ \_`-._,-'  / --   \  - \_   / |
|~~ | \ -      /~~| "     ,-'_ /-  `_ ._`._`-...._____...._,--'  /~~|
| ~~\  \_ /   /~~/    ___  `---  ---  - - ' ,--.     ___        |~ ~|
|~   \      ,'~~|  " (o o)   "         " " |~~~ \_,-' ~ `.     ,'~~ |
| ~~ ~|__,-'~~~~~\    \"/      "  "   "    /~ ~~   O ~ ~~`-.__/~ ~~~|
|~~~ ~~~  ~~~~~~~~`.______________________/ ~~~    |   ~~~ ~~ ~ ~~~~|
|____~jrei~__~_______~~_~____~~_____~~___~_~~___~\_|_/ ~_____~___~__|
/ \----- ----- ------------  ------- ----- -------  --------  -------\
\_/__________________________________________________________________/''')
dir = input('You are at a cross road. Where do you want to go? Type "left" or "right"')
if dir == 'left':
    print('You come to a lake. There is an island in the middle of the lake. Type "wait" to wait for a boat. Type "swim" to swim across.')
    a = input()
    if a == 'wait':
        print('You have arrived at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose?')
        b = input()
        if b == 'yellow':
            print("You found the treasure! You Win!")
        elif b == 'red':
            print("It's a room full of fire. Game Over.")
        elif b == 'blue':
            print("You enter a room of beasts. Game Over.")
        else:
            print("You chose a door that doesn't exist. Game Over.")
    else:
        print("You get attacked by an angry trout. Game Over.")
else:
    print("You fell into a hole. Game Over.")