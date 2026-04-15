# SPAGHETTI CODE
# Written by ChatGPT + A naive programmer
# Fixed by DANIEL TETTEH
# 04.03.2026
# CMSC 150-02


import math
import random

def is4Mult(n):
    '''Checks if a number is a multiple of 4'''
    number = n % 4
    if number != 0:
        return False
    elif number == 0:
        return True

def print10(l):
    '''Prints items in a list on separate lines up to the first 10'''
    lst = l[0:10]
    for x in lst:
        print(x)


def sameArr(a,b):
    '''Checks if 2 1-dimensional arrays are the same'''
    if len(a) != len(b):
        return False
    else:
        for i in range(len(a)):
            if a[i] != b[i]:
                return False
        return True

class Car:
    '''A car class for driving'''
    def __init__(self, year, make, model):
        self.year = year
        self.make = make
        self.model = model

    def start_engine(self):
        '''Starts the engine'''
        print("Engine started")

    def drive(self):
        '''Shows what kind of car is being driven'''
        print(f"I'm driving a {self.year} {self.make} {self.model}")

def calculate_total(prices):
    '''Gets the total of a list of prices'''
    return sum(prices)

def square(l):
    ''' Squares each number in a list l'''
    s = []
    for n in l:
        s.append(n * n)
    return s

def isOk(str):
    '''Checks if a string is "Ok"'''
    isOk = False
    if str == "Ok":
        return True
    else:
        return False

def find_max(numbers):
    '''Returns the maximum value in a list of numbers'''
    return max(numbers)

# for loop help: Clement Tetteh (brother)
t_letter = 't'
def changeAllT(lst):
    '''Returns an array where all letter t's in a list of strings
        are changed to the letter o'''
    lst2 = []
    for w in lst:
        new_word = ''
        for c in w:
            if c == t_letter:
                new_word += 'o'
            else:
                new_word += c
        lst2.append(new_word)
    return lst2
    
dice1 = random.randint(1,6)
dice2 = random.randint(1,6)
def lucky7():
    '''Randomly generate 2 numbers from range 1-6
        Print the sum of the dice
        If they add to 7, return "win" and "lose" if otherwise'''

    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)
    total = dice1 + dice2

    print(f"{dice1}+{dice2} = {total}")

    if dice1 + dice2 == 7:
        return "win"
    else:
        return "lose"

t_letter = 't'
def onlyT(lsst):
    '''Returns items in a string list that have a 't' in it'''
    only_t = []
    for word in lsst:
        for i in word:
            if i.lower() == t_letter:
                only_t.append(word)
                break  # stop checking this word once we found 't'
    return only_t
    
################################
#       !!! WARNING !!!        #
# DO NOT CHANGE ANYTHING BELOW #
################################

if __name__ == "__main__":

    print("== is4Mult() ==");print(is4Mult(5));print(is4Mult(16))

    print("\n== print10() ==");print10(['a','b','c','d','e','f','g'])

    print("\n== sameArr() ==");print(sameArr(['red','blue'],['gold','black']));print(sameArr(['a'],['a','r','e']));print(sameArr([420,69],[420,69]))

    print("\n== Car.drive() ==");my_car = Car(2017, "Nissan", "Sentra");my_car.start_engine();my_car.drive()

    print("\n== calculate_total() ==");print(calculate_total([10, 20, 30]))

    print("\n== square() ==");numbers = [1, 2, 3, 4, 5];print(square(numbers))

    print("\n== isOk() ==");print(isOk("Ok"));print(isOk("not ok"))

    print("\n== find_max() ==");print(find_max([8,10,3000,128,32.023]))

    print("\n== changeAllT() ==");print(changeAllT(["don't",'try','to','allow','another','error']))

    print("\n== lucky7() ==");print(lucky7());print(lucky7());print(lucky7())

    print("\n== onlyT =="); print(onlyT(['That','game','is','totally','cool','Trevor']))
