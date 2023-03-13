# # Assignment 01

# # Make the define function 
# friends_map = ["AEmanS", "AAhmedS", "DSamehF", "LOsamaL"]
# # def clean_char(clean):
# #     return clean[1:-1]
# # cleaned_list = map(clean_char,friends_map)
# # for remove in cleaned_list:
# #     print(remove)
    
# # Make the lambda function
# cleaned_list = map(lambda clean : clean[1:-1], friends_map)
# for remove in cleaned_list:
#     print(remove)

# Assignment 02
# make filter with define function

friends_filter = ["Osama", "Wessam", "Amal", "Essam", "Gamal", "Othman"]
# def get_names(names_list):
#     return names_list.endswith('m')
# names = filter(get_names, friends_filter)
# for name in names:
#     print(name)

# make filter with lambda function
# get_names = filter(lambda names_list : names_list.endswith('m'), friends_filter)
# for name in get_names:
#     print(name)

# Assignemt 03

# nums = [2, 4, 6, 2]

# make reduce with define function
# from functools import reduce
# def multi(n1,n2):
#     return n1 * n2
# result = reduce(multi , nums)
# print(result)

# make reduce with lambda function
# solution = reduce(lambda num1,num2: num1 * num2 ,nums)
# print(solution)


# Assignemnt 04

skills = ("HTML", "CSS", 10, "PHP", "Python", 20, "JavaScript")
reverse = enumerate(reversed(skills),50)

for index,skill in reverse:
    if type(skill) != int:
        print(f'{index}-{skill}')

print('#' * 50)

reverseSkills = reversed(skills)

for skill in reverseSkills:
    ind = skills.index(skill) + 1
    if type(skill) != int:
        print(f'{ind}-{skill}')

