import os
import mycolors as mc
os.system("")  #if we dont use os, print colors cannot working

try:
    from firebase import firebase
    import random
except:
    raise ModuleNotFoundError(mc.errorcolor + "You should check library.txt" + mc.normalColor)

try:
    firebase = firebase.FirebaseApplication("https://fnmeinssquiz-default-rtdb.firebaseio.com/", None) #get our database
except:
    print(mc.errorcolor + "You should check your network" + mc.normalColor)

def getquestionFunction(category, times):
    database = firebase.get(f"/Questions/{category}",None) #getting data
    datasize = len(database) #checking database size 
    databaselist = list(database) #collecting question keys in a list
    answer_list =[]
    question_list=[]
    other_list = []
    key_list = []
    selector_list = random.sample(range(0,datasize), times)
    for selector in selector_list:
        # selector = random.randint(0,datasize-1) #creating random number between 0 and datasize-1. This is for random selecting
        questioninformation = database[databaselist[selector]] #firstly selecting random a key then selecting question with this key
        question = questioninformation["Question"] #getting selected question
        answer = questioninformation["Answer"] #getting answer for selected question
        other = questioninformation["Other"] #getting other choice for selected question
        other.append(answer) #collecting all choice in other list
        other = choiceMixer_and_Naming(other) #calling choicemixerandnaming
        key_list.append(databaselist[selector])
        question_list.append(question)
        answer_list.append(answer)
        other_list.append(other)

    return question_list, answer_list,other_list,key_list  

def setquestionFunction(category, creator, question, answer, *args):
    data = {
        "Creator":creator,
        "Question":question,
        "Answer":answer,
        "Other":args,
        "Rank":0,
        "Usage":0,
        "Correctly":0
    }
  
    firebase.post(f"/Questions/{category}",data)
# setquestionFunction("Sport","vdfvdf","vfgvgf","vfdvfd","dfvdf","vffvd","vrffevfd")
def choiceMixer_and_Naming(list_):
    usedindex = []
    newlist = []
    
    while not len(newlist) == len(list_): #if lists size aren't equals 
            
        index_ = random.randint(0,len(list_)-1) #creating a random index between 0 and max index of list_

        if not index_ in usedindex: #if this choice didn't append before
            newlist.append(list_[index_]) 
            usedindex.append(index_)

    choicedict = {}
    counter = 0
    choiceKey = ["A","B","C","D"]
    for sentence in newlist:
        choicedict[choiceKey[counter]] = sentence #matching choice key and values
        counter += 1

    return choicedict

def answerChecker(userchoose,answer, choices):
    correct = False
    choiceKey = ["A","B","C","D"]
    if not (userchoose in choiceKey):
        print(mc.errorcolor +  "Geçersiz şık girildi!"+mc.normalColor)
        return False,False
    else:
        if answer == choices[userchoose]:
            correct = True
        else:
            correct = False
        return True,correct

def questionpoint(key,category,point,correct):
    usage = firebase.get(f'/Questions/{category}/{key}/Usage',None)
    firebase.put(f'/Questions/{category}/{key}','Usage',usage+1)
    rank = firebase.get(f'/Questions/{category}/{key}/Rank',None)
    firebase.put(f'/Questions/{category}/{key}','Rank',rank + point)
    correctly = firebase.get(f'/Questions/{category}/{key}/Correctly',None)
    if correct:
        firebase.put(f'/Questions/{category}/{key}','Correctly',correctly + 1)
