# Write a python program to create a class ‗Rectangle‘. This class should include a
# constructor to initialize the dimensions. Include a function in the class to compute the area of
# the rectangle. Create objects of the class and print area.

class Rectangle:
    def __init__(self,length,breadth):
        self.length=length
        self.breadth=breadth
    
    def findArea(self):
        return int(self.length)* int(self.breadth);

obj=Rectangle(5,10)
print("Area of Initial rectangle:"+str(obj.findArea()))
n,m=input("Enter dimensions of rectanlge space separated").split()
obj1=Rectangle(int(n),int(m))
print("Area:" + str(obj1.findArea()))
