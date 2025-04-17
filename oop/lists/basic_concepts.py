# List: Lists are used to store multiple items in a single variable.
# Lists are one of 4 built-in data types in Python used to store collections of data, the other 3 are Tuple, Set, and Dictionary, all with different qualities and usage.

# List Items: List items are ordered, changeable, and allow duplicate values.
# Ordered: It means that the items have a defined order, and that order will not change.
# If you add new items to a list, the new items will be placed at the end of the list.
# List items are indexed and accessible by index number

mylist = ["apple", "banana", "cherry"]
print(mylist)

thislist = ["apple", "banana", "cherry", "apple", "cherry"]
print(thislist)

# To determine how many items a list has, use the len() function
print(len(mylist))
# print(mylist.count) # output - <built-in method count of list object at 0x0000017527166080>

# List items can be of any data type:
any_datatype_list = ["abc", 34, True, 40, "male"]

# data type of a list - <class 'list'>
print(type(mylist))

print(type(any_datatype_list))

# list() Constructor - constructor when creating a new list
thislist = list(mylist)
print(thislist)
