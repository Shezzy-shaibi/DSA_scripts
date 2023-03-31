 


# def sort_li(list_):
#     num = list_[0]
#     new_ = []
#     for i in list_:
#         if i < num:
#             num = i
            
#         new_.append(num)
#         list_.remove(num)
        
            
#     return new_
# li = [3,2,4,5,6,1,0]
# print(sort_li(li))


data_list = [-5, -23, 5, 0, 23, -6, 23, 67]
new_list = []

# data_list.sort()
# print(data_list)


while data_list:
    num = data_list[0]
    for i in data_list:
        if i < num:
            num = i
    new_list.append(num)
    data_list.remove(num)
        
print(new_list)