"""
# nput: arr[] = {5, 1, 4, 2, 8}

# First Pass: 

# Bubble sort starts with very first two elements, comparing them to check which one is greater.
# ( 5 1 4 2 8 )  ( 1 5 4 2 8 ), Here, algorithm compares the first two elements, and swaps since 5 > 1. 
# ( 1 5 4 2 8 )   ( 1 4 5 2 8 ), Swap since 5 > 4 
# ( 1 4 5 2 8 )   ( 1 4 2 5 8 ), Swap since 5 > 2 
# ( 1 4 2 5 8 )  ( 1 4 2 5 8 ), Now, since these elements are already in order (8 > 5), algorithm does not swap them

"""


arr = [5, 1, 4, 2, 8]

def bubble_sort(arr):
    sorted = True
    for i in range(len(arr) -1):
        if arr[i]>arr[i+1]:
            arr[i], arr[i+1] = arr[i+1], arr[i]
            sorted = False
    if sorted == False:
        bubble_sort(arr)
    
    return arr

print(bubble_sort(arr))