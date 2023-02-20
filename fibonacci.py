

# Program to find fibonacci numbers upto 30

n = int(input("Enter the number of iterations you want: "))

# first two terms
n1, n2 = 0, 1
count = 0

# check if the number of terms is valid
if n <= 0:
   print("Entered number is negative")


elif n == 1:
   print("Fibonacci sequence upto",n,":")
   print(n1)



else:
   print("Fibonacci sequence:")
   while count < n:
       print(n1)
       c = n1 + n2
       # update values
       n1 = n2
       n2 = c
       count += 1