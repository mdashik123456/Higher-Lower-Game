import Art
import random
from Data import data
import os

def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)

def CheckAnswer(a_folower_count, b_folower_count, guess):
    '''this return a bool'''
    if a_folower_count > b_folower_count:
        return guess == 'a'
    else:
        return guess == 'b'


while True:
    score = 0
    clearConsole()
    print(Art.logo)

    option_a = random.choice(data)
    option_b = random.choice(data)

    while True:
        option_a = option_b
        option_b = random.choice(data)

        while option_b == option_a:
            option_b = random.choice(data)

        print(
            f"\n\nCompare A: {option_a['name']} , a {option_a['description']}, from {option_a['country']}")
        print(Art.vs)
        print(
            f"Against B: {option_b['name']} , a {option_b['description']}, from {option_b['country']}")

        guess = input(
            "\nWho has more followers? Type 'A' or 'B'\n--> ").lower()
        isCorrect = CheckAnswer(
            option_a["follower_count"], option_b["follower_count"], guess)

        clearConsole()
        print(Art.logo)
        if isCorrect:
            score += 1
            print(f"\nYou answer is correct.\nYour Score is : {score}\n")
        else:
            print(f"\nSorry Wrong Answer\nYour Final Score is : {score}")
            break

    isContinue = input("\nDo you want to play again? (Y/N)\n--> ").lower()
    if isContinue == 'n':
        break

print("\n\n\t\tThank You for Playing This Game\n\n")
