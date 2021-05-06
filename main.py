class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
        print("Name: ",self.name)
        print("Age: ",self.age)

class Student(Person):
    def __init__(self,name,age,roll_no,branch):
        Person.__init__(self,name,age)
        self.rollno = roll_no
        self.branch = branch

    def show(self):
        Person.display(self)
        print("Roll no: ", self.rollno)
        print("Branch: ",self.branch)

