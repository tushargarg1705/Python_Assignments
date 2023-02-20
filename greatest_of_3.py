a=int(input('Enter 1st number: '))
b=int(input('Enter 2nd number: '))
c=int(input('Enter 3rd number: '))

if a>b:
    if a>c:
        print('1st number is greatest ',a)
elif b>a:
    if b>c:
        print('2nd number is greatest ',b)
else:
    print('3rd number is greatest ',c)
    