"""
https://leetcode.com/problems/circular-sentence/
"""
 
def CircularArray(sentence):
    sentence = sentence.split(" ")
    if sentence[0][0] == sentence[-1][-1]:
        for i in range(len(sentence)):   
            if sentence[i][0] != sentence[i-1][-1]:
            # print(sentence[i],sentence[i-1])
                return False
        return True
    

print(CircularArray("leetcode exercises sound delightful"))