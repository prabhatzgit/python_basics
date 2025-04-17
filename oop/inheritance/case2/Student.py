from oop.inheritance.case1.Person import Person

class Student(Person):
    def __init__(self,fname,lname):
        Person.__init__(self,fname,lname)
# Note: The child's __init__() function overrides the inheritance of
# the parent's __init__() function.
x = Student("Ranjan","Mahanty")
x.printname()