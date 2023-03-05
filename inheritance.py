# 1.Single Inheritence
#When child class is derived from only one parent class. Below code class Animal (parent class) and class Bird (child class) is there. 
#Class Bird (child class) is derived from class Animal. Class Bird holds all the properties of class Animal.

class Animal:
    def eat(self):
        print("yes it eats")
    def sleep(self):
        print("yes it sleeps")

class Bird(Animal):
    def type(self,type):
        self.type = type
    def fly(self):
        print("yes it can fly")
    def speak(self,sound):
        self.sound = sound
        print(f"it speaks: {sound} {sound}")
    def __repr__(self):
        return "this is a " + self.type

# 2. Multilevel Inheritance
#In multilevel inheritance, we have one parent class and child class that is derived or inherited from that parent class. 
# Below code, Person is the parent class for class Employee and class Employee is acting as the parent class for grand-child class Manager.
class Person:
    def __init__(self,age,name):
        self.age = age
        self.name = name
        print("Person constructor called")
    def __repr__(self):
        return f"name: {self.name}, age: {self.age}"
class Employee(Person):
    def __init__(self,name,age,ids,salary):
        super().__init__(age,name)
        self.ids = ids
        self.salary = salary
        print("Employee constructor called") 
    def __repr__(self):
        string = super().__repr__()
        return f"{string}, id: {self.ids}, salary: {self.salary}"
class Manager(Employee):
    def __init__(self,name,age,ids,salary,bonus):
        super().__init__(name,age,ids,salary)
        self.bonus = bonus
        print("Manager constructor called")  
    def __repr__(self):
        string = super().__repr__()
        return f"{string}, bonus: {self.bonus}"

# 3. Hierarchical Inheritance
# When we derive or inherit more than one child class from one(same) parent class. Below code, class Schoolmember is parent class.
# Schoolmember is the parent class for classes Employee and Teacher that both are child class.
class Schoolmember:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def tell(self):
        print(self.name, self.age, end=" ")
class Student(Schoolmember):
    def __init__(self, name, age, rollno, percentage):
        super().__init__(name, age)
        self.rollno = rollno
        self.percentage = percentage
    def tell(self):
        super().tell()
        print(self.rollno, self.percentage)
class Teacher(Schoolmember):
    def __init__(self, name, age,salary):
        super().__init__(name, age)
        self.salary = salary
    def tell(self):
        super().tell()
        print(self.salary)

# 4.Multiple Inheritance
#When child class is derived or inherited from more than one parent class. This is called multiple inheritance. In multiple inheritance, we have two parent classes and one child class that inherits both parent classes properties. 
# Below code Person and Student are parent classes and Sciencestudent is a child class.
# First method
class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
class Student:
    def __init__(self,name,age,rollno,percentage):
        super().__init__(name,age)
        self.rollno = rollno
        self.percentage = percentage
class Sciencestudent(Student,Person):
    def __init__(self,name,age,rollno,percentage,stream):
        super().__init__(name,age,rollno,percentage)
        self.stream = stream
    def tell(self):
        print(self.name, self.age, self.rollno, self.percentage, self.stream)
# Second method
class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
class Student:
    def __init__(self,rollno,percentage):
        self.rollno = rollno
        self.percentage = percentage
class Sciencestudent(Student,Person):
    def __init__(self,name,age,rollno,percentage,stream):
        Person.__init__(self,name,age)
        Student.__init__(self,rollno,percentage)
        self.stream = stream
    def tell(self):
        print(self.name, self.age, self.rollno, self.percentage, self.stream)

# 5. Hybrid Inheritance
# Hybrid Inheritance is the combinations of simple, multiple, multilevel and hierarchical inheritance
class vehicle:   
    def __init__(self,model,mileage,price):
        self.price = price
        self.mileage = mileage
        self.model = model
        
    def show_details(self):
        print(f'Model : {self.model}')
        print(f'Price : {self.price}')
        print(f'Mileage : {self.mileage}')                
class bike(vehicle):  
    def __init__(self,model,mileage,price,tyre,cc):
        super().__init__(model,mileage,price)
        self.cc = cc
        self.tyre = tyre
    
    def show_details(self):
        super().show_details()
        print(f'CC : {self.cc}')
        print(f'Tyres : {self.tyre}')
    
    def rating(self):
        print('4 star')
        
class car(bike,vehicle):    
    def rating(self):
        print('5 star')