class Pair():
    def __init__(self):
        self.min = 0
        self.max = 0
        
def GetMinMax(arr):
    minmax = Pair()
    if len(arr) == 1:
        minmax.min = arr[0]
        minmax.max = arr[0]
        return minmax
    
    if arr[0] > arr[1]:
        minmax.max = arr[0]
        minmax.min = arr[1]
    else:
        minmax.max = arr[1]
        minmax.min = arr[0]
    
    for i in range(2,len(arr)):
        if arr[i] > minmax.max:
            minmax.max = arr[i]
        elif arr[i] < minmax.min:
            minmax.min = arr[i]
    return minmax


arr = [0,1,9,5,6,3]
res = GetMinMax(arr)
print("Maximum: ",res.max, "Minimum: ", res.min)