import random
number = random.randint(1, 10)

name = input("Hi! What is your name? \n")
print(f'You have a nice name {name}!\nNow we gonna play a game is called guess the number.\n'
      f'I will think a number between 1 and 10 then you will guess.\nYou have only 3 chances.')
number_guess = 0

while number_guess < 3 :
    guess = int(input("What is your estimate? \n"))
    number_guess += 1
    if guess < number:
        print("Your estimate is too low, go up a little!")
    if guess > number:
        print("Your estimate is too high, go down a little!")
    if guess == number:
        break

if guess == number:
    print(f"Congratulations {name} , you guessed the number in {number_guess} tries!")
else:
    print(f"Close but no cigar, you could not guess the number. Well the number was {number}")



