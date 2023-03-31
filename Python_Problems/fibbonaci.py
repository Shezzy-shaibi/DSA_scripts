def func(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return func(n-1) + func(n-2)
    
    
for i in range(0,20):
    print(func(i))
    


def fibonacciFunc(num):
    if num==0:
        return 0
    elif num==1:
        return 1
    else:
        return fibonacciFunc(num-1) + fibonacciFunc(num-2)
    
for i in range(10):
    print(fibonacciFunc(i))
    