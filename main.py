# task 1 from handout
# guess number between 1 - 100
import random
number = int(input("Please enter a number from 1-100: "))
guesses = random.randint(1,100)
count = 1

while number <=100 and number >1:
    count+=1
    if number > guesses:
        print("Your guess is too high")
        number = int(input("Please enter another number: "))
    elif number < guesses:
        print("Your guess is too low")
        number = int(input("Please enter another number: "))
    elif number == guesses:
        print("You have guessed correctly")
        print("You have guessed", count,"times")
        break
