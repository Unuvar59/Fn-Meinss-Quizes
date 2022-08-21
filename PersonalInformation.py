
import os
from time import sleep
import mycolors as mc
import graphs
import questionEditor
file = __file__ #this file 
dir_ = os.path.dirname(__file__) #dir name for this file


try:
    from firebase import firebase
    import random
except:
    raise ModuleNotFoundError(mc.errorcolor + "You should check library.txt" + mc.normalColor)

try:
    firebase = firebase.FirebaseApplication("https://fnmeinssquiz-default-rtdb.firebaseio.com/", None) #get our database
except:
    print(mc.errorcolor + "You should check your network" + mc.normalColor)

class person_sign():
    def __init__(self):

        username_checker = True #firstly not used but we need running to while 
        while username_checker:
            print(mc.infocolor + "\nWhat is your username?"+mc.normalColor)
            username = input(mc.usercolor + "\t = ").upper().strip()
            username_checker = slagchecker(username)
            if not username_checker:
                username_checker = usernamerepeat(username)


        password_checker = True #firstly not used but we need running to while       
        while password_checker:
            print(mc.infocolor + "\nWhat is your password?"+mc.normalColor)
            password = input(mc.usercolor + "\t = ").strip()        
            password_checker = passwordchecker(password)
            if not (password_checker):
                print(mc.infocolor + "\nWhat is your password again?"+mc.normalColor)
                password2 = input(mc.usercolor + "\t = ").strip()
                if not (password2==password):
                    print(mc.errorcolor + "passwords are not the same" + mc.normalColor)
                    password_checker = True


        bornyear_checker = True #firstly not used but we need running to while 
        while bornyear_checker:
            print(mc.infocolor + "\nWhat is your born year?"+mc.normalColor)
            # TODO: doğum tarihi şuandan sonra olamaz
            bornyear = input(mc.usercolor + "\t = ").upper().strip()        
            bornyear_checker = bornyearchecker(bornyear)


        mail_checker = True #firstly not used but we need running to while       
        while mail_checker:
            print(mc.infocolor + "\nWhat is your mail adress?"+mc.normalColor)
            mail = input(mc.usercolor + "\t = ").lower().strip()        
            mail_checker = mailchecker(mail)
            if not mail_checker:
                mail_checker = mailrepeat(mail)

        question_Checker = True
        while question_Checker:

            print(mc.subinfocolor + "\nWe need your support to improve our question pool"+mc.normalColor)
            sleep(1.5)
            print(mc.subinfocolor + "\nThat's why we ask all our new users to post a question"+mc.normalColor)
            sleep(1.5)
            print(mc.subinfocolor + "\nDon't worry, this will only be a one time transaction\n\n"+mc.normalColor)
            sleep(1.5)
            print(mc.subinfocolor + "\nfirst you have to choose a category:"+mc.normalColor)
            sleep(1)
            fail = True
            while fail:
                print(mc.subinfocolor + "\n[1]- Sport\n[2]- Science\n[3]- General Knowledge\n[4]- History\n[5]- Art"+mc.normalColor)
                print(mc.infocolor + "\nWhich one would you like to choose?" + mc.normalColor)
                try:
                   userchoice = int(input(mc.usercolor + "\t = ").strip())
                except:
                    print(mc.errorcolor + f"You should write 1, 2, 3, 4 or 5\n" + mc.normalColor)
                    continue
            
                if userchoice == 1:
                    question_Checker = questioncreator(username,"Sport")
                    fail = False
                elif userchoice == 2:
                    question_Checker = questioncreator(username,"Science")
                    fail = False
                elif userchoice == 3:
                    question_Checker = questioncreator(username,"General Knowledge")                        
                    fail = False
                elif userchoice == 4:
                    question_Checker = questioncreator(username,"History")                        
                    fail = False
                elif userchoice == 5:
                    question_Checker = questioncreator(username,"Art")                        
                    fail = False
                else:
                    print(mc.errorcolor + f"You should write 1,2,3,4 or 5\n" + mc.normalColor)
                    fail = True
        


        bornyear = int(bornyear)
        self.username = username
        self.bornyear = bornyear
        self.mail = mail    
        self.password = password
        self.saveprofil()

    def saveprofil(self):
        data = {
            "Username":self.username,
            "BornYear":self.bornyear,
            "Mail":self.mail,
            "Password":self.password,
            "Statistic":{"no":"No"}
        }
        try:
            firebase.post("/Persons",data)
            print(mc.subinfocolor + "\nRegistration done successfully"+mc.normalColor)
        except:
            print(mc.errorcolor + "Something went wrong" + mc.normalColor)
# //////////////////

def slagchecker(name):
    badwordsfile = open(f"{dir_}\\badwords.txt", encoding="utf-8",) #opening badwords.txt in our files
    badwordsstr = badwordsfile.read() #converting str
    badwordslist = badwordsstr.split("\n") #split rows one by one

    
    for badword in badwordslist: 
        badword = badword.upper()
        if badword in name: #is there any badword in anywhere in name
            print(mc.errorcolor + f"Try to be more polite! Can't use \"{badword}\"" + mc.normalColor )
            return True

    return False

def questioncreator(username,category):
    question_checker = True
    while question_checker:
        question_checker = False
        print(mc.infocolor + "\nQuestion?" + mc.normalColor)
        user_question = input(mc.usercolor + "\t = ").strip()
        question_checker_temporary = False
        user_question_list = user_question.split()
        for word in user_question_list:
            word = word.upper()
            question_checker_temporary = slagchecker(word)
            if question_checker_temporary:
                question_checker = True
            

    answer_checker = True
    while answer_checker:
        answer_checker = False
        print(mc.infocolor + "Answer?" + mc.normalColor)
        user_answer = input(mc.usercolor + "\t = ").strip()
        answer_checker_temporary = False
        for word in user_answer:
            answer_checker_temporary = slagchecker(word)
            if answer_checker_temporary:
                answer_checker = True
    other = []
    for i in range(3):
        other_checker = True
        while other_checker:
            other_checker = False
            print(mc.infocolor + f"{(i+1)}. Other choice?" + mc.normalColor)
            user_other = input(mc.usercolor + "\t = ").strip()
            other_checker_temporary = False
            for word in user_other:
                other_checker_temporary = slagchecker(word)
                if other_checker_temporary:
                    other_checker = True
        other.append(user_other)
    questionEditor.setquestionFunction(category,username, user_question,user_answer,other[0],other[1],other[2])
    return False
def bornyearchecker(bornyear):


    if not(len(bornyear) == 4):
        print(mc.errorcolor + "Born year must be 4 digits" + mc.normalColor)
        return True
    
    try:
        bornyear = int(bornyear)
    except:
        print(mc.errorcolor + "you must enter an integer" + mc.normalColor)
        return True

    if not( bornyear > 1900):
        print(mc.errorcolor + "Born year cannot be before 1900" + mc.normalColor)
        return True
    
    return False

def mailchecker(mail):
    if not (type(mail) == str):
        print(mc.errorcolor + "you must enter an string" + mc.normalColor)
        return True

    if not("@" in mail):
        print(mc.errorcolor + "mail must contain the @ sign" + mc.normalColor)
        return True
    
    return False

def passwordchecker(password):
    if (len(password)<4 ):
        print(mc.errorcolor + "Password must be at least 4 characters" + mc.normalColor)
        return True

    return False

def usernamerepeat(name):
    database = firebase.get("/Persons",None) #getting data
    usernamelist=[]
    for person_ in database.values():
        if name == (person_["Username"]):
            print(mc.errorcolor + "Username already used" + mc.normalColor)
            return True
    return False

def mailrepeat(mail):
    database = firebase.get("/Persons",None) #getting data
    for person_ in database.values():
        if mail == (person_["Mail"]):
            print(mc.errorcolor + "Mail already used" + mc.normalColor)
            return True
    return False

class person_login():
    os.system("cls")
    def __init__(self):
        checker = True #firstly not used but we need running to while 
        while checker:
            print(mc.infocolor + "\nWhat is your username?"+mc.normalColor)
            username = input(mc.usercolor + "\t = ").upper().strip()
            print(mc.infocolor + "\nWhat is your password?"+mc.normalColor)
            password = input(mc.usercolor + "\t = ").strip()        
            checker = self.correctly(username,password)         
        self.username = username   
        self.password = password
        
    def correctly(self,name,password):
        database = firebase.get("/Persons",None) #getting data
        usernamelist=[]
        for person_ in database.values():
            usernamelist.append(person_["Username"])

        if not name in usernamelist:
            print(mc.errorcolor + "Username not defined" + mc.normalColor)
            return True


        for person_ in database.values():
            if name == (person_["Username"]):
                if(password == person_["Password"]):
                    return False
                else:
                    print(mc.errorcolor + "Password is wrong" + mc.normalColor)
                    return True

        print(mc.errorcolor + "Something went wrong" + mc.normalColor)   
        return True

def getpersoninfo(user):
    username = user.username
    database = firebase.get("/Persons",None) #getting data
    count = 0
    index_ = 0
    for person_ in database.values():
            if username == (person_["Username"]):
                mail = person_["Mail"]
                bornyear = person_["BornYear"]
                password = person_["Password"]
                index_ = count
            count+=1
    passwordsecret = (len(password))*"*"
    
    size_ = 0
    stringlist = [username,mail,str(bornyear),passwordsecret]
    for i in stringlist:
        if len(i) > size_:
            size_ = len(i)

    print(mc.questionbackcolor + ((size_+11)*"-" + mc.normalColor) +
          mc.questioncolor + "\nUsername:  " + mc.subinfocolor + username +
          mc.questioncolor + "\nMail:      "  + mc.subinfocolor + mail +
          mc.questioncolor + "\nBorn Year: "  + mc.subinfocolor + f"{bornyear}" +
          mc.questioncolor + "\nPassword:  "  + mc.subinfocolor +passwordsecret + 
          mc.questionbackcolor +"\n"+ ((size_+11)*"-" + mc.normalColor))
    i = {}
    count = 0
    key = {}
    for i in database:
        if count == index_:
            key = i
        count += 1
    return key


def updateusername(data):
    username_checker = True #firstly not used but we need running to while 
    while username_checker:
        print(mc.infocolor + "\nWhat is your new username?"+mc.normalColor)
        username = input(mc.usercolor + "\t = ").upper().strip()
        username_checker = slagchecker(username)
        if not username_checker:
            username_checker = usernamerepeat(username)
    firebase.put(f'/Persons/{data}','Username',username)
    

def updatemail(data):
    mail_checker = True #firstly not used but we need running to while       
    while mail_checker:
        print(mc.infocolor + "\nWhat is your new mail adress?"+mc.normalColor)
        mail = input(mc.usercolor + "\t = ").lower().strip()        
        mail_checker = mailchecker(mail)
        if not mail_checker:
            mail_checker = mailrepeat(mail)
    firebase.put(f'/Persons/{data}','Mail',mail)

def updatebornyear(data):
    bornyear_checker = True #firstly not used but we need running to while 
    while bornyear_checker:
        print(mc.infocolor + "\nWhat is your new born year?"+mc.normalColor)
        bornyear = input(mc.usercolor + "\t = ").upper().strip()        
        bornyear_checker = bornyearchecker(bornyear)
    firebase.put(f'/Persons/{data}','BornYear',bornyear)

def updatepassword(data):
    password_checker = True #firstly not used but we need running to while       
    while password_checker:
        print(mc.infocolor + "\nWhat is your new password?"+mc.normalColor)
        password = input(mc.usercolor + "\t = ").strip()        
        password_checker = passwordchecker(password)
        if not (password_checker):
            print(mc.infocolor + "\nWhat is your new password again?"+mc.normalColor)
            password2 = input(mc.usercolor + "\t = ").strip()
            if not (password2==password):
                print(mc.errorcolor + "passwords are not the same" + mc.normalColor)
                password_checker = True
    firebase.put(f'/Persons/{data}','Password',password)

def deleteacount(data):
    firebase.delete(f'/Persons/{data}',"")

def userstatistic(user,time,correct,category):
    database = firebase.get("/Persons",None) #getting data
    database_keys = list(database.keys())
    name = user.username
    usernamelist=[]
    for person_ in database.values():
        usernamelist.append(person_["Username"])
    counter = 0    
    for person_ in database.values():
        if name == (person_["Username"]):
            key = database_keys[counter]
        counter += 1

    data={
        "Time":time,
        "Correct": correct,
        "Category" :category
    }
    firebase.post(f"/Persons/{key}/Statistic",data)
    return True    


def getuserstatistic(user):
    database = firebase.get("/Persons",None) #getting data
    database_keys = list(database.keys())
    name = user.username
    usernamelist=[]

    totalstatistic = {
        "Sport":{
            "Correct":0,
            "Time":0,
            "Usage":0
        },
        "Science":{
            "Correct":0,
            "Time":0,
            "Usage":0
        },
        "General Knowledge":{
            "Correct":0,
            "Time":0,
            "Usage":0
        },
        "History":{
            "Correct":0,
            "Time":0,
            "Usage":0
        },
        "Art":{
            "Correct":0,
            "Time":0,
            "Usage":0
        }

    }
    for person_ in database.values():
    
        for data in person_["Statistic"].values():
            if not data == "No":
                category = data["Category"]
                correct = data["Correct"]
                time = data["Time"]
                totalcorrect = totalstatistic[category]["Correct"]
                totalusage = totalstatistic[category]["Usage"]
                totalusage += 1
                if correct:
                    totalcorrect += 1
                    totalstatistic[category]["Correct"] = totalcorrect
                totaltime = totalstatistic[category]["Time"]
                totaltime += time
                totalstatistic[category]["Time"] = totaltime
                totalstatistic[category]["Usage"] = totalusage
        
    for person_ in database.values():
        usernamelist.append(person_["Username"])
    counter = 0    
    
    for person_ in database.values():
        if name == (person_["Username"]):
            key = database_keys[counter]
        counter += 1
    if not (totalstatistic["History"]["Usage"] == 0):
        average_history = totalstatistic["History"]["Correct"]/totalstatistic["History"]["Usage"]
        average_history_time = totalstatistic["History"]["Time"]/totalstatistic["History"]["Usage"]
    if not (totalstatistic["General Knowledge"]["Usage"] == 0):
        average_GeneralKnowledge = totalstatistic["General Knowledge"]["Correct"]/totalstatistic["General Knowledge"]["Usage"]
        average_GeneralKnowledge_time = totalstatistic["General Knowledge"]["Time"]/totalstatistic["General Knowledge"]["Usage"]

    if not (totalstatistic["Sport"]["Usage"] == 0):
        average_Sport = totalstatistic["Sport"]["Correct"]/totalstatistic["Sport"]["Usage"]
        average_Sport_time = totalstatistic["Sport"]["Time"]/totalstatistic["Sport"]["Usage"]

    if not (totalstatistic["Science"]["Usage"] == 0):
        average_Science = totalstatistic["Science"]["Correct"]/totalstatistic["Science"]["Usage"]
        average_Science_time= totalstatistic["Science"]["Time"]/totalstatistic["Science"]["Usage"]

    if not (totalstatistic["Art"]["Usage"] == 0):
        average_Art = totalstatistic["Art"]["Correct"]/totalstatistic["Art"]["Usage"]
        average_Art_time = totalstatistic["Art"]["Time"]/totalstatistic["Art"]["Usage"]

    
    Totalcorrect_everycategory_average = (totalstatistic["History"]["Correct"]+totalstatistic["General Knowledge"]["Correct"]+
                                          totalstatistic["Sport"]["Correct"]+totalstatistic["Science"]["Correct"]+
                                          totalstatistic["Art"]["Correct"])
    Totalusage_everycategory_average =    (totalstatistic["History"]["Usage"]+totalstatistic["General Knowledge"]["Usage"]+
                                          totalstatistic["Sport"]["Usage"]+totalstatistic["Science"]["Usage"]+
                                          totalstatistic["Art"]["Usage"])
    Totaltime_everycategory_average =    (totalstatistic["History"]["Time"]+totalstatistic["General Knowledge"]["Time"]+
                                          totalstatistic["Sport"]["Time"]+totalstatistic["Science"]["Time"]+
                                          totalstatistic["Art"]["Time"])
    totalstatistic = {
        "Sport":{
            "Correct":0,
            "Time":0,
            "Usage":0
        },
        "Science":{
            "Correct":0,
            "Time":0,
            "Usage":0
        },
        "General Knowledge":{
            "Correct":0,
            "Time":0,
            "Usage":0
        },
        "History":{
            "Correct":0,
            "Time":0,
            "Usage":0
        },
        "Art":{
            "Correct":0,
            "Time":0,
            "Usage":0
        }
    }
   
    database = firebase.get(f"/Persons/{key}/Statistic",None)
    for data in database.values():
        if not data == "No":
            category = data["Category"]
            correct = data["Correct"]
            time = data["Time"]
            totalcorrect = totalstatistic[category]["Correct"]
            totalusage = totalstatistic[category]["Usage"]
            totalusage += 1
            if correct:
                totalcorrect += 1
                totalstatistic[category]["Correct"] = totalcorrect
            totaltime = totalstatistic[category]["Time"]
            totaltime += time
            totalstatistic[category]["Time"] = totaltime
            totalstatistic[category]["Usage"] = totalusage
    

    Totalcorrect_everycategory_user = (totalstatistic["History"]["Correct"]+totalstatistic["General Knowledge"]["Correct"]+
                                          totalstatistic["Sport"]["Correct"]+totalstatistic["Science"]["Correct"]+
                                          totalstatistic["Art"]["Correct"])
    Totalusage_everycategory_user =    (totalstatistic["History"]["Usage"]+totalstatistic["General Knowledge"]["Usage"]+
                                          totalstatistic["Sport"]["Usage"]+totalstatistic["Science"]["Usage"]+
                                          totalstatistic["Art"]["Usage"])
    if not Totalusage_everycategory_user == 0:
        print(mc.correctColor + ("*"*100)+mc.normalColor)
        print(mc.correctColor +'* {:^96} *'.format('Correct')+mc.normalColor)
        print(mc.correctColor + ("*"*100)+mc.normalColor)
        sleep(1)
        if not (totalstatistic["History"]["Usage"] == 0):
            user_history = totalstatistic["History"]["Correct"]/totalstatistic["History"]["Usage"]
            graphs.singlegraph("History",user_history,average_history)
            sleep(1)

        if not (totalstatistic["General Knowledge"]["Usage"] == 0):
            user_GeneralKnowledge = totalstatistic["General Knowledge"]["Correct"]/totalstatistic["General Knowledge"]["Usage"]
            graphs.singlegraph("General Knowledge",user_GeneralKnowledge,average_GeneralKnowledge)
            sleep(1)
        if not (totalstatistic["Sport"]["Usage"] == 0):
            user_Sport = totalstatistic["Sport"]["Correct"]/totalstatistic["Sport"]["Usage"]
            graphs.singlegraph("Sport",user_Sport,average_Sport)    
            sleep(1)
        if not (totalstatistic["Science"]["Usage"] == 0):
            user_Science = totalstatistic["Science"]["Correct"]/totalstatistic["Science"]["Usage"]
            graphs.singlegraph("Science",user_Science,average_Science)
            sleep(1)    
        if not (totalstatistic["Art"]["Usage"] == 0):
            user_Art = totalstatistic["Art"]["Correct"]/totalstatistic["Art"]["Usage"]
            graphs.singlegraph("Art",user_Art,average_Art)
            sleep(1)
            graphs.singlegraph("Total",(Totalcorrect_everycategory_user/Totalusage_everycategory_user),(Totalcorrect_everycategory_average/Totalusage_everycategory_average))
            
        print("")
        print(mc.correctColor + ("*"*100)+mc.normalColor)
        print(mc.correctColor + ("*"*100)+mc.normalColor)
        sleep(1)

        Totaltime_everycategory_user = (totalstatistic["History"]["Time"]+totalstatistic["General Knowledge"]["Time"]+
                                          totalstatistic["Sport"]["Time"]+totalstatistic["Science"]["Time"]+
                                          totalstatistic["Art"]["Time"])
        print("\n")
        print(mc.correctColor + ("*"*100)+mc.normalColor)
        print(mc.correctColor +'* {:^98} *'.format('Time')+mc.normalColor)
        print(mc.correctColor + ("*"*100)+mc.normalColor)
        sleep(1)    
        if not (totalstatistic["History"]["Usage"] == 0):
            user_history_time = totalstatistic["History"]["Time"]/totalstatistic["History"]["Usage"]
            graphs.singlegraph("History",user_history_time/100,average_history_time/100)
            sleep(1)
        if not (totalstatistic["General Knowledge"]["Usage"] == 0):
            user_GeneralKnowledge_time = totalstatistic["General Knowledge"]["Time"]/totalstatistic["General Knowledge"]["Usage"]
            graphs.singlegraph("General Knowledge",user_GeneralKnowledge_time/100,average_GeneralKnowledge_time/100)
            sleep(1)
        if not (totalstatistic["Sport"]["Usage"] == 0):
            user_Sport_time = totalstatistic["Sport"]["Time"]/totalstatistic["Sport"]["Usage"]
            graphs.singlegraph("Sport",user_Sport_time/100,average_Sport_time/100)    
            sleep(1)
        if not (totalstatistic["Science"]["Usage"] == 0):
            user_Science_time = totalstatistic["Science"]["Time"]/totalstatistic["Science"]["Usage"]
            graphs.singlegraph("Science",user_Science_time/100,average_Science_time/100)
            sleep(1)   
        if not (totalstatistic["Art"]["Usage"] == 0):
            user_Art_time = totalstatistic["Art"]["Time"]/totalstatistic["Art"]["Usage"]
            graphs.singlegraph("Art",user_Art_time/100,average_Art_time/100)
            sleep(1)
            graphs.singlegraph("Total",(Totaltime_everycategory_user/Totalusage_everycategory_user)/100,(Totaltime_everycategory_average/Totalusage_everycategory_average)/100)
            sleep(1)
        print(mc.correctColor + ("*"*100)+mc.normalColor)
        print(mc.correctColor + ("*"*100)+mc.normalColor)
    else:
        print("Firstly, you should enter a quiz")
    
    return True    
def getranking(user,category,score):
    name = user.username
    firebase.post(f"/Quizes/{category}",{"Name":name,"Score":score})
    highscore = 0
    scoreruser = ""
    dict_ = {"vdfv":"vdfv"}
    dict_.clear
    categories = firebase.get(f"/Quizes/{category}",None).values()
    for i in categories:
        score_ = i["Score"]
        if score_ >= highscore:
            highscore = score_
            scoreruser =i["Name"]
    if highscore == score:
        return True, scoreruser, highscore
    else:
        return False, scoreruser, highscore
            