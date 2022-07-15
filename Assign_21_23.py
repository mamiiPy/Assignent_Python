# ----------------------- Assignemnt_Three ---------------------------
# Assign_1: Creat A New List And Find the Index With Two Ways.

# Assign_2: print Even and odd name

# Assign_3: Print the 2,3,4 and the last, after last Index

# Assign_4: Update List

# Assign_5: Add A New Name To List

# Assign_6: Remove name From The List

# Assign_7: Merge A multiple List

# Assign_8: Class the List

# Assign_9: count the List

# Assign_10: Sublist
# ----------------------- End Assignment_Three -----------------------

print('Assign_1: Creat A New List And Find the Index With Two Ways. \n')

Friend = ['Mohammed', 'ahmed', 'Khaled', 'Hamza', 'Iman', 'loubna', ]
# print the First Name with To way
print(Friend[-len(Friend)])
print(Friend[0])

# print the First Name with To way
print(Friend[-1])
print(Friend[len(Friend)-1])
print('#'*30)


print('Assign_2: print Even and odd name \n')
print(Friend[::2])
print(Friend[1::2])
print('#'*30)

print('Assign_3: Print 2,3,4 and last and befor Last name from List \n')
# Print The 2,3,4 index name "khaled","Hamza","Iman"
print(Friend[Friend.index('Khaled'):Friend.index('Iman') + 1])
print(Friend[Friend.index('loubna') - 1:Friend.index('loubna') + 1])


print('#'*30)

print('Assign_4: Update The List \n')
print(Friend)
Friend[-1] = 'Elzero'
Friend[-2] = 'Elzero'
print(Friend)

print('#'*30)

print('Assign_5: Add A new Name To List\n')

print(Friend)
Friend.insert(0, "Hoda")
Friend.append('Zaki')
print(Friend)
print('#'*30)

print('Assign_6: Remove name From The List\n')
print(Friend)
Friend.remove('Hoda')
Friend.remove("Mohammed")
print(Friend)
Friend.pop()
print(Friend)
print('#'*30)

print('Assign_7: Merge A multiple List \n')

friend = ['ahmed', 'ossama', 'hamza']
employee = ['siham', 'rachid', 'amina']
naihbor = ['fayssal', 'boubaker']

print(friend)
friend.extend(employee)
print(friend)
friend.extend(naihbor)
print(friend)
print('#'*30)


print('Assign_8: Class the List \n')
friends = ["Ahmed", "Sayed", "Samah", "Eman", "Ramy", "Shady"]
friends.sort()
print(friends)
friends.reverse()
print(friends)
print('#'*30)

print('Assign_9: Count The List \n')
friends = ["Ahmed", "Sayed", "Samah", "Eman", "Ramy", "Shady"]
print(len(friends))
print('#'*30)

print('Assign_10: Sublist \n')
technologies = ["Html", "CSS", "JS", "Python", ["Django", "Flask", "Web"]]
print(technologies[-1][0])
print(technologies[-1][-1])
