# ----------------------- Boolean & Operator & Assignment & Comparison & User Input ---------------------------
# Assign_1: Input user

# Assign_2: User Input Confirmation

# Assign_3: input User Detection

# Assign_4: Email_Slicing

# ----------------------- End Assignment_Three -----------------------

print('Assign_1: Input user \n')
name = input('Please! enter your name:\n').capitalize().strip()
print(f'hello! {name},happy to see you here')
print('#'*30)

print('Assign_2: User Input Confirmation \n')
age = int(input('pleas! Enter Your Age:\n'))
print(f'Hello! you age is under 16, Some Articles Is Not Suitable For You' if age < 16 else f'Hello! you age is Greather 16, Some Articles Is Suitable For You'),
print('#'*30)

print('Assign_3: input User Detection \n')
first_name = input('Please! type your First Name:\n').strip().capitalize()
familly_name = input('Please! type your Familly Name:\n').strip().capitalize()
print(f"Hello! {first_name}.{familly_name:.1},Happy To see You ?")
print('#'*30)

print('Assign_4: Assignment Operators \n')
usermail = input('Please! type Your Mail:\n').strip().lower()
print(f'Hello! Your user name is: {usermail[:usermail.index("@")].capitalize()} ,Happy to see you ?')
print(f'Hello! You account Is: {usermail[usermail.index("@") + 1:usermail.index(".")]} ')
print(f'Hello! You Domain  Is: {usermail[usermail.index(".")+1:]} ')


