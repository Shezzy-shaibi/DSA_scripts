
def IsPrimeNum(f,t):
    for i in range(f,t):
        if i % 2 == 0:
            pass
        elif i % 3 == 0:
            pass
        else:
            print(i)
            
            
print(IsPrimeNum(10,20))


import random
from random import choice, shuffle

s = random.shuffle
c = choice
shuffle