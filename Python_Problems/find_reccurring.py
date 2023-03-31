str1 = "My Name is Muhammad Shahzaib"

#Extract Recurring method

new_str = ''
for i in str1:
    if str1.count(i) == 1:
        new_str = ''.join((new_str,i))
    else:
        pass
    
print(new_str)

 
 