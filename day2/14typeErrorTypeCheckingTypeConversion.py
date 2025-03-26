# len(12345)
# uncomment above code and run. It show below error
# TypeError: object of type 'int' has no len()

print(len("Hello"))

print(type("Hello"))
print(type(123))
print(True)
print(3.14)

print(int("123") + int("456"))
# int() - this function will convert data into different data types using special functions

# print("Number of letters in your name: " + len(input("Enter your name")))
# TypeError: can only concatenate str (not "int") to str
# len(input("Enter your name")) - give int. So Str with int concatenation not possible and provides an error

name_of_the_user = input("Enter your name")
length_of_name = len(name_of_the_user)

print(type("Number of letters in your name: ")) # Str
print(type(length_of_name)) # int

print("Number of letters in your name: " + str(length_of_name))