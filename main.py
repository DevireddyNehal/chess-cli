def game(board,movenumber):
    while True:
        Notation=notationToCoordinates()
        if isLegal(board, Notation,movenumber):
            board[Notation[1][0]][Notation[1][1]]=board[Notation[0][0]][Notation[0][1]]
            board[Notation[0][0]][Notation[0][1]]="."
            displayBoard(board)
            movenumber+=1
        else: 
            print("Illegal Move")
def Move():
    initial=input("Enter your move:-\nInitial: ")
    final=input("Final: ")
    return (initial,final)
def createBoard():
    row1=["r", "n", "b", "q", "k", "b", "n", "r"]
    row2=["p", "p", "p", "p", "p", "p", "p", "p"]
    row3=[".", ".", ".", ".", ".", ".", ".", "."]
    row4=[".", ".", ".", ".", ".", ".", ".", "."]
    row5=[".", ".", ".", ".", ".", ".", ".", "."]
    row6=[".", ".", ".", ".", ".", ".", ".", "."]
    row7=["P", "P", "P", "P", "P", "P", "P", "P"]
    row8=["R", "N", "B", "Q", "K", "B", "N", "R"]
    return [row1,row2,row3,row4,row5,row6,row7,row8]
def notationToCoordinates():
    move=Move()
    files="abcdefgh"
    ranks="12345678"
    fileInitial=-1
    rankIntial=-1
    if move[0][0] in files:
        fileInitial=files.index(move[0][0])
    else: print("Wrong Notation")
    if move[0][1] in ranks:
        rankIntial=7-ranks.index(move[0][1])
    else: print("Wrong Notation")
    rankFinal=-1
    fileFinal=-1
    if move[1][0] in files:
        fileFinal=files.index(move[1][0])
    else: print("Wrong Notation")
    if move[1][1] in ranks:
        rankFinal=7-ranks.index(move[1][1])
    else: print("Wrong Notation")
    return [[rankIntial,fileInitial],[rankFinal,fileFinal]]
def isSameColour(board,Notation):
    if board[Notation[0][0]][Notation[0][1]].isupper() and board[Notation[1][0]][Notation[1][1]].isupper():
        return True
    elif board[Notation[0][0]][Notation[0][1]].islower() and board[Notation[1][0]][Notation[1][1]].islower():
        return True
    else: return False
def displayBoard(board):
    for i in range(0,8):
        print(8-i, end=" ")
        for j in range(0,8):
            if board[i][j].isupper():
                if board[i][j] == "P": print("♟", end=" ")
                elif board[i][j] == "R": print("♜", end=" ")
                elif board[i][j] == "N": print("♞", end=" ")
                elif board[i][j] == "B": print("♝", end=" ")
                elif board[i][j] == "Q": print("♛", end=" ")
                elif board[i][j] == "K": print("♚", end=" ")
            else: 
                if board[i][j] == ".": print(".", end=" ")
                elif board[i][j] == "p": print("♙", end=" ")
                elif board[i][j] == "r": print("♖", end=" ")
                elif board[i][j] == "n": print("♘", end=" ")
                elif board[i][j] == "b": print("♗", end=" ")
                elif board[i][j] == "q": print("♕", end=" ")
                elif board[i][j] == "k": print("♔", end=" ")
        print()
    print("", " a", "b", "c", "d", "e", "f", "g", "h")
def isLegal(board, Notation,movenumber):
    if not isEmpty(board,Notation):
        if not isSameColour(board,Notation):
            if isPieceLegal(board,Notation):
                if whoseMove(board,Notation,movenumber):
                    return True
                return False
        else: return False
    else: return False
def whoseMove(board,Notation,movenumber):
    if board[Notation[0][0]][Notation[0][1]].isupper() and (not movenumber%2==0):
        return True
    elif board[Notation[0][0]][Notation[0][1]].islower() and movenumber%2==0:
        return True
    else: return False
def isEmpty(board,Notation):
    if board[Notation[0][0]][Notation[0][1]] == ".":
        return True
    else: return False
def isPieceLegal(board,Notation):
    rankDiff=Notation[0][0]-Notation[1][0]
    fileDiff=Notation[1][1]-Notation[0][1]
    match board[Notation[0][0]][Notation[0][1]]:
        case "P": 
                if (not board[Notation[1][0]][Notation[1][1]]==".") and (abs(rankDiff)==abs(fileDiff)):
                    return True
                elif board[Notation[1][0]][Notation[1][1]]=="." and (abs(rankDiff)==abs(fileDiff)):
                    return False
                elif (board[Notation[1][0]][Notation[1][1]]==".") and rankDiff==1 and fileDiff==0:
                    return True
                elif Notation[0][0] == 6 and rankDiff==2 and fileDiff == 0 and (board[(Notation[1][0]+Notation[0][0])//2][Notation[1][1]]=="."):
                    return True
                else: print("c")
        case "p": 
                if (not board[Notation[1][0]][Notation[1][1]]==".") and (abs(rankDiff)==abs(fileDiff)):
                    return True
                elif board[Notation[1][0]][Notation[1][1]]=="." and (abs(rankDiff)==abs(fileDiff)):
                    return False
                elif (board[Notation[1][0]][Notation[1][1]]==".") and -(rankDiff)==1 and -(fileDiff)==0:
                    return True
                elif Notation[0][0] == 1 and -(rankDiff)==2 and -(fileDiff) == 0 and (board[(Notation[1][0]+Notation[0][0])//2][Notation[1][1]]=="."):
                    return True
                else: print("c")

board=createBoard()      
displayBoard(board) 
movenumber=1
game(board,movenumber)