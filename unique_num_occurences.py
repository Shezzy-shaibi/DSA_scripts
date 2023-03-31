from collections import Counter

def uniqeNumOccurences(nums):
    hashmap = dict(Counter(nums))
    lis = hashmap.values()
    return True if len(lis) == len(set(lis)) else False
    

print(uniqeNumOccurences([1,2,2,1,1,5]))