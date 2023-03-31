
"""
https://leetcode.com/problems/determine-if-two-events-have-conflict
"""

event1 = ["01:15","02:00"]
event2 = ["02:00","03:00"]

def haveConflict(event1, event2):
    return max(event1[0], event2[0]) <= min(event1[1], event2[1])
