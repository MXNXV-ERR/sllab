# Question:Create a Python class called ‘Student’ having ‘name’, ‘age’ as attribute along with a
# list having the marks obtained for three subjects.
# • Create a constructor to initialize two objects of this class.
# • Create a member function called ‘display’ printing the details of a specific object
# • Ask user to enter the values for an object through an ‘accept’ member function.
# • Display these details.

class Student:     #Class created
    def __init__(self):
        self.name=input("Enter student name:")
        self.age=input("Enter student age:")     #name and age attributes along with the list
        self.marks=[]                                       # to contain marks for 3 subjects

    def accept(self):#Accepting values through 'accept' function
        for i in range(3):
            self.marks.append(input("Enter subject "+str(i+1)+" marks"))

    def display(self): #Displaying values through 'display' function
        print("Name: "+self.name)
        print("Age: "+self.age)
        print("Three subject marks are:")
        print(self.marks)
#First Object
print("Student 1:")
s=Student()
s.accept()
#Second Object
print("Student 2:")
s1=Student()
s1.accept()
#Print details of object 
print("\nStudeunt 1");s.display()
print("\nStudeunt 2");s1.display()
