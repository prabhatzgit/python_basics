thistuple = ("apple", "banana", "cherry")
print(thistuple[1])

# Negative Indexing - -1 refers to the last item, -2 refers to the second last item etc.

print(thistuple[-1])

# Range of Indexes - specify a range of indexes by specifying where to start and where to end the range.
#  the return value will be a new tuple with the specified items.

fruits_tuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(fruits_tuple[2:5]) # 2 is included 5 is excluded

print(fruits_tuple[:4]) # returns the items from the beginning to, but NOT included, "kiwi":

print(fruits_tuple[2:]) # returns from the index value cherry onwards

# Range of Negative Indexes

print(fruits_tuple[-4:-1]) # -4 is included -1 is not included

# Check if Item Exists

if "cherry" in fruits_tuple:
    print("Yes, 'cherry' is in the fruits tuple")