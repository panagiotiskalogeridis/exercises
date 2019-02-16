import random


print "The game of tic tac toe."
board=[" "]*10
vacantblocks=9


def createboard(board):
    print'   |   |'
    print' ' + board[7] + ' | ' + board[8] + ' | ' + board[9]
    print'   |   |'
    print'-----------'
    print'   |   |'
    print' ' + board[4] + ' | ' + board[5] + ' | ' + board[6]
    print'   |   |'
    print'-----------'
    print'   |   |'
    print' ' + board[1] + ' | ' + board[2] + ' | ' + board[3]
    print'   |   |'
    print "\n"

def marks():
    mark=''
    while not (mark=='X' or mark=='O'):
        print('Do you want to be X or O?')
        mark= input().upper()
    if mark=='X':
        return ['X', 'O']
    else: return ['O', 'X']


def firstturn():
    a=random.randint(1,2)
    if a==1:
        return "user"
    else: return "computer"


def winner(board):
    if (board[1]==board[2]==board[3]=="X")or(board[1]==board[2]==board[3]=="O"):
        return 1
    elif (board[4]==board[5]==board[6]=="X")or(board[4]==board[5]==board[6]=="O"):
        return 1
    elif (board[7]==board[8]==board[9]=="X")or(board[7]==board[8]==board[9]=="O"):
        return 1
    elif (board[7]==board[4]==board[1]=="X")or(board[7]==board[4]==board[1]=="O"):
        return 1
    elif (board[8]==board[5]==board[2]=="X")or(board[8]==board[5]==board[2]=="O"):
        return 1
    elif (board[3]==board[6]==board[9]=="X")or(board[3]==board[6]==board[9]=="O"):
        return 1
    elif (board[7]==board[5]==board[3]=="X")or(board[7]==board[5]==board[3]=="O"):
        return 1
    elif (board[1]==board[5]==board[9]=="X")or(board[1]==board[5]==board[9]=="O"):
        return 1
    else: return 0


def userplay(board):
    moveon=False
    while moveon==False:
        print "Give a number between 1 and 9 to mark the block you want"
        marked=input()
        if board[marked]==" ":
            moveon=True
            board[marked]=mark[0]
            return board
        else: moveon=False


def computerplay(board):
    moveon=False
    while moveon==False:
        cc=random.randint(1,9)
        if board[cc]==" ":
            moveon=True
            board[cc]=mark[1]
            return board
        else: moveon=False


createboard(board)
mark=marks()
turn=firstturn()


while vacantblocks>0:
    if turn=="user":
        turn="computer"
        userplay(board)
        createboard(board)
    else:
        turn="user"
        computerplay(board)
        createboard(board)
    if winner(board)==1:
        vacantblocks=0
    else:
        vacantblocks=vacantblocks-1


if winner(board)==0:
    print "It's a draw"
else:
    if turn=="user":
        print "Computer wins"
    else:
        print "You win!"
