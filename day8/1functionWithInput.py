#def my_function(something): # Parameter
    # do this with something
    # then do this
    # finally do this
#my_function(123) # argument
# something --> Parameter --> the name of the data that's being passed in
# argument --> actual value of the data

def greet():
    print("Hello Angela")
    print("How do you do Jack Bauer")
    print("Isn't the weather nice?")

greet()

# Functions that allows for inputs
def greet_with_name(name):
    print(f"Hello {name}")
    print(f"How do you do {name}")

greet_with_name("Prabhat")