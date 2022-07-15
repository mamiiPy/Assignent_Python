# ----------------------- Set & Dictionary ---------------------------
# Assign_1: Creat a Unique_list.

# Assign_2: Creat A new Set and Concatenate

# Assign_3: Creat A new Set Make same changing

# Assign_4: Set Joind

# Assign_5: Dictionary
# ----------------------- End Assignment_Three -----------------------

print('Assign_1: Creat a Unique_list \n')

my_list = [1, 2, 3, 3, 4, 5, 1]
unique_list = set(my_list)
print(unique_list)
unique_list = list(unique_list)
print(type(unique_list))
print(unique_list)
# unique_list.pop()
unique_list.remove(len(unique_list))
print(unique_list)
print('#'*30)

print('Assign_2: Creat A new Set and Concatenate \n')
num = {1, 2, 3}
let = {'a', 'b', 'c'}
# Concat_One : Union Method
print(num | let)

num = {1, 2, 3}
let = {'a', 'b', 'c'}
# Concate_Two : Update Method
num.update(let)
print(num)

# Concate_Three: Symethric_difference Methode
num = {1, 2, 3}
let = {'a', 'b', 'c'}
print(num ^ let)
print('#'*30)

print(' Assign_3: Creat A new Set Make same changing \n')
my_set = {1, 2, 3}
let = {'a', 'b', 'c'}
print(my_set)
my_set.clear()
print(my_set)
my_set.add('a')
my_set.add('b')
print(my_set)
my_set.symmetric_difference_update(let)
my_set.remove('c')
print(my_set)
print('#'*30)

print('Assign_4: Set Joind \n')
set_one = {1, 2, 3}
set_two = {1, 2, 3, 4, 5, 6}
print(set_one.issubset(set_two))
print('#'*30)

print('Assign_5: Dictionary \n')
skill = {
  'Html':'90%',
  'Css':"60%",
  'Python':"50%"
}

skill['Php'] = '85%'
print(f"Html Progress is: {skill['Html']}")
print(f"Css Progress is: {skill['Css']}")
print(f"Python Progress is: {skill['Python']}")
print(f"Php Progress is: {skill['Php']}")
