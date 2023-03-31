from curses.ascii import isdigit


"Extract digits from string"


str1 = "My name is 344Muhmmad Shahzaib 7645Rehmat" 


res = ''.join(filter(lambda i: i.isdigit(), str1))

print(res)