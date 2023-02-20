start_no=int(input('Enter the number from which you want to start:'))
end_no=int(input('Enter the number upto which you want to check:'))


def prime(start_no, end_no):

    for num in range(start_no,end_no +1 ):
        if num>1:
            for i in range(2,num):
                if num%i ==0:
                    break;
            
            else:
                print('Prime numbers are:',num)




prime(start_no, end_no)
    
