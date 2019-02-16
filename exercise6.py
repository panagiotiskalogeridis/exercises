import random

def board(a,b,mines):
    p=b*"0"
    g=""
    for i in range(0,a):
        g=g+(p+'\n')
    g=getmines(g,mines)
    print g

def getmines(g,mines):
    new_list=(list(g))
    ties=len(new_list)
    newg=""
    for i in range(0,mines):
        pos=random.randint(0,ties-1)
        while new_list[pos]=="\n":
                pos=random.randint(0,ties-1)
        new_list[pos]="X"
    for i in range (0,ties-1):
        newg=newg+new_list[i]
    g=newg
    return g




print "This algorythm creates the board of the game minesweper.\nGive values greater than zero and create your own board!"

height=input("give the board's height:" )
if height==0:
    while height==0:
        height=input("please give value greater than zero")

length=input("give the board's length:" )
if length==0:
    while length==0:
        length=input("please give value greater than zero")

mines=input("give the number of mines:" )
if mines==0:
    while mines==0:
        mines=input("please give value greater than zero")

board(height,length,mines)
