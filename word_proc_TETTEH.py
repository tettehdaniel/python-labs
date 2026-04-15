# SPEED RUN LAB
# Daniel Tetteh
# 04.10.2026
# CMSC 150 - 02

import random
import math


# DEBUGGING CONSTANTS
SHOW_DATA = True            # (optional) set to False to not show the lists in the beginning
RANDOM_WORD = ""            # (optional) change this to look for a specific word
RANDOM_INT = -1             # (optional) change this to look for a specific integer


# -- FILE IMPORT AND PRE-PROCESSING -- #


def get_file_data() -> list:
    ''' Opens the file "weird_data.txt"
        and returns a list of each element
    '''
    filename = "weird_data.txt"
    entries = []
    with open('weird_data.txt', 'r') as file:
        entries = file.readlines()
    new_entries = []
    for i in entries:
        ls = i.strip('\n')
        new_entries.append(ls)
        

    # Write importing code here

    return new_entries       # replace me with the actual data

def all_words(n:list) -> list:
    ''' Returns a list of only the words from the data
        ex. [apple82, bear23, can00] --> [apple, bear, can]
    '''
    list1 = []
    for i in n:
        list1.append(i[:-2])
    return list1

def all_numbers(n:list) -> list:
    ''' Returns a list of only the integers
        ex. [apple82, bear23, can00] --> [82, 23, 00]
    '''
    list3 = []
    for i in n:
        list3.append(int(i[-2:]))
    return list3


# -- SEARCH ALGORITHMS -- #

def any_search(n:list,x):
    for i in range(len(n)):
        if n[i] == x:
            return i
    return -1

def int_search(n:list,x):
    sortedlist = sorted(n)
    low_int = 0
    high_int = len(sortedlist) - 1
    middle_int = math.floor((low_int + high_int + 1)/2)
    index_int = -1
    
    while low_int <= high_int and index_int == -1:
        if x == sortedlist[middle_int]:
            index_int = middle_int
        elif x < sortedlist[middle_int]:
            high_int = middle_int -1
        else:
            low_int = middle_int + 1
        middle_int = math.floor((low_int + high_int + 1) / 2)
    return index_int
    


# -- SORTING ALGORITHMS -- #

def int_sort(n:list):
    for i in range(len(n) - 1):
        s = i
        for j in range(i + 1, len(n)):
            if n[j] < n[s]:
                s = j
        tmp = n[i]
        n[i] = n[s]
        n[s] = tmp
    return n

def word_sort(n:list):
    new_list = sorted(n, key=str.lower)
    return new_list
    


# !!!!! DO *NOT* CHANGE ANYTHING BELOW  !!!! #

def main():

    # import the data
    weird_data = get_file_data()
    print(f"File imported! {len(weird_data)} lines of data found")

    if SHOW_DATA:
        print(f"== Full data: ==\n{', '.join(weird_data)}\n")

    # make separate lists for words and integers
    word_data = all_words(weird_data)
    int_data = all_numbers(weird_data)

    # optionally show the data
    if SHOW_DATA:
        print(f"== Word data: ==\n{', '.join(word_data)}\n")
        print(f"== Integer data: ==\n{', '.join([str(x) for x in int_data])}\n")
        
    
    # pick a random element to search for
    int_rand = random.choice(int_data) if RANDOM_INT == -1 else RANDOM_INT
    word_rand = random.choice(word_data) if RANDOM_WORD == "" else RANDOM_WORD
    
    # test linear search
    print(f"== ANY SEARCH [int] ({int_rand}) ==")
    print(any_search(int_data,int_rand))
    print("")

    print(f"== ANY SEARCH [word] ({word_rand}) ==")
    print(any_search(word_data,word_rand))
    print("")
    
    # test binary search
    print(f"== INT SEARCH (on sorted array) ({int_rand}) ==")
    print(int_search(int_data,int_rand))
    print("")

    # test linear search on non-existent element
    non_int_rand = 150
    non_word_rand = "cs"
    
    print(f"== ANY SEARCH (for missing element) [int] ({non_int_rand}) ==")
    print(any_search(int_data,non_int_rand))
    print("")

    print(f"== ANY SEARCH (for missing element) [word] ({non_word_rand}) ==")
    print(any_search(word_data,non_word_rand))
    print("")
    
    # test binary search on non-existent element
    print(f"== INT SEARCH (for missing element) (on sorted array) ({non_int_rand}) ==")
    print(int_search(int_data,non_int_rand))
    print("")

    # test selection sort
    print(f"== INT SORT == ")
    int_dat2 = int_data.copy()
    print(int_sort(int_dat2))
    print("")

    print(f"== WORD SORT == ")
    word_dat2 = word_data.copy()
    print(word_sort(word_dat2))
    print("")

    

if __name__ == "__main__":
    main()
