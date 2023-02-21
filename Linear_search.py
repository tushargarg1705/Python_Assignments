
# Program for Linear search



def linear_Search(list, n, key):  
    
    for i in range(0, n):  
        if (list[i] == key):  
            return i  
    return -1  
  
  
list = [10 ,31, 15, 54, 27, 97]  
key = 27  
  
n = len(list)  
o = linear_Search(list, n, key)  
if(o == -1):  
    print("Element not found")  
else:  
    print("Element found at index: ", o)  