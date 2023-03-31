
"""
The array which could be increasing or decreasing always
"""


def isMonotonic(arr):
    decreasing = False
    increasing = False
    for i in range(1,len(arr)):
        if arr[i]<arr[i-1]:
            decreasing = True
        if arr[i]>arr[i-1]:
            increasing = True
        if increasing and decreasing:
            return False
    return True

arr = [1,2,2,3]

print(isMonotonic(arr))