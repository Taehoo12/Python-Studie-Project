# Created by: Sebastian Dąbrowski -  Uniwersytet WSB Merito Gdańsk | NR. ALBUMU: 72138
# GitHub: https://github.com/Taehoo12

import random

def greeting ():   
    name = input("\nWhat's your name?: ")
    print(f'Hi, {name.capitalize()}\n\nWelcome in guessing game')           # Makeing sure that first letter of name is capitalized
    del name

def generate_number (l_attempt):                                            # Generates a random number for the player to guess
    attempt = 1
    los = random.randint(1, 100)
    print(f"\nGuess the number\nAttempt number: {attempt}")

    while True:
        testing = int(input())

        if testing == los:                                                  # Player entered the correct number
            print("\nYou won!!\n\n")
            l_attempt.append(attempt)
            break

        elif testing != los:                                                # You missed. Showing a small hint where you are
            attempt += 1

            if los+1 <= testing <= los+7: 
                print("\n\nYou're so close, but try something smaller.")    # Your number is from 1 to 7 bigger than program expects
            elif los-1 >= testing >= los-7: 
                print("\n\nYou're so close, but try something bigger.")     # Your number is from 1 to 7 smaller than program expects
            elif los+8 <= testing <= los+14: 
                print("\n\nYou're close, but not enough. Try something smaller.")
            elif los-8 >= testing >= los-14: 
                print("\n\nYou're close, but not enough. Try something bigger.")
            elif los+15 <= testing <= los+21: 
                print("\n\nThat's not what i'm thinking about, try something smaller.")
            elif los-15 >= testing >= los-21: 
                print("\n\nThat's not what i'm thinking about, try something bigger.")
            elif los+22 <= testing: 
                print("\n\nYou're so far away, try something really smaller.")
            elif los-22 >= testing:
                print("\n\nYou're so far away, try something really bigger.")

        print(f"Attempt number: {attempt}")

def statistics(l_attempt):                                                  # Showing you the statistics from the list
    c = l_attempt.copy()
    c.sort()                                                                # Copying and sorting the original list to get the best score and its position in the list that equals the game number
    print(f"\n\nYour best score: {c[0]}\nIn game: {l_attempt.index(c[0])+1}\nYour last score: {l_attempt[-1]}\nIn game: {l_attempt.index(l_attempt[-1])+1}\n")


if __name__ == '__main__':
    l_attempt = []

    greeting()
    menu = int(input("\n[1] Start The Game\n[2] EXIT\n"))
    
    if menu == 1:
        print("\nYou need to guess the number that i'm thinking about (1 to 100). I'll tell you if you're close or not.\nLet's start it!!!\n")

    while menu == 1:
        menu2 = 2
        generate_number(l_attempt)

        while menu == 1 and menu2 == 2:                                     # There's two ways out of the loop. Exit the game or play again
            menu2 = int(input("[1] Play again\n[2] Statistics\n[3] EXIT\n"))

            if menu2 == 2: statistics(l_attempt)
            if menu2 == 3: menu = 2

    print("\nSee you soon!!")
