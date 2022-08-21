import mycolors as mc

def singlegraph(title,value,averagevalue):
    value *= 100
    averagevalue *= 100
    print(mc.normalColor + "-"*100)
    print(mc.infocolor + title + mc.normalColor)
    print(mc.correctColor + "Your   : " + mc.bluebackColor + (" "*int(value)) + mc.correctColor + f" {value:0.2f}"+mc.normalColor )
    print(mc.wrongColor + "Average: " + mc.purplebackColor + (" "*int(averagevalue))+ mc.wrongColor +f" {averagevalue:0.2f}" +mc.normalColor)
    print("-"*100)
# singlegraph("Furkan",3.3,4.5)