# Constructing Objects and Accessing their Attributes and Methods

#Case 1:
import another_module
print(another_module.another_variable)

# Case 2:
# import turtle
# timmy = turtle.Turtle()

# Case3:
from turtle import Screen, Turtle
timmy = Turtle()
print(timmy)
timmy.shape("red")

# Object attributes and methods

my_screen = Screen()
print(my_screen.canvheight) # canvheight is the attribute of the object
my_screen.exitonclick() # exitonclick is the method of the object