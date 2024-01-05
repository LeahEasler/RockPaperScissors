#Ro-sham-bo also known as rock paper sciscor.
import random, sys
print("ROCK PAPER SCISSCORS!")
wins = 0
losses = 0
ties = 0

while True: #The main loop
    print('%s Wins, %s Losses, %s Ties' % (wins, losses, ties))
    while True: # Loop Looks for player input and prints error if wrong key is pressed
        print("Enter your move: (r)ock (p)aper (s)cisscor or (q)uit: ")
        playerMove = input()
        if playerMove == 'q':
            sys.exit()
        if playerMove == 'p' or playerMove == 'r' or playerMove == 's':
            break #leaves main loop
        else:
            print('Type one of the r, p, s or q.')

        # Player choice displayed:
    if playerMove == 'r':
        print('Rock versus...')
    elif playerMove == 'p':
            print('Paper versus...')
    elif playerMove == 's':
            print('Scisscors versus...')

    randomNumber = random.randint(1, 3) # Defines random number and prints computer move
    if randomNumber == 1:
       computerMove = 'r'
       print('ROCK')
    elif randomNumber == 2:
       computerMove = 'p'
       print('PAPER')
    elif randomNumber == 3:
       computerMove = 's'
       print('SCISSCORS')

        # Checking result and counting the Wins, Loses, and Ties
    if playerMove == computerMove:
        print('You tied with the computer!')
        ties = ties + 1 # Adds to ties counter
    elif playerMove == 'r' and computerMove == 's':
        print('YOU WIN!')
        wins = wins + 1 # Adds to wins
    elif playerMove == 'p' and computerMove == 'r':
        print('YOU WIN!')
        wins = wins + 1
    elif playerMove == 's' and computerMove == 'p':
        print('YOU WIN!')
        wins = wins + 1
    elif playerMove == 'r' and computerMove == 'p':
        print('Better luck next time! You lose...')
        losses = losses + 1
    elif playerMove == 's' and computerMove == 'r':
        print('Better luck next time! You lose...')
        losses = losses + 1
    elif playerMove == 'p' and computerMove == 's':
        print('Better luck next time! You lose...')
        losses = losses + 1
