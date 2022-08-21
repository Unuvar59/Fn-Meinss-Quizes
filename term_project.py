
import mycolors as mc
import questionEditor 
import PersonalInformation
from PersonalInformation import person_sign, person_login, getranking, getpersoninfo, updateusername, updatemail,updatebornyear,updatepassword, deleteacount, userstatistic
from os import system,_exit
import time
def firstscreen():
     
    needtry = True
    while needtry:
        print(mc.subinfocolor + "\n[1] - Log in\n[2] - Sign in\n[3] - Quit" + mc.normalColor)
        print(mc.infocolor + "\nWhat do you want to do?" + mc.normalColor)        
        userchoose = input(mc.usercolor + "\t = ").lower().strip()
        try:
            userchoose = int(userchoose)
        except:
            print(mc.errorcolor + f"You should write 1 or 2\n" + mc.normalColor)
            continue
        if (userchoose == 1):
            system("cls")
            user = person_login()
            system("cls")
            needtry = False
            
            menuscreen(user)
        elif (userchoose == 2):
            system("cls")
            user = person_sign()
            system("cls")
            firstscreen()
            needtry = False
        elif (userchoose == 3):
      
            system("cls")
            print("Closing...")
            time.sleep(1)
            system("cls")
            _exit(0)
        else:
            print(mc.errorcolor + f"You should write 1 or 2\n" + mc.normalColor)
            
def menuscreen(user):
    
   
    fail = True
    while fail:
        print(mc.subinfocolor + "\n[1] - Quizes\n[2] - Profil\n[3] - User statistic\n[4] - Log out" + mc.normalColor)
        print(mc.infocolor + "\nWhat do you want to do?" + mc.normalColor)
        userchoice = (input(mc.usercolor + "\t = ").strip())
        try:
            userchoice = int(userchoice)
        except:
            print(mc.errorcolor + f"You should write 1, 2, 3 or 4\n" + mc.normalColor)
            continue
        match userchoice:
            case 1:
                fail = True  
                system("cls")        
                quizes(user)
              

            case 2:
                fail = False
                system("cls")
                profil(user)
            case 3:
                fail = False
                PersonalInformation.getuserstatistic(user)
                time.sleep(2)
                fail = True
            case 4:
                system("cls")
                firstscreen()
            case default:
                print(mc.errorcolor + f"You should write 1, 2, 3 or 4\n" + mc.normalColor)
                fail = True

def profil(user):
    
    system("cls")
    key = getpersoninfo(user)

    print(mc.subinfocolor + "\n[1] - Edit Username\n[2] - Edit Mail\n[3] - Edit Born Year\n[4] - Edit Password\n[5] - Delete Account" + mc.normalColor)
    print(mc.infocolor + "\nWhat do you want to do?" + mc.normalColor)
    userchoice = int(input(mc.usercolor + "\t = ").strip())
    fail = True
    while fail:
        match userchoice:
            case 1:
                fail = False               
                updateusername(key)
            case 2:
                fail = False               
                updatemail(key)
            case 3:
                fail = False               
                updatebornyear(key)
            case 4:
                fail = False               
                updatepassword(key)
            case 5:
                fail = False
                deleteacount(key)
            case default:
                fail = True
                print(mc.errorcolor + f"You should write 1,2,3 or 4\n" + mc.normalColor)

def quizes(user):
    
    choice_checker = True
    while choice_checker:
        print(mc.subinfocolor + "\n[1] - Sport\n[2] - Science\n[3] - General Knowledge\n[4] - History\n[5] - Art\n[6] - Undo <--  " + mc.normalColor)
        print(mc.infocolor + "\nWhat do you want to do?" + mc.normalColor)
        try:
            userchoice = int(input(mc.usercolor + "\t = ").strip())
        except:
            print(mc.errorcolor + f"You should write 1, 2, 3, 4, 5, 6 or 7\n" + mc.normalColor)
            continue
        match userchoice:
            case 1:
                system("cls")
                choice_checker = False               
                category = "Sport"
            case 2:
                system("cls")
                choice_checker = False               
                category = "Science"
            case 3:
                system("cls")
                choice_checker = False               
                category = "General Knowledge"
            case 4:
                system("cls")
                choice_checker = False               
                category = "History"
            case 5:
                system("cls")
                choice_checker = False
                category = "Art"
            case 6:
                system("cls")
                choice_checker = False
                menuscreen(user)
            case default:
                choice_checker = True
                print(mc.errorcolor + f"You should write 1, 2, 3, 4, 5, 6 or 7\n" + mc.normalColor)

    system("cls")
    Total_score=0
    question_list, answer_list, other_list,key_list = questionEditor.getquestionFunction(category,5) #get a question, printing this question and return answer and choices
    for i in range(len(question_list)):
        start_time=time.time()
        system("cls")
        print(mc.questionbackcolor + ((len(question_list[i])+7)*"-" + mc.normalColor))
        print(mc.questionbackcolor + " " + mc.questioncolor + f" Q: {question_list[i]} " + mc.questionbackcolor + " " + mc.normalColor)
        print(mc.questionbackcolor + ((len(question_list[i])+7)*"-" + mc.normalColor))
        for key in other_list[i]:
            print (mc.answercolor+f"{key}: {other_list[i][key]}"+ mc.normalColor)
        everythinkOK = False
        while not everythinkOK:
            print(mc.infocolor + "\nWhat is your answer?" + mc.normalColor)
            userchoose = input(mc.usercolor + "\t = ").upper().strip()
            print(mc.normalColor)
            everythinkOK,correct =  questionEditor.answerChecker(userchoose,answer_list[i],other_list[i])
            elapsedtime = (time.time()-start_time)
        score = 0
        if correct:
            if elapsedtime > 1:
                score = 100/elapsedtime
            else:
                score = 100
            print(mc.correctColor + f"Congratulations, you know right!" + mc.normalColor)
            print(mc.correctColor + f"You spent {elapsedtime:0.2f} second for this question" + mc.normalColor)
            print(mc.correctColor + f"You earned {score:0.2f} points" + mc.normalColor)
        else:
            print(mc.wrongColor + f"Maybe later, you should study harder!\n" + mc.normalColor)
            print(mc.wrongColor + f"You earned {elapsedtime:0.2f} second for this question" + mc.normalColor)
        Total_score += score
        print(mc.subinfocolor + f"You total score is {Total_score:0.2f} points" + mc.normalColor)
        userstatistic(user,elapsedtime,correct,category)
        print(mc.infocolor + "\nRate the question (0-5)" + mc.normalColor)
        rate_checker = True
        while rate_checker:
            userrate = (input(mc.usercolor + "\t = ").upper().strip())
            try:
                userrate = int(userrate)
            except:
                print(mc.errorcolor + f"You should write a integer\n" + mc.normalColor)
                continue
            else: 
                questionEditor.questionpoint(key_list[i],category,userrate,correct)
                rate_checker = False
        print(mc.infocolor + "\nPlease enter for Contuine" + mc.normalColor)
        userchoose = input(mc.usercolor + "\t = ").upper().strip()
    Total_score_str = f"You total score is {Total_score:0.2f} points"
    print(mc.correctColor +("-"*(len(Total_score_str)+2))+ mc.normalColor)
    print(mc.correctColor +"|" + Total_score_str + "|"+ mc.normalColor)
    print(mc.correctColor +("-"*(len(Total_score_str)+2))+ mc.normalColor)

    isyou, name, score = getranking(user,category,Total_score)
    if isyou:
        print(mc.correctColor +f"\n\nCongratulations! You are the new leader of the {category} category!"+ mc.normalColor)
    else:
        print(mc.wrongColor +"\n\nUnfortunately you couldn't pass the high score, keep working."+ mc.normalColor)
        print(mc.wrongColor + f"Leader of the {category} category: \nUsername: {name} \nScore: {score:0.2f}" + mc.normalColor)
    time.sleep(2)
firstscreen() #login-sign screen

# # questionEditor.setquestionFunction("Nasılsın?","harika","sdssddsff","dsvsdsdfdv","sdvdfvfdqq")
# answer, choices = questionEditor.getquestionFunction() #get a question, printing this question and return answer and choices



# TODO: kullanıcı istatistikleri+
# TODO: soru istatistikleri+
# TODO: Modlar+
# TODO: Modlara Göre sıralamalar+