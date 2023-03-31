
import math
def check_prime_num(num):
    if all(num%i != 0 for i in range(2,int(math.sqrt(num))+1)):
        return True
    else:  
        return False
    
    
number = input("Enter num: \n")
print(check_prime_num(number))

def isPrime(num):
    if num == 1:
        return False
    if all(num%i != 0 for i in range(2,int(math.sqrt(num))+1)):
        return True
    else:
        return False
    
print(isPrime(number))