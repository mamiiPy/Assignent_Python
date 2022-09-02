# ------------------ Assignment_One ----------------
# [1] - Calculator Function 

# add = ['add','A','a']
# sub = ['Sub','sub','S','s']
# mult = ['mlt','m','M']


# def calc(n1,n2,op=add):
#     if op == add :
#         return n1+n2
#     elif op in sub:
#         return n1-n2
#     elif op in mult:
#             return n1*n2
#     else:
#         return f'Sorry! this Operator Does not exisit'

# print(calc(10,25))
# print(calc(10,25,'s'))
# print(calc(10,25,'m'))

# ------------------ End Assignment --------------------


# ------------------ Assignment_Two ----------------
# # [1] - Addition Function

def addition(*numbers):
  i = 0
  num = []
  # Clean Data from Number: 10
  
  while i < len(numbers):
    numbers = list(numbers)
    if numbers[i] != 10:
      num.append(numbers[i])
      # print(num)
    i+=1
  else:
    # Addition Numbers
    print(sum(num))
addition(10,253,10,20,25,36,-85,34,10,10,10,10)
# ------------------------------------------------

# ---------------------- Assignment Three -------------------
# Skills Functions

def show_skills(name, *skills):
  # Check Skills is not empty
  if skills != (): 
    print(f'hello {name} Your skills is:')
    # Loop for skills
    for skill in skills:
      print(skill)
  else:
    print(f'Sorry! {name} You do not have Skills to show')
  

show_skills('mohammed')
show_skills('ahmed','css')
# ---------------------- End Assignment --------------------

# ---------------------- Assignment Four -------------------

# Greeting Function

def say_hello(name='unkoun',age='unkoun',country='unkoun'):
  print(f'hello {name} Your age is {age} and you lived in {country}')

say_hello('mohammed',31,'Miziria')
say_hello()

# ---------------------- End Assignment --------------------