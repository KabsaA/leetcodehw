'''Problem 1: Implement function ToLowerCase() that has a string parameter str, and returns the same string in lowercase.'''
# Restate: This function will take in a string and return the same one in lower case.
#I'm assuming all inputs alpha characters as numbers don't have lower cases.

def toLowerCase(string):
    return string.lower()

# Test Cases
#print(toLowerCase("CAT ARE CUTE!"))
#print(toLowerCase("i love Kittens"))
#print(toLowerCase("ABCDEabcde"))


'''Problem 2 : You're given strings J representing the types of stones that are jewels, and S representing the stones you have.
Each character in S is a type of stone you have. You want to know how many of the stones you have are also jewels.
The letters in J are guaranteed distinct, and all characters in J and S are letters.
Letters are case sensitive, so "a" is considered a different type of stone from "A".'''

# This function will return the total number of characters that are both stones and jewels.


def numJewelsInStones(J,S):
    numofchars = 0
    for chars in S:
        if chars in J:
            numofchars += 1
    return numofchars

# Test Cases
#Input: J = "aA", S = "aAAbbbb"
#Output: 3

#Input: J = "z", S = "ZZ"
#Output: 0
