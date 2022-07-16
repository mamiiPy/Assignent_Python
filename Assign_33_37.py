# ----------------------- Boolean & Operator & Assignment & Comparison & User Input ---------------------------
# Assign_1: Bool Data

# Assign_2: Bool Confirmation

# Assign_3: Bool Confirmation

# Assign_4: Assignment Operators

# Assign_5: Dictionary
# ----------------------- End Assignment_Three -----------------------

print('Assign_1: Bool Data \n')

print(bool(int))
print(bool(str))
print(bool(5))
print(bool(-10))
print(bool(""))
print(bool([]))
print(bool(False))
print(bool(0))
print('#'*30)

print('Assign_2: Creat A new Set and Concatenate \n')
html = 60
Css = 70
Python = 65
print(html and Css and Python > 50)
print('#'*30)

print('Assign_3: Bool Confirmation \n')
num_one = 10
num_two = 20
num = 20
print(num > num_one or num > num_two)
print(num_one > num and num_two > num)
print('#'*30)

print('Assign_4: Assignment Operators \n')
num_one = 10
num_two = 20
result = num_one + num_two
print(result)
result **= 3
print(result)
result %= 26000
print(result)
result /= 5
print(result)
result=str(result)
print(type(result))
print('#'*30)