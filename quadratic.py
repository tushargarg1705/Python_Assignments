# Program to find roots of a quadratic equation


import cmath  
a = float(input('Enter value of a : '))  
b = float(input('Enter value of b : '))  
c = float(input('Enter value of c : '))  
  
# the discriminant  
d = (b**2) - (4*a*c)  
  
# 2 roots
root_1 = (-b-cmath.sqrt(d))/(2*a)  
root_2= (-b+cmath.sqrt(d))/(2*a)  


print('The roots are {0} and {1}'.format(root_1,root_2)) 