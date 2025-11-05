#This is a Python file where it takes the user input and returns the number of dices rolled.
# Created by Harsh S - 04/11/2025 

#Importing random library to use the randint function
import random

#Creating a function to calculate the amount of rolls and return the list of numbers seen on the dices.Takes the amount = 2 when not provided any number.
def roll_dice(amount : int = 2) -> list[int]:
    if amount <= 0:
        raise ValueError
    
    rolls: list[int] = []
    for i in range(amount):
        rolls.append(random.randint(1,6))

    return rolls

def main():
    while True:
        try:
            user_input: str = input('How many dice you want to roll?')

            if user_input.lower() == 'exit':
                print('Thanks for playing!')
                break

            print(*roll_dice(int(user_input)),sep=',')

        except ValueError:
            print('Please enter a valid argument!')

if __name__ == '__main__':
    main()