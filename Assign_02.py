# ----------------------- Assignemnt_One ---------------------------
# Assign_1: Creat a Three Varibles and Print it ###"Hello 'Osama', How You Doing \ """ Your Age Is "38"" + And Your Country Is: Egypt###

# Assign_2: print The Three Varibles In Multibale line

# Assign_3: Indexing

# Assign_4: Slicing

# Assign_5: Remove Caracters

# Assign_6: Zero Fill

# Assign_7: Decorator

# Assign_8: sweap The Caravters

# Assign_9: find Caracters

# Assign_10: Position of Letters

# Assign_11&12: Replace Caracters

# Assign_13: print Formatting

# ----------------------- End Assignment_one -----------------------

print('Assign_1: Print The Varibles\n')

name = "'mohammed'"
age = '"31"'
country = 'algeria'
print('"Hello!' + name + ', How You Doing \ """ Your Age Is: ' +
      age + '\"\ +  + And Your Country Is: ' + country)
print('#'*30)


print('Assign_2: make varibles In Multibles Lines\n')

print('"Hello!' + name + ', How You Doing \ \n """Your Age Is: ' +
      age + '\"\ +\n And Your Country Is: ' + country)
print('#'*30)

print('Assign_3: indexing\n')
name = 'Elzero'
print('Second Letter is: '+name[1])
print('Third Letter is: '+name[2])
print('Last Letter Letter is: '+name[-1])
print('#'*30)
print('Assign_4: Slicing\n')
name = 'Elzero'
# Needed Output
# "lze"
# "Ezr"
# "rzE
print(name[1:4])
print(name[::2])
print(name[name.index('r')]+name[name.index('z')]+name[name.index('E')])
print('#'*30)

print('Assign_5: Assign_5: Remove Caracters\n')

name = "#@#@Elzero#@#@"
print(name.strip('@#'))
print('#'*30)

print('Assign_6: Zero Fill\n')

num1 = "9"
num2 = "15"
num3 = "130"
num4 = "950"
num5 = "1500"

print(num1.zfill(4))
print(num2.zfill(4))
print(num3.zfill(4))
print(num4.zfill(4))
print(num5.zfill(4))
print('#' * 30)

print('Assign_7: Decorator\n')

name_one = "Osama"
name_two = "Osama_Elzero"
print(name_one.rjust(20, "@"))
print(name_two.rjust(20, "@"))
print('#'*30)

print('Assign_8: Sweap Caracters\n')

name_one = "OSamA"
name_two = "osaMA"
print(name_one.swapcase())
print(name_two.swapcase())
print('#'*30)

print('Assign_9: find Caracters\n')
msg = "I Love Python And Although Love Elzero Web School"
print(msg.count('Love'))
print('#'*30)

print('Assign_10: Position of Letters\n')

name = 'Elzero'
print(name.index('z'))
print(name.find('z'))

print('#'*30)

print('Assign_11_&_12: Replace Caracters\n')

msg = "I <3 Python And Although <3 Elzero Web School"
print(msg.replace('<3', 'Love'))

print('#'*30)

print('Assign_13: print Formatting\n')
name = 'mohammed'
age = 31
Country = 'Algeria'
print(
    f'My name Is: {name}, and My age Is: {age}, and my country Is: {country}')
