# function : name of a function which does action based on its naming convention
# and followed by a set of parenthesis

print("Hello")
num_char = len("Hello")
print(num_char)

# if we want to make our own function, then first start out with keyword def
# by which we can define the function
# after def keyword, specify the function name
# add set of parenthesis and add colon :
# write the lines of code to implement the logic
# when the function is triggered, the lines of code must be indented
# then call the function with declaring the function name

def my_function():
    print("Hello")
    print("Python")

my_function() # call the function, else print() not print on the console
