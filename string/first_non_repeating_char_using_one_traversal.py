'''
Python3 implementation to find non repeating character using
1D array and one traversal'''
import math as mt

NO_OF_CHARS = 256

'''
The function returns index of the first 
non-repeating character in a string. If 
all characters are repeating then 
returns INT_MAX '''


def firstNonRepeating(string):
    # initialize all character as absent

    arr = [-1 for i in range(NO_OF_CHARS)]

    '''
    After below loop, the value of 
    arr[x] is going to be index of 
    of x if x appears only once. Else 
    the value is going to be either 
    -1 or -2.'''

    for i in range(len(string)):
        if arr[ord(string[i])] == -1:
            arr[ord(string[i])] = i
        else:
            arr[ord(string[i])] = -2
    res = 10 ** 18

    for i in range(NO_OF_CHARS):
        '''
        If this character occurs only 
        once and appears before the 
        current result, then update the 
        result'''
        if arr[i] >= 0:
            res = min(res, arr[i])
    return res


# Driver program to test above function

string = "geeksforgeeks"

index = firstNonRepeating(string)

if index == 10 ** 18:
    print("Either all characters are repeating or string is empty")
else:
    print("First non-repeating character is", string[index])

# Using counter

# Python implementation of
# above approach
from collections import Counter


def makeHashMap(string):

    # Use Counter to make a frequency
    # dictionary of characters in a string.

    d1 = Counter(string)

    # Update value of each key such that
    # if frequency of  frequency of  a key
    # is equal to 1, then it is set to 0,
    # else set the value equal to None
    d1 = {(key): (0 if d1[key] == 1 else None)
          for key, value in d1.items()}

    return d1


def firstNotRepeatingCharacter(s):

    d = makeHashMap(s)

    # variable to store the first
    # non repeating character.
    nonRep = None

    # Traversing through the string only once.
    for i in s:
        if d[i] is not None:

            '''
            As soon as the first character in the string is 
            found whose value in the HashMap is "not None", 
            that is our first non-repeating character. 
            So we store it in nonRep and break out of the 
            loop. Thus saving on time.
            '''
            nonRep = i
            break

    if nonRep is not None:
        return nonRep
    else:

        # If there are no non-repeating characters
        # then "_" is returned
        return str("_")


# Driver Code
print(firstNotRepeatingCharacter('bbcdcca'))

# third approach

# Python implementation of above approach
def firstNonRepeating(s):

    flag = False
    index = -1
    for i in range(len(s)):

        # Here I am replacing a character with "" and
        # then finding the length after replacing and
        # then subtracting  length of that replaced
        # string from the total length of the original
        # string
        count_occurrence = len(s) - len(s.replace(s[i],''))

        if (count_occurrence == 1):
            flag = True
            index = i
            break

    if (flag):
        print(f"First non repeating character is {s[index]}")

    else:
        print("There is no non-repeating character is present in the string")

# Driver Code
s = "GeeksforGeeks"
firstNonRepeating(s)