#  Its order is O(log(n))

"""
How its order is logn
As in binary search we will sort array and then in sorted array we pick the middle element. 
And if that number will be greater than the number we are searching then we will skip the 
all the numbers greater than the middle element and we will search only from left numbers and then again we will 
apply this rule and so on untill we will find exact element.
so

iteration 1 = n/2
iteration 2 = n/2^2
iteration k = n/2^k

Now,

n = 2^k
applying log both side

log2 n = log2 2^k
log2 n = k * log2 2          ._. log2 2 == 1

 k = log n


"""

 
arr = [3,4,2,4,6,4,2,9,8,7,12,13,45]

f_num = 12

def binary_search(arr, f_num):
    arr.sort()
    low = 0
    high = len(arr) -1
    mid = 0
    while low<=high:
        mid = (low + high) // 2
        if arr[mid]<f_num:
            low = mid + 1
        elif arr[mid]>f_num:
            high = mid-1
        else:
            return mid
            
         
         
print(binary_search(arr,f_num))