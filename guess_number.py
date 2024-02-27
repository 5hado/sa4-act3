import random

number = random.randint(1, 10)

print("I'm thinking of a number...")
for u in range(5):
    guess = input("What number am I thinking of? ")

    if guess == "q" or u == 4 :
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
    
    print("You have " + str(4-u) + " more tries")
    
