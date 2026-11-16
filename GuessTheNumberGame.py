import random
import sys

number = random.randrange(1,100)
print("--------------------------------------------------")
print("----------------GUESS THE NUMBER!!----------------")
print("--------------------------------------------------\n")
print("===================MAIN MENU======================\n")
options = int(input("Choose options(1/2): \n1)Play   \n2)Exit\n"))
if options == 1:
    while True:
        guess = int(input("Enter your guessed number: "))
        if guess == number:
            print()
            print("Congratulations! You guessed the right number.\n")
            break
    
        if guess > number:
            print("HIGHER guess! Try Again!")
            print()
    
        if guess < number:
            print("LOWER guess!Try Again!")
            print()
        
        cont = input("Do you want to continue? (Y/N) ")
        print()
        
        if cont == 'N':
            print("See you soon!")
            break
else:
    print("See you soon!")
    sys.exit()
    
    
    