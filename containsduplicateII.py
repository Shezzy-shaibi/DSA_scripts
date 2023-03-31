
"""
https://leetcode.com/problems/contains-duplicate-ii/

"""

def containsNearbyDuplicate(nums,k):
    hashmap = dict()
    for i,n in enumerate(nums):
        if n in hashmap and (i - hashmap[n]) <= k:
            return True
        else:
            hashmap[n] = i
    return False
                    