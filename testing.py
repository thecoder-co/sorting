import random as rd

def bubbleSort(arr):
    print('||||||||||||||||||||||||||||||||||||||||||||||||||||||')
    n = len(arr)
    print(arr)
    # Traverse through all array elements 
    for i in range(n):
          
        # Last i elements are already in place 
        for j in range(0, n-i-1): 
            
            # traverse the array from 0 to n-i-1 
            # Swap if the element found is greater 
            # than the next element 
            if arr[j] > arr[j+1]:
                print ('{} greater than {}, exchanging'.format(arr[j], arr[j+1]))
                arr[j], arr[j+1] = arr[j+1], arr[j]
                print('{} sorted to this point'.format(arr))

def test():
    for i in range(10):
        arr = [rd.randint(1, 100) for i in range(rd.randint(5, 15))]
        bubbleSort(arr)

        test = True
  
        print ("Sorted array is:", arr) 
        for i in range(len(arr)-1):
            if arr[i] > arr[i+1]:
                test = False
            else:
                pass
        if test:
            print('passed')
        else:
            print('failed')

test()
