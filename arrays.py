"""
>  In other languages like c++ and java Static and Dynamic both are exist 
>  But in python Dynamic array is exist which is called List. Although in Numpy you can specify static array.
>  In other languages like Java and C++ homogenius arrays exist which means you can store only one type of elements in a signle array
but in python you can store every type of elements in a single array(List).

For time complexity order check python cheat sheet.

"""

"""
Q1:

Let us say your expense for every month are listed below,
January - 2200
February - 2350
March - 2600
April - 2130
May - 2190
Create a list to store these monthly expenses and using that find out,

1. In Feb, how many dollars you spent extra compare to January?
2. Find out your total expense in first quarter (first three months) of the year.
3. Find out if you spent exactly 2000 dollars in any month
4. June month just finished and your expense is 1980 dollar. Add this item to our monthly expense list
5. You returned an item that you bought in a month of April and
got a refund of 200$. Make a correction to your monthly expense list
based on this


Q2:

You have a list of your favourite marvel super heros.
heros=['spider man','thor','hulk','iron man','captain america']
Using this find out,

1. Length of the list
2. Add 'black panther' at the end of this list
3. You realize that you need to add 'black panther' after 'hulk',
   so remove it from the list first and then add it after 'hulk'
4. Now you don't like thor and hulk because they get angry easily :)
   So you want to remove thor and hulk from list and replace them with doctor strange (because he is cool).
   Do that with one line of code.
5. Sort the heros list in alphabetical order (Hint. Use dir() functions to list down all functions available in list)







"""



def searchList(lis):
    extra_dollars = lis[1] - lis[0] #1
    print(extra_dollars)
    
    total_quarter_ex = lis[0] + lis[1] + lis[3] #2
    print(total_quarter_ex)
    
    result = False
    for i in lis:                   #3     O(n)
        if i==2000:
            result = True

    print(result)
        
        
    lis.append(1980)                #4
    print(lis)
    
    
    lis[3] = lis[3] + 200          #5

    return "Test paased"    

lis = [2200,2350,2600,2130,2190]

searchList(lis)

# =====================================================




def Q2_herolis(lis):
    
    lis.append("black panthar")     #2   O(1)
    print(lis)
                            
                                    #3
    lis.pop()    #pop last item. We have used pop else than remove because its time complexity is O(1)                         
    
    print(lis)
    lis.insert(3,"black panthar")                           #O(n)
    print(lis)
    #4
   
    
    lis[1:3] = ["Doc Strange"]    #  Must be in brackets
    print(lis)
    
    lis.sort()
    print(lis)                                               #5
    
    
heros=['spider man','thor','hulk','iron man','captain america']

    
Q2_herolis(heros)



 