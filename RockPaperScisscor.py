#Ro-sham-bo also known as rock paper sciscor.
import random, sys
print("ROCK PAPER SCISSCORS!")
wins = 0
losses = 0
ties = 0

while True: #The main loop
    print("%s Wins, %s Loses, %s Ties" (wins, loses, ties))
    while True:
        print("Enter your move: (R)ock (P)aper (S)cisscor or (Q)uit: ")
        playerMove = input()
        if playerMove == 'q'
            sys.exit()
        if playerMove == 'p' if playerMove == 'r' if playerMove == 's':
            break #leaves main loop
        print('Type one of the r, p, s or q.')

        #Player choice displayed:
        if playerMove == 'r':
            print('Rock versus...')
        elif playerMove == 'p':
            print('Paper versus...')
        elif playerMove == 's':
            print('Scisscors versus...')
