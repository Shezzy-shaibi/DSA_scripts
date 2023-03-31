
def check_duplicate(lis):
    elem_list = []
    for i in lis:
        if lis.count(i) > 1:
            elem_list.append(i)
    set_ = set(elem_list)
    print("Duplicate elements are", set_)
            


def check_dup_2(lis):
    print("Function 2:  ",set(i for i in lis if lis.count(i) > 1))
    
    
    
lis = [1,2,3,4,5,2,3,4,7,8,9,0,2,2,3,4]

check_duplicate(lis)

check_dup_2(lis)






def checkDuplicate(arr):
    newSet = set()
    for item in arr:
        if item in newSet:
            return True
        else:
            newSet.add(item)
    return False

     
print(checkDuplicate([1,2,3,4,5,2,3,4,7,8,9,0,2,2,3,4]))