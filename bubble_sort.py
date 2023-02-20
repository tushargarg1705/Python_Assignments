


def bubble_sort(arr):
    length = len(arr)
    
    swapped = False
    
    for i in range(length-1):
        
        for j in range(0, length-i-1):

            if arr[j] > arr[j + 1]:
                swapped = True
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
         
        if not swapped:
            
            return
 

arr = [4, 354, 215, 152, 2, 101, 90]
 
bubble_sort(arr)
 
print("Sorted array is:")
for i in range(len(arr)):
    print("% d" % arr[i], end=" ")