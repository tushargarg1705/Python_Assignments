

# Single Inheritance


class Person(object):
 
    # Constructor
    def __init__(self, name):
        self.name = name
 
    # To get name
    def getName(self):
        return self.name
 
    # To check if this person is an employee
    def isEmployee(self):
        return False
 
 
class Employee(Person):
 
    
    def isEmployee(self):
        return True
 
 
# Driver code
emp = Person("Tushar")  
print(emp.getName()) 
print(emp.isEmployee())
 
emp = Employee("Garg")  
print(emp.getName())
print(emp.isEmployee())




# Multiple Inheritance



class Calculator:  
    def Sum(self,a,b):  
        return a+b;  
class Calc:  
    def product(self,a,b):  
        return a*b;  
class Answer(Calculator, Calc):  
    def Divide(self,a,b):  
        return a/b;  
d = Answer()  
print(d.Sum(100,20))  
print(d.product(100,20))  
print(d.Divide(100,20))  