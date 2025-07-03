class User:
    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username
        self.followers = 0
        self.following = 0

    def follow(self,user):
        user.followers += 1
        user.following += 1

user_1 = User("001","Prabhat")
user_2 = User("002","Ranjan")

def function():
    pass

# adding attributes

# user_1.id = "001"
# user_1.user_name = "Prabhat"

# user_1.id = "002"
# user_1.user_name = "Ranjan"

print(user_1.username)
print(user_2.username)
#print(user_1.follower)

user_1.follow(user_2)
print(user_1.followers)
print(user_1.following)
print(user_2.following)
print(user_2.followers)

# A class in Python is a blueprint for creating objects.
# Classes are defined using the class keyword followed by the class name and a colon.
# Class names should follow PascalCase naming convention.
# The pass keyword is used to define an empty class or function body to avoid indentation errors.

