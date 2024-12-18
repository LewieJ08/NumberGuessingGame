from sys import exit
import random
import os


def welcomeMessage():
    print("Welcome to the number guessing game")
    print("You will be given an amount of chances to guess a number between 1 and 100")


def randomNumber():
    return random.randint(0,101)


def difficultyLevel():
    print("""
\nDifficulty Selection:
1. Easy - 10 Chances
2. Medium - 5 Chances
3. Hard - 3 Chances
              """)
    while True:
        try:
            choice = int(input("Select a difficulty [1,2,3]\n> "))
        except ValueError:
            print("Invalid Input")
        if choice == 1:
            return 10
        elif choice == 2:
            return 5
        elif choice == 3:
            return 3 
        

        
def game():
    chances = difficultyLevel()
    number = randomNumber()
    attempts = 0

    while chances > attempts:
        try:
            guess = int(input("\nEnter a guess: "))
        except ValueError:
            print("Invalid input")
            continue

        attempts += 1

        if guess > number:
            print(f"The Number is less than {guess}")
        elif guess < number:
            print(f"The Number is more than {guess}")
        else:
            print(f"\nCORRECT! You guess the number in {attempts} attempts")
            return attempts
    print(f"Sorry you have run out of Chances. The number was {number}")
            

def main():
   os.system("cls")

   welcomeMessage() 

   while True: 
        game()
        running = True
        while running:
            choice = input("Would you like to play again [yes/no]\n> ").lower().strip()
            if choice == "yes":
                continue
            elif choice == "no":
                print("Thanks for playing")
                exit()
            else:
                print("Invalid Input")
                running = False
                continue
    
if __name__ == "__main__":
    main()