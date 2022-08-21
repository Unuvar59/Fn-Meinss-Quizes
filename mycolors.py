import os
os.system("")  #if we dont use os, print colors cannot working

############## Color Cods ####################
answercolor = "\033[0;36;40m"
subinfocolor = answercolor
errorcolor = "\033[1;40;41m"
questioncolor = "\033[1;34;40m"
questionbackcolor = "\033[1;30;44m"
infocolor = "\033[1;33;40m"
usercolor = "\033[1;36;40m"
normalColor = '\033[0m'
correctColor = "\033[1;32;40m"
wrongColor = "\033[1;31;40m"
bluebackColor = "\033[1;37;44m"
purplebackColor = "\033[1;37;45m"
##############################################

def colortest():
    print(answercolor + "Hello World" + normalColor)
    print(errorcolor + "Hello World" + normalColor)
    print(questioncolor + "Hello World" + normalColor)
    print(questionbackcolor + "Hello World" + normalColor)
    print(infocolor + "Hello World" + normalColor)
    print(usercolor + "Hello World" + normalColor)
    print(normalColor + "Hello World" + normalColor)
    input()
# colortest()