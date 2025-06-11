thislist = ["apple","banana","cherry"]

print(thislist[0])  # apple left to right
print(thislist[1])  # banana left to right
print(thislist[2])  # cherry left to right

# Negative Indexing

print(thislist[-1]) # cherry right to left
print(thislist[-2]) # banana right to left
print(thislist[-3]) # apple right to left
# print(thislist[-4]) # IndexError: list index out of range

# range of indexes

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]

# specify a range of indexes by specifying where to start and where to end the range.
# The search will start at index 2 (included) and end at index 5 (not included).
print(thislist[2:5])

# returns the items from the beginning to, but NOT including, "kiwi"
# colon before index means last index value should not include in the response list
print(thislist[:4])

# colon after index means from the beginning index to last index value  should include in the response list
print(thislist[2:])

# Range of Negative Indexes
# Specify negative indexes if you want to start the search from the end of the list
print(thislist[-4:-1]) # end index to begin index

# Check if Item Exists
#To determine if a specified item is present in a list use the in keyword

# Check if "apple" is present in the list:
if "apple" in thislist:
  print(f"Yes apple is in {thislist}")