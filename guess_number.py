import random

number = random.randint(1, 10)

print("I'm thinking of a number...")
while(True):
    guess = input("What number am I thinking of? ")

    if guess == "q":
        break
    guess = int(guess)
    if guess == number:
        print("Congratulations! You guessed the right number.")
       
    else:
        print("Wrong")
    
print(f"Sorry! The number was {number}.")