'''Problem 1: Implement function ToLowerCase() that has a string parameter str, and returns the same string in lowercase.'''
# Restate: This function will take in a string and return the same one in lower case.
#I'm assuming all inputs alpha characters as numbers don't have lower cases.

def toLowerCase(string):
    return string.lower()


# Test Cases
print(toLowerCase("CAT ARE CUTE!"))
print(toLowerCase("i love Kittens"))
print(toLowerCase("ABCDEabcde"))
