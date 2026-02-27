# Name: Daniel Tetteh
# Date: 02-13-26
# Lab 4
# CMSC 150 Section 2

import random
import math

def shuffle(arr):

    ''' Shuffles a copy of a list and returns the newly shuffled list '''

    backup = arr.copy()
    random.shuffle(backup)
    return backup

def pickN(arr,n =1):

    ''' Creates a function that returns n randomly pickd elements from a list '''
    if n < 1:
        print("n must be greater than 0")
        None
    else:
        b = set(arr)
        c = list(b)
        random.shuffle(c)
        return c[:n]

def spamChat(s):

    ''' Creates a function that prints a string multiple times until the output is equal to or no more than 500 characters long '''
    if s == "":
        None
        print("No string given!")
    else:
        a = 500 // len(s)
        b = s * a
        return b

def diceRoll(n,d):

    ''' Creates a function that picks a random number from 1 to d,
repeats it n times and returns the sum of the random values '''

    if n < 1 or d < 1:
        print("Invalid inputs. d nor n can be less than 1")
        return 0
    else:
        # for loop help: my brother Clement Tetteh (CS grad)
        total = 0
        for i in range(n):
            a = random.randint(1,d)
            total += a
        return total

def keySwap(d):
    ''' Inverts the keys in a given dictionary and returns as a new dictionary '''
    
    # for inverted dictionary: https://stackoverflow.com/questions/1031851/how-do-i-exchange-keys-with-values-in-a-dictionary
    backup = {value : key for key, value in d.items()}
    return backup

def wordCts(s):
    if s == "":
        print("s cannot be empty!")
        None
    else:
        # for dictionary loop help: https://www.geeksforgeeks.org/python/counting-word-frequency-and-making-a-dictionary-from-it/
        b = {}
        for c in s.split():
            b[c] = b.get(c, 0) + 1
        return b
if __name__ == "__main__":
    #write your test code here!
    x = wordCts("what the what")
    print(x)
