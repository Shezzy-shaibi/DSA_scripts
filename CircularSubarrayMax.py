
# Link:  https://www.youtube.com/watch?v=zZCdd9zIgts
 
array = [1, 3, 8,10,25,30, -2, 6, -8, 5,-10,-25,-30]    #81
array2 = [11, 10, -20, 5, -3, -5, 8, -13, 10]           #31
 
def SumOfSubarryCircular(arr):
    
    currMax, maxSum, currMin, minSum, total = -1e8,-1e8,1e8,1e8,0
    for num in arr:
        currMax = max(num,currMax + num)
        maxSum = max(maxSum,currMax)
        
        currMin = min(num, currMin + num)
        minSum = min(minSum, currMin)
        
        total += num
    return max(maxSum,total - minSum) if maxSum > 0 else maxSum


print(SumOfSubarryCircular(array))





# def CircSubArr(arr):
#     max_sum total



