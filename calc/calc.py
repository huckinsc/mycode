#!/usr/bin/env python3

def main():
    done = False
    while not done:
        display_menu();
        user_input = get_menu_input()
        if user_input == 5:
            done = True
        else:
            perform_calculation(user_input)

def display_menu():
    print ("Select an opperation to perform:")
    print("\t1) Addition")
    print("\t2) Subtraction")
    print("\t3) Multiplication")
    print("\t4) Division")
    print("\t5) Exit")

def get_menu_input():
    done = False
    while not done:
        user_input = input("Choice: ")
        if user_input.isdigit():
            choice = int(user_input)
            if choice >= 1 and choice <= 5:
                return choice
        print("Not valid input")

def get_number(input_str):
    done = False
    while not done:
        user_input = input(input_str)
        try:
            number = float(user_input)
            return number
        except:
            print("Not a valid number.")

def perform_calculation(user_input):
    if user_input == 1:
        addition()
    elif user_input == 2:
        subtraction()
    elif user_input == 3:
        multiplication()
    elif user_input == 4:
        division()

def addition():
    print("Enter two numbers to add.")
    num1 = get_number("Please enter number 1: ")
    num2 = get_number("Please enter number 2: ")
    result = num1 + num2
    print(f"{num1} + {num2} = {result}")
    input("Press enter to continue.")


def subtraction():
    print("Enter two numbers to subtract.")
    num1 = get_number("Please enter number 1: ")
    num2 = get_number("Please enter number 2: ")
    result = num1 - num2
    print(f"{num1} - {num2} = {result}")
    input("Press enter to continue.")

def multiplication():
    print("Enter two numbers to multiply.")
    num1 = get_number("Please enter number 1: ")
    num2 = get_number("Please enter number 2: ")
    result = num1 * num2
    print(f"{num1} * {num2} = {result}")
    input("Press enter to continue.")

def division():
    print("Enter two numbers to divide.")
    num1 = get_number("Please enter the dividend: ")
    num2 = get_number("Please enter the divisor: ")
    if num2 != 0:
        if num1 == int(num1) and num2 == int(num2):
            i_num1 = int(num1)
            i_num2 = int(num2)
            result = i_num1 // i_num2
            remainder = i_num1 % i_num2
            print(f"{i_num1} / {i_num2} = {result}r{remainder}")
       # else:
        result = num1 / num2
        print(f"{num1} / {num2} = {result}")
    else:
        print("To infinity and beyond...\nCannot divide by zero.")
    input("Press enter to continue.")

main()
