
"Approach 1"

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    
    else:
        return fibonacci(n-1) + fibonacci(n-2)
    


for i in range(7):
    print(fibonacci(i))
    
"Approach2"

def better_fibonacci(rng):
    n1,n2 = 0,1
    if rng == 0:
        print(n1)
    elif rng ==1:
        print(n2)
        
    else:
        for i in range(rng):
            print(n1)
            nth = n1+n2
            
            n1 = n2
            n2 = nth

better_fibonacci(7)