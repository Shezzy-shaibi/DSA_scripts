
import math

for number in range(100,200):
    if all(number%i != 0 for i in range(2,int(math.sqrt(number)) +1 )):
        print(number)
        
        

def isPrime(num):
    for i in range(2, int(math.sqrt(num)) +1):
        return False if num%i==0 else True
    
print(isPrime(7))