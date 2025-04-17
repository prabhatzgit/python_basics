# creating class
class Student:
    name = "Prabhat"
    def __init__(self):
        print(self)
        print("adding new students in database")

# creating object(instance)
s1 = Student() #() helps to call init function
print(s1)
# print(s1) and print(self) refers to same memory location

# init function - constructor --> called at the time of object creation
# it is a default function and called automatically

# self --> it is a reference to the current instance of the class, and it is used to
# access variables that belongs to the class

class Student:
    college_name = "NIT" # same for all student, it is class level attr
    # to access class level attr, use Class.attr
    # so declared at class level and occupied memory at one time
    # default constructors
    name = "anonymous"
    def __init__(self):
        pass

    # parameterized constructor
    def __init__(self, firstname, marks):
        self.name = firstname
        self.marks = marks

# creating object(instance)
s1 = Student("Prabhat", 90) #() helps to call init function
print(s1.name, s1.marks)

s2 = Student("Ranjan", 95)
print(s2.name, s2.marks)

print(Student.college_name)
print(s2.college_name)
print(s1.name) # obj.attr precedence is higher than > class.attr