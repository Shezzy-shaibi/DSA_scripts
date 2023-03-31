# # Simple Approach

# def reverArray(arr):
#     return arr[::-1]


# arr = [2,4,6,8,10,12,14,16]
# print("Reverse Simple Approach: ", reverArray(arr))


# Another Approach 
# Set first and last index and then swap them and then accordingly
def reverseArray2(arr):
    start = 0
    end = len(arr) - 1
    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start +=1
        end -=1
    return arr
arr = [0,1,4,5,2,7,9,1]
print(reverseArray2(arr))