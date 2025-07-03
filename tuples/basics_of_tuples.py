fruits = ("apple", "banana", "cherry", "apple", "cherry")
print(fruits)

# Using Parenthesis

colors = ("red","green","blue")
print(colors)
numbers = (1,2,3,4,5)
print(numbers)
mixed = (1, 2, "red", 3.14, True)
print(mixed)
nested = (1,[2,3],[5,6,7])
print(nested)

# Without using Parenthesis

number_tuples = 1,2,3,4,5
print(number_tuples)

# Using the tuple constructor

tuple_constructor = tuple(("red","green","blue"))
print(tuple_constructor)

# Ordered - the items have a defined order, and that order will not change.

print(mixed[1]) # always provide 2

# Tuple length
print(len(number_tuples))

# Create Tuple With One Item - add a comma after the item, otherwise Python will not recognize it as a tuple.

tuple_one_item = ("apple",)
print(type(tuple_one_item)) # <class 'tuple'>

#NOT a tuple
not_a_tuple = ("apple")
print(type(not_a_tuple)) # <class 'str'>

# Tuple Items - Data Types

print(type(colors))
print(type(numbers))
print(type(mixed))