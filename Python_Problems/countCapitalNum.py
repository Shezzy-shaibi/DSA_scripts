


import re


def findCapitalLetters(file):
    count = 0
    with open(file) as f:
        reading = f.read()
        for i in reading:
            if i.isupper():
                count +=1
    
    return count

# Now one liner

def OneLinerfindCapitalLetters(file):
    with open(file) as f:
        reading = f.read()
        count = sum(1 for char in reading if char.isupper())
        
    return count

 