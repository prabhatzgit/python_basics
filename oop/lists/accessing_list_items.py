thislist = ["apple","banana","cherry"]

print(thislist[0])  # apple left to right
print(thislist[1])  # banana left to right
print(thislist[2])  # cherry left to right

# Negative Indexing

print(thislist[-1]) # cherry right to left
print(thislist[-2]) # banana right to left
print(thislist[-3]) # apple right to left
print(thislist[-4]) # IndexError: list index out of range

# range of indexes

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])