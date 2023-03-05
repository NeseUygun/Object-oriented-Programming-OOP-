# Polymorphism in Class Methods
# It refers to the use of a single type entity (method, operator or object) to represent different types in different scenarios.
#A child class inherits all the methods from the parent class. However, in some situations, the method inherited from the parent class doesn’t quite fit into the child class. 
#In such cases, you will have to re-implement method in the child class.

class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def __add__(self,other):
        x = self.x + other.x
        y = self.y + other.y
        p = Point(x,y)
        return p
    def __repr__(self):
        return f"x={self.x}, y={self.y}"
    
p1 = Point(3,5)
p2 = Point(6,13)
print(p1+p2)