import random

number = random.randint(1, 10)

print("I'm thinking of a number...")
while(True):
    guess = input("What number am I thinking of? ")

    if guess == "q":
        print(f"Sorry! The number was {number}.")
        break
    guess = int(guess)
    if guess == number:
        print("Congratulations! You guessed the right number.")
        break
       
    if guess > number:
        print("Wrong your guess is too high")
    else:
        print("Wrong you guess is too low")
    
