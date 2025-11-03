#This is a Python file where it takes the user input and checks if the user has guessed the number right!
#Created by Harsh S - 29/10/2025.
 
#We have to assign a number from 1 to 10. Therefore, we will use the random library to get this number.
from random import randint
 
 
#Declaring the ranges
lower_rng, upper_rng = 1, 10
rand_num : int = randint(lower_rng,upper_rng)
print(f'Enter a number between {lower_rng} and {upper_rng}!')
 
#Creating the loop until the user gets the correct number!
while True:
    try:
        #Gathering the user input.
        user_inp : int = int(input('Please enter a number: '))
    except ValueError as e:
        #Catching if the type of input is different and informing the user
        print("Please enter a Valid argument!",e)
        continue
   
 
    #Checking if the user input is near or farther from the random generated number.
    if user_inp < rand_num:
        print("Higher!")
    elif user_inp > rand_num:
        print("Lower!")
    else:
        print("You have guessed it right!")
        break
 
 
#This is one way which I have tried, but I will use the try and catch block, since it is more reliable than assert function. Good try though!
# Gathering the user input.
#     user_inp : int = int(input('Please enter a number: '))
 
#     #Checking if the user input is valid, we can use the try and catch block to catch for invalid arguments.
#     assert user_inp == int(user_inp) and lower_rng < user_inp < upper_rng, "Please enter a valid argument!"
 