# Topic1 : Debugging flipping Coin

# Orignial Code
import random 
guess =""
while guess not in ('heads','tails'):
    print("Guess the coin toss! Enter heads or tails:")
    guess = input()
toss = random.randint(0,1)
if toss == guess:
    print('You got it!')
else:
    print('Nope! Guess again!')
    guess = input()
    if toss == guess:
        print('You got it!')
    else:
        print('Nope. You are really bad at this game.')

# Debug Code
import random 
guess =""
coin = ['heads','tails']
while guess not in ('heads','tails'):
    print("Guess the coin toss! Enter heads or tails:")
    guess = input()

if toss == coin.index(guess):
    print('You got it!')
else:
    print('Nope! Guess again!')
    guess = input()
    while guess not in ('heads','tails'):
        print("Guess the coin toss! Enter heads or tails:")
        guess = input()
    if toss == coin.index(guess):
        print('You got it!')
    else:
        print('Nope. You are really bad at this game.')