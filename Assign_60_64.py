# ---------------- Assign One --------------------

# Get_Score Function

# def get_score(**scores):
#     # Loop Function
#     for module,score in scores.items():
#         print(f'{module} ==> {score}')

# # Call Function
# get_score(math=90,Science=90,Languages=82)
# get_score(Logic=70,Problems=60)

# ---------------- End Assign One --------------------

# ---------------- Assign Two ------------------------
# Get_Score_Function + Name
# def get_people_score(name='',**scores):
#     # User does not write his name
#     if name != "" and scores != {}:
        
#     # Print Gretting Message for name added 
#         print(f'Hello {name} Your Skills is :\n')
        
#     # Condition For score not added
#     if scores == {}:
#         print(f'sorry {name} You do not have a score to show')
        
#     # Loop To print score of peoples
#     for module,score in scores.items():
#         print(f'{module} ==> {score}')
    


# # Call Function

# get_people_score(math=90,Science=90,Languages=82)
# print('#'*40)
# get_people_score('ahmed',Logic=70,Problems=60)
# print('#'*40)
# get_people_score('hamza')


# ---------------- End Assign Two --------------------


# ---------------- Assign Three ----------------------------
# [1] - Make Dictionnary 

score_List = {
    'math':90,
    'science': 80,
    'langaue' : 70
}

def get_result(name = '' ,**score_List):
    
    # Check for name not added 
    if name != '' and score_List != {}:
    
    # Print Greeting Message
        print(f'Hello! {name} Your Skills is :\n ')
    # Check for Score_list Not empty
    
    if score_List == {}:
        print(f'Sorry {name} You do not have skills To show')
        
    # Loop for printing Message
    for module,reslt in score_List.items():
        print(f'{module} ==> {reslt}')

get_result(**score_List)
get_result("mohammed")



# ---------------- End Assign Three ------------------------
