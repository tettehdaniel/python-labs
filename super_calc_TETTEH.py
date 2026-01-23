# SUPER CALCULATOR PROGRAM
# Name: Daniel Tetteh
# Date: 1/23/2025
# Lab no. 2 - Super Calculator
# Class: CMSC 150 - [Section 02]

import math
import random

while True:
    print("What would you like to do?")

    user_input = input("> ")
    
    if user_input == "quit":
        break

    # YOUR CODE BELOW #

    if user_input == "add":
        a = input("a:")
        b = input("b:")
        c = int(a) + int(b)
        print(f"{a} + {b} = {c}")

    elif user_input == "subtract":
        a = input("a:")
        b = input("b:")
        c = int(a) - int(b)
        print(f"{a} - {b} = {c}")

    elif user_input == "multiply":
        a = input("a:")
        b = input("b:")
        c = int(a) * int(b)
        print(f"{a} * {b} = {c}")

    elif user_input == "divide":
        a = input("a:")
        b = input("b:")
        c = int(a) / int(b)
        if int(b) == 0:
            print("Cannot divide by 0!")
        else:
            print(f"{a} / {b} = {c}")

    elif user_input == "modulo":
        a = input("a:")
        b = input("b:")
        c = int(a) % int(b)
        if int(b) == 0:
            print("Cannot divide by 0!")
        else:
            print(f"{a} % {b} = {c}")

    elif user_input == "quad":
        a = int(input("a:"))
        b = int(input("b:"))
        c = int(input("c:"))
        if int(a) == 0:
            print("Cannot divide by 0!")
        else:
            q = b**2 - 4*a*c
            print("Cannot take square root of negative!")

    elif user_input == "coin":
        a = random.random()
        if a > 0.5:
            print("Heads")
        else:
            print("Tails")

    elif user_input == "help":
        print("add = Adds 2 numbers \nsubtract = Subtracts 2 numbers \nmultiply = Multiplies 2 numbers \ndivide = Divides 2 numbers \nmodulo = Gets remainder of 2 numbers \nquad = Quadratic formula \ncoin = Flips a coin \nquit = Ends the program \n ")
# the spacing is intentional
print("==== SUPER CALCULATOR PROGRAM TERMINATED ====")
