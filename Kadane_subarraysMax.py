
# The simple approach to solve this problem is to run two for loops and for every subarray check if it is the maximum sum possible. Follow the below steps to solve the problem.

# . Run a loop for i from 0 to n-1, where n is the size of the array.
# . Now, we will run a nested loop for j from i to n-1 and add the value of the element at index j to a variable currentMax.
# . Lastly, for every subarray, we will check if the currentMax is the maximum sum of all contiguous subarrays.

# Link:  https://www.youtube.com/watch?v=yPTghcz7OME
 


# O(n^2)


array = [1, 3, 8,10,25,30, -2, 6, -8, 5,-10,-25,-30]

def SubArray(arr):
    maxSum = -1e8
    maxSumSubArray = []
    for i in range(0,len(arr)):
        subs = []
        sumSubarray = 0
        for j in range(i,len(arr)):
            subs.append(arr[j])
            print(subs)
            sumSubarray = sumSubarray+arr[j]
            if sumSubarray > maxSum:
                maxSum = sumSubarray
    print("sum: ",maxSum)

SubArray(array)


# Link:  https://www.youtube.com/watch?v=yPTghcz7OME
# O(n)    




def SumOfSubArrayMaxOn(arr):
    result = -1e8
    prev_value = 0
    
    for i in arr:
        prev_value = max(i, prev_value + i)
        result = max(result, prev_value)
        
    return ('Sum of Max SubArray',result)
    
    
print(SumOfSubArrayMaxOn(array))