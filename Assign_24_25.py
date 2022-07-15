# ----------------------- Tuples ---------------------------
# Assign_1: Creat A New Tuples.

# Assign_2: Creat a new Tuple and make new Changing

# Assign_3: Creat A new Tuple and Concatenate

# Assign_4: Destruct Tuples
# ----------------------- End Assignment_Three -----------------------

print('Assign_1: Creat a New Tuples \n')

name = 'Mohammed',
print(name)
print(type(name))
print('#'*30)

print('Assign_2: Creat a new tuple and make some changing \n')
friend = ('ossama','wafaa','mohammed')
friend = list(friend)
friend[0]='Elzero'
friend = tuple(friend)
print(friend)
print(type(friend))
print(f'{len(friend)} Elements')
print('#'*30)

print('Assign_3: Creat A new Tuple and Concatenate \n')
num = 1,2,3
let = 'a','b','c'
full = num + let
print(full)
print(f'{len(full)} Elements')

print('#'*30)

print('Assign_4: Destruct Tuples \n')
my_Tuples = (True,'mohammed',3,['khaled'])
a,b,_,c = my_Tuples
print(a)
print(b)
print(c)

print('#'*30)

i = {1, 2, 3, 4, 5, "X"} # Ossama,Zero
j = {"Osama", "Zero", 1, 2, 4, "X"} # 3,5
print(i)
print(i.symmetric_difference(j))  # i ^ j
print(i)
# print('Assign_5: Add A new Name To List\n')

# print(Friend)
# Friend.insert(0, "Hoda")
# Friend.append('Zaki')
# print(Friend)
# print('#'*30)

# print('Assign_6: Remove name From The List\n')
# print(Friend)
# Friend.remove('Hoda')
# Friend.remove("Mohammed")
# print(Friend)
# Friend.pop()
# print(Friend)
# print('#'*30)

# print('Assign_7: Merge A multiple List \n')

# friend = ['ahmed', 'ossama', 'hamza']
# employee = ['siham', 'rachid', 'amina']
# naihbor = ['fayssal', 'boubaker']

# print(friend)
# friend.extend(employee)
# print(friend)
# friend.extend(naihbor)
# print(friend)
# print('#'*30)


# print('Assign_8: Class the List \n')
# friends = ["Ahmed", "Sayed", "Samah", "Eman", "Ramy", "Shady"]
# friends.sort()
# print(friends)
# friends.reverse()
# print(friends)
# print('#'*30)

# print('Assign_9: Count The List \n')
# friends = ["Ahmed", "Sayed", "Samah", "Eman", "Ramy", "Shady"]
# print(len(friends))
# print('#'*30)

# print('Assign_10: Sublist \n')
# technologies = ["Html", "CSS", "JS", "Python", ["Django", "Flask", "Web"]]
# print(technologies[-1][0])
# print(technologies[-1][-1])
