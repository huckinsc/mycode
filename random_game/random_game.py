#!/usr/bin/env python3

from random import randint

def main():
    game_round = 1
    player_score = 0
    target_number = randint(1,100)
    while game_round <= 7:
        display_stats(game_round,player_score)
        player_guess = get_player_guess()
        player_score += calculate_round_score(player_guess,target_number,game_round)
        if target_number == player_guess:
            print("You guessed the number")
            game_round = 7
        elif player_guess < target_number:
            print("Your guess is low")
        else:
            print("Your guess is high")
        game_round += 1
    display_end_game(player_score, target_number)

def display_stats(g_round, score):
    print(f"ROUND: {g_round}\t\tSCORE: {score}")

def get_player_guess():
    valid = False
    result = 0
    while not valid:
        usr_input = input("What is your guess? (1 - 100)\n ")
        if usr_input.isdigit():
            guess = int(usr_input)
            if guess >= 1 and guess <= 100:
                result = guess
                valid = True;
            else:
                print("Input need to be between 1 and 100!")
        else:
            print("Input needs to be a valid integer")
    return result

def calculate_round_score(guess,target,g_round):
    points = 0
    if guess == target:
        if g_round == 1:
            points = 5000
        elif g_round == 2:
            points = 4000
        elif g_round == 3:
            points = 3000
        else:
            points = 500
    else:
        dif = abs(target - guess)
        if dif <= 15:
            points = ((dif * 2) + 30)  * (8 - g_round)
        elif dif <= 30:
            points = dif * (8 - g_round)
        elif dif <= 50:
            points = round(dif / 2)
    return points

def display_end_game(score, target):
    print("\tGame Over")
    print(f"The target was {target}")
    if score > 3000:
        print("Great job!!!")
    elif score > 1000:
        print("Pretty good guessing.")
    elif score > 500:
        print("You can do better.")
    else:
        print ("Did you even try...?")
    print(f"Your final score is {score}")

main()
