# assignment 01
# values = (0,1,2)
# if any(values): # Check if there are one Element is true
#     my_var = 0 # The condition Succssede
# my_list = [True,1,1,['A','B'],10.5,my_var ] # my_var = 0 because the condition above is true 
# if all(my_list[:4]) or all(my_list[:6]) or all(my_list[:]): # Check if any one of All Condition is true  
#     print('Good') # this is Output because there is on condition is true ===> all[my_list[:4]] 
# else:
#     print('Bad') # 
# # Good

# Assignment 02
# v = 40

# my_range = list(range(v))

# print(my_range)
# print(sum(my_range,v))
# print(pow(v,v,v))

# print(sum(my_range,v)+ pow(v,v,v))

# Assignemnt 04
# 01 - make all function
# 02 - make any function
# 03 - make max function
# 04 - make min function

# 01 - make all function


# def my_all(myList):
#     for func in myList:
#         if bool(func) != True:
#             return 'The list is False'
#             break
#     else:
#         return 'the list is True'
# print(my_all([1, 2, 3, []]))
# print(my_all([1, 2, 3]))

# 02 - make any function


# def my_any(myList):
#     for func in myList:
#         if bool(func) == True:
#             return 'The list is True'
#             break
#     else:
#         return 'the list is False'
# print(my_any([(), 0, False]))
# print(my_any([1, 2, 3]))

# 03 - make max function
def my_max(max_list):
    if max_list == tuple:
        max_list = list(max_list)
    for max in range(len(max_list) - 1):
        if max_list[0] > max_list[1] :
            max_list.remove(max_list[1])
        else:
            max_list.remove(max_list[0])
    print(max_list)
my_max([-55,-300,1000,10,15,2,-25,23,66,200])

# # 04 - make min function
# def my_min(min_list):
#     if type(min_list) == tuple:
#         print('true')
#         min_list = list(min_list)
#     for min in range(len(min_list) - 1):
#         if min_list[0] < min_list[1] :
#             min_list.remove(min_list[1])
#         else:
#             min_list.remove(min_list[0])
#     print(min_list)
# my_min((-55,-300,1000,10,15,2,-25,23,66,200,-10000))

# mylist = [12,16]
# print(type(mylist))
# if type(mylist) == list:
#     print('true')
    


