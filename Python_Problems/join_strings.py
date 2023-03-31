str1 = "My name is "
str2 = "Muhammad Shahzaib Rehmat"

joind_str_plus = str1 + str2 
# joind_str = "".join(str1,str2)      #this will give you an error
joind_str = "".join((str1,str2))    # Two paranthesis are required.

print("join with plus", joind_str_plus)

print("with built in join function",joind_str)
