import random as rd

def bubbleSort(arr): 
    n = len(arr) 
  
    # Traverse through all array elements 
    for i in range(n):   
        # Last i elements are already in place 
        for j in range(0, n-i-1): 
            # traverse the array from 0 to n-i-1 
            # Swap if the element found is greater 
            # than the next element 
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

def test():
    for i in range(10):
        arr = [rd.randint(1, 100) for i in range(rd.randint(5, 15))]
        print(arr)
        bubbleSort(arr) 
  
        print ("Sorted array is:") 
        for i in range(len(arr)): 
            print ("%d" %arr[i])

test()