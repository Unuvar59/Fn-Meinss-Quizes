try:
    from firebase import firebase
    
except:
    raise ModuleNotFoundError("You should check library.txt")

try:
    firebase = firebase.FirebaseApplication("https://fnmeinssquiz-default-rtdb.firebaseio.com/", None) #get our database
except:
    print("You should check your network")
import os
file = __file__ #this file 
dir_ = os.path.dirname(__file__) #dir name for this file
""" #for get persons

database = firebase.get(f"/Persons",None) #getting data
print("Persons:")
for i in database:
    p = firebase.get(f"/Persons/{i}",None)
    print("-----------------")
    for i2 in p:
    
        p2 = firebase.get(f"/Persons/{i}/{i2}",None)
        print(f"{i2}:",p2)
    print("-----------------")
"""
""" #for get question
database = firebase.get(f"/Questions",None) #getting data
print("Questions:")
for i in database:
    p = firebase.get(f"/Questions/{i}",None)
    print(i)
    print("-----------------")
    for i2 in p:
        
        p2 = firebase.get(f"/Questions/{i}/{i2}",None)
        print(f"{i2}:",p2)
    print("-----------------")
"""


""" #for get quizes results
database = firebase.get(f"/Quizes",None) #getting data
print("Quizes:\n")
for i in database:
    p = firebase.get(f"/Quizes/{i}",None)
    print(i)
    print("-----------------")
    for i2 in p:
        
        p2 = firebase.get(f"/Quizes/{i}/{i2}",None)
        print(f"{i2}:",p2)
    print("-----------------")
"""