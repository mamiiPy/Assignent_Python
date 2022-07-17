# ----------------------- Control Flow IF - Elif - Else---------------------------
# Assign_1: Input user

# Assign_2: Tenary Condition

# Assign_3: Age Calculator

# Assign_4: Practise Exercices

# ----------------------- End Assignment_Three -----------------------

print('Assign_1: Input user \n')
num1 = int(input('Enter The First Number:\n').strip())
num2 = int(input('Enter Second Number:\n').strip())
operator = input('please! Choose the Assignment Operator ["+" or "-" or "*" or "/" or "%"]:\n').strip()

if operator == "+":
    print(f'Hello! you Choose "{operator}" Operator')
    print(f'your Result is:{num1+num2} ')
elif operator == '-':
    print(f'Hello! you Choose "{operator}" Operator')
    print(f'your Result is:{num1-num2} ')
elif operator == '*':
    print(f'Hello! you Choose "{operator}" Operator')
    print(f'your Result is:{num1*num2} ')
elif operator == '/':
    print(f'Hello! you Choose "{operator}" Operator')
    print(f'your Result is:{num1/num2} ')
elif operator == '-':
    print(f'Hello! you Choose "{operator}" Operator')
    print(f'your Result is:{num1%num2} ')
else:
    print(f'Sorry! this {operator} does not exisit in the System !')


print('#'*30)

print('Assign_2: Tenary Condition\n')
age = 12
print(f'Hello! your Age is {age} and This Application Is Good For you' if age >
      16 else f'Sorry! this Application Is not siutabale for you because your age is {age} under 16')
print('#'*30)

print('Assign_3: Age Calculator \n')
# User Information
age=int(input('Please! type your age:\n').strip())
# Age Unites
month = age * 12
week = month * 4
day = age * 365
hour = day * 24
min = hour * 60
sec = min * 60

# Age unit between 10 and 100
if age >=10 and age < 100 :
    print(f'You Age Is {month} months')
    print(f'You Age Is {week} weeks')
    print(f'You Age Is {day} days')
    print(f'You Age Is {hour} hours')
    print(f'You Age Is {min} minutes')
    print(f'You Age Is {sec} Seconds')
else:
    print(f'Sorry! your age is {age} and it"s Over the siutable range ')
print('#'*30)

print('Assign_4: Practise Exercices \n')
Get country Info
country = str(input('Hello! Type your Country:\n').strip().capitalize())

List of Countries
coun_List = ["Egypt", "Palestine", "Syria","Yemen", "Ksa", "Usa", "Bahrain", "England"]

Price and discount
price = 100
dist = 30

if country in coun_List:
    print(f'Hi! your {country} country has a discount')
    print(f'Hello! you are From {country}, You have a {dist}$ discount')
    print(f'The price of book is {price}, and after discount you can buy it by {price-dist}$')
else:
    print(f'Sorry! your country has not a discount, the price of book is {price}$')


