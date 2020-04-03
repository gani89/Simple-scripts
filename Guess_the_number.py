import random
import time

print('Hello! What is your name?')
name = input()

n = random.randint(1,10)
print('\n/Hi ' + name + "I am thinking a number between 1 and 10. Guess it in 3 attempts.")
print(n)

attempt = 0

while True:
    attempt = attempt + 1
    if attempt > 3:
        break
    print('Take a guess:')
    guess = int(input())
    if guess > n:
        print('too high')
    elif guess < n:
        print('too low')
    else:
        print('You are right! Guessed number is ' + str(n))
        break

time.sleep(1)

print('\n\nYou already took 3 guesses, the number was ' + str(n))