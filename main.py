import random
n = random.randint(1, 99)
guess = int(input("Enter a number from 1 to 99:"))
while True:
    if guess < n:
        print("guess is too low")
        guess = int(input("Enter an number from 1 to 99:"))
    elif guess > n:
        print("guess is too high")
        guess = int(input("Enter a number from 1 to 99:"))
    else:
        print("you guessed it right!")
        break
input("press enter to exit")
