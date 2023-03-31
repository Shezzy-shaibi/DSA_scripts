lis = [1,3,4,5,6,6,3,2,2,66,2,1]
def search(x, lis):
    print(i for i in range(len(lis)) if lis[i] == x )
    
    for i in range(len(lis)):
        if lis[i] == x:
            print(i)
    
search(66, lis)