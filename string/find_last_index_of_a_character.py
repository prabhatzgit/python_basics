# A Python program to find last
# index of character x in given
# string.

# Returns last index of x if it
# is present. Else returns -1.
def findLastIndex(str, x):
    index = -1
    for i in range(0, len(str)):
        if str[i] == x:
            index = i
    return index

# Driver program

# String in which char is to be found
str = "geeksforgeeks"

# char whose index is to be found
x = 'e'

index = findLastIndex(str, x)

if index == -1:
    print("Character not found")
else:
    print('Last index is', index)

# traverse from right

# Simple Python3 program to find last
# index of character x in given string.

# Returns last index of x if it is
# present. Else returns -1.
def findLastIndex(str, x):

    # Traverse from right
    for i in range(len(str) - 1, -1,-1):
        if (str[i] == x):
            return i

    return -1

# Driver code
str = "geeksforgeeks"
x = 'e'
index = findLastIndex(str, x)

if (index == -1):
    print("Character not found")
else:
    print("Last index is " ,index)