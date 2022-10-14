# Write a python program to create a class ‗Rectangle‘. This class should include a
# constructor to initialize the dimensions. Include a function in the class to compute the area of
# the rectangle. Create objects of the class and print area.

#Class defination
class Rectangle:
    def __init__(self,length,breadth):
        self.length=length
        self.breadth=breadth
   #Function to find area of reactangle 
    def findArea(self):
        return int(self.length)* int(self.breadth);
#Creating object by passing values
obj=Rectangle(5,10)
print("Area of Initial rectangle:"+str(obj.findArea()))
n,m=input("Enter dimensions of rectanlge space separated").split()
#creating object by passing variable inputs
obj1=Rectangle(int(n),int(m))
#Print area using member function 
print("Area:" + str(obj1.findArea()))
