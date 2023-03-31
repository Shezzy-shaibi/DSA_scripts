

"""
Given an array of N integers where each value represents the number of chocolates in a packet. Each packet can have a variable number of chocolates. There are m students, the task is to distribute chocolate packets such that: 

Each student gets one packet.
The difference between the number of chocolates in the packet with maximum chocolates and the packet with minimum chocolates given to the students is minimum.
"""


def distribution(choco_packet, n):
    choco_packet.sort()
    diff = 1e8
    for i in range(len(choco_packet)-n + 1):
        res = choco_packet[i + n - 1] - choco_packet[i]
        diff = min(diff, res)
    
    return diff
    
arr = [12, 4, 7, 9, 2, 23, 25, 41, 30, 40, 28, 42, 30, 44, 48, 43, 50]
students = 7 
    
print("Check-1",distribution(arr,students))


def chocDistribution(arr,m):
    ln = len(arr)
    result = 1e8
    for i in range(ln -m+1):
        diff = arr[i+m-1] - arr[i]
        result = min(result,diff)
        
    return result

print("Check-2",chocDistribution(arr,students))