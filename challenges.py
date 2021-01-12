import datetime
import random
import pickle
import time
import winsound
import requests
from collections import Counter
import numpy as np
from itertools import product


# Write a python function to fin the prime factorization of a given number.
# It should take an  integer value as the input and then return a list containing all of its prime factors.

# Solution 1
def factornumber(num):
   prime = 3
    while num != 1:
        if num % 2 == 0:
            num = num / 2
            print(2, num)
        elif num % prime == 0:
            num = num / prime
            print(prime, num)
        else:
            prime = prime + 2

# Solution 2
def recursive_factor(num, numbers, prime):
    if num==1:
        return numbers
    elif num % prime == 0:
        return recursive_factor(num/prime, numbers + "{}, ".format(prime), prime)
    else:
        return recursive_factor(num, numbers, prime+1)


# Write a function that determines if a given string is palindrome.
# It should take a string and retrun a Boolean. The function should overlook punctuation, whitespaces and treat uppercase and lowercase as the same.

def palindrome(stri):
    clear_string = ''.join(ch for ch in stri if ch.isalnum()).lower()
    return clear_string == clear_string[::-1]


# Write a function to sort the words in a string. 
# It should accept a string containing one or more words separated by spaces as the input argument, and then return a string of words sorted alphabetically.

def tolower(stri):
    return stri.lower()

def sortwords(strin):
    palabras = strin.split()
    print(sorted(palabras, key=tolower))


# Write a function  to find the indices for all items ina list that are equal to a given value.
# It should accept two input parameters; the list to search and the value you're searching for. The output should be a list of indices, each represented by a list of numbers.

# Solution 1
def findindex(lists, value, depth):
    result = []
    for index, element in enumerate(lists):
        if element == value:
            result = result + ["found value at index {} depth {}".format(index, depth)]
        if type(element) == list:
            result = result + findindex(element, value, [index]+depth)
    return result

# Solution 2
def index_all(lists,item):
    indices = list()
    for i in range(len(lists)):
        if lists[i] == item:
            indices.append([i])
        elif isinstance(lists[i],list):
            for index in index_all(lists[i],item):
                indices.append([i]+index)
    return indices


# Write a function to play a pulse pounding game. It should print a message for the player to wait a random amount of time.
# The player's goal is to wait that time and press enter again.
# That displays the elapsed time, and if the player was too fast, too slow or just right.

def waiting_game():
    goal = random.randint(2,4)
    input("Press enter to start. Press enter again in {}".format(goal))
    start = datetime.datetime.now()
    input("Game started")
    end = datetime.datetime.now()
    print("Game finished. Elapsed time {} \nOff by {}".format((end - start).total_seconds(), (end - start).total_seconds() - goal))


# Write a function to save and load a dictonary.

# Solution 1
def savedictionarty(dict):
    f = open("dictionary.txt", "w")
    for k, v in dict.items():
        f.write("{},{}\n".format(k,v))
    f.close()

def loaddict(path):
    f = open(path, "r")
    dict = {}
    for line in f:
        print(line)
        splitted = line.split(",")
        dict[splitted[0]] = splitted[1][:-1]
    return dict

# Solution 2
def save_dict(dict, path):
    with (open(path, 'wb')) as file:
        pickle.dump(dict,file)


def load_dict(dict, path):
    with (open(path, 'rb')) as file:
        return pickle.load(file)


# Write a function to set an alarm by playing asound file and printing a message at the specified time.

def alarm(atime,sound,message):
    wait= atime - time.time()
    time.sleep(wait)
    winsound.PlaySound(sound, winsound.SND_ALIAS)
    print(message)


# Write a function to determine the probability of different outcomes when rolling an arbitraty set of dice using the Monte Carlo simulation.

# Solution 1

def sim_dice2(*args):
    chances = {}
    for i in range(1000000):
        sum = 0
        for arg in args:
            roll = random.randint(1,arg)
            sum = roll  + sum
        chances[sum] = chances.get(sum,0) + 1
    for num in chances:
        chances[num] = chances.get(num,0) * 1/999999 * 100
    return chances

# Solution 2

def sim_dice(*dice,num_trials=1_000_000):
    counts = Counter()
    for trials in num_trials:
        counts[sum((random.randint(1,sides) for sides in dice))] = +1

    for outcome in counts:
        print("{}\t{:0.2f}%".format(outcome,counts[outcome]*100/num_trials))


# Write a function to solve sodoku puzzles.
# It should tale a ártoaññy filled in puzzle as input, and then return a two-dimensional list representing the solution.

def sodoku(puzzle):
    restart = True
    while(restart == True):
        restart = False
        for (row, col) in product(range(0, 9), repeat=2):
            if(puzzle[row][col] == 0):
                numbers = set()
                for i in range(0, 9):
                    numbers.add(puzzle[row][i])
                    numbers.add(puzzle[i][col])

                for (i, j) in product(range(0, 3), repeat=2):
                    numbers.add(puzzle[row - row % 3 + i][col - col % 3 + j])

                difference = set([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]) ^ numbers

                if (len(difference) == 1):
                    print("bingo! at [{}{}]".format(row,col))
                    puzzle[row][col] = (list)(difference)[0]
                    restart = True
                    break

            #print(difference)


    # print sodoku
    for j, row in enumerate(puzzle):
        print("")
        if j in [3,6]:
            print("-----------",)
        for i, num in enumerate(row):
            if i in [3,6]:
                print("|",end="")
            print(num,end="")
        print

# puzzle = [[5,3,0,0,7,0,0,0,0],
#           [6,0,0,1,9,5,0,0,0],
#           [0,9,8,0,0,0,6,0,0],
#           [8,0,0,0,6,0,0,0,3],
#           [4,0,0,8,0,3,0,0,1],
#           [7,0,0,0,2,0,0,0,6],
#           [0,6,0,0,0,0,2,8,0],
#           [0,0,0,4,1,9,0,0,5],
#           [0,0,0,0,8,0,0,7,9]]

# sodoku(puzzle)


# Write a function that takes a single argument for the number of words to select and then
# returns a string containg a sequence of randombly select words from that Diceware list separeted by spaces to generate a password.

def dice(rolls):
    d = {}
    password = ""
    with open("C:\temp\dice.txt") as f:
        for line in f:
            (key, val) = line.split()
            d[int(key)] = val

    for roll in range(0,rolls):
        number = 0
        for i in range(0,5):
            number = number * 10 + random.randint(1,6)
        print(number)
        password = password + "{} ".format(d[number])

    print(password.rstrip())

dice(4)

