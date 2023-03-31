
# check if the array contains duplicate


array = [1,2,3,1]    #True
array2 = [1,2,3,4]    #False

# def ContainsDuplicate(arr):
#     for i in range(len(arr)):
#         for j in range(len(arr)):
#             if i != j:
#                 if arr[i] == arr[j]:
#                     return True
#                 else:
#                     return False
            
# print("Normal Case",ContainsDuplicate(array))



#2nd Approach O(n)


def BestContainsDuplicate(arr):
    has_in_set = set()
    
    for elm in arr:
        if elm in has_in_set:
            return True
        else:
            has_in_set.add(elm)
    return False

print("Best Case",BestContainsDuplicate(array))