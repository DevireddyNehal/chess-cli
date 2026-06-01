def game(board,movenumber):
    while True:
        Notation=notationToCoordinates()

        while Notation==None:
            print("Illegal Move")
            Notation=notationToCoordinates()
        if Notation==-1:
            print("Game Over, you resigned!")
            break

        rankDiff=Notation[0][0]-Notation[1][0]
        fileDiff=Notation[1][1]-Notation[0][1]

        if isLegal(board, Notation,movenumber,rankDiff,fileDiff):
            board[Notation[1][0]][Notation[1][1]]=board[Notation[0][0]][Notation[0][1]]
            board[Notation[0][0]][Notation[0][1]]="."
            displayBoard(board)
            movenumber+=1
        else:
            print("Illegal Move")
        whiteKingAlive=any("K" in row for row in board)
        blackKingAlive=any("k" in row for row in board)
        if not whiteKingAlive or not blackKingAlive:
            print("Game Over!")
            break

def Move():
    initial=input("Enter your move (r for resign):-\nInitial: ")
    if initial=="r":
        return -1
    final=input("Final: ")
    if len(initial)!=2 or len(final)!=2:
        return None
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
    while move==None:
        print("Wrong Notation/Format")
        move=Move()
    if move==-1:
        return -1
    files="abcdefgh"
    ranks="12345678"

    fileInitial=-1
    rankIntial=-1
    rankFinal=-1
    fileFinal=-1

    if move[0][0] in files:
        fileInitial=files.index(move[0][0])

    if move[0][1] in ranks:
        rankIntial=7-ranks.index(move[0][1])

    if move[1][0] in files:
        fileFinal=files.index(move[1][0])

    if move[1][1] in ranks:
        rankFinal=7-ranks.index(move[1][1])
    
    if not (rankIntial==-1 or rankFinal==-1 or fileInitial==-1 or fileFinal==-1):
        return [[rankIntial,fileInitial],[rankFinal,fileFinal]]
    else:
        return None

def isSameColour(board,Notation):
    if board[Notation[0][0]][Notation[0][1]].isupper() and board[Notation[1][0]][Notation[1][1]].isupper():
        return True
    elif board[Notation[0][0]][Notation[0][1]].islower() and board[Notation[1][0]][Notation[1][1]].islower():
        return True
    else:
        return False

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

def isLegal(board, Notation,movenumber,rankDiff,fileDiff):
    if not isEmpty(board,Notation):
        if not isSameColour(board,Notation):
            if isPieceLegal(board,Notation,rankDiff,fileDiff):
                if whoseMove(board,Notation,movenumber):
                    return True
                return False
            return False
        return False
    return False

def whoseMove(board,Notation,movenumber):
    if board[Notation[0][0]][Notation[0][1]].isupper() and (not movenumber%2==0):
        return True
    elif board[Notation[0][0]][Notation[0][1]].islower() and movenumber%2==0:
        return True
    else:
        return False

def isEmpty(board,Notation):
    if board[Notation[0][0]][Notation[0][1]] == ".":
        return True
    else:
        return False

def isPathBlocked(board,Notation):
    rankFirst = Notation[0][0]
    fileFirst = Notation[0][1]
    rankLast = Notation[1][0]
    fileLast = Notation[1][1]

    rankCurrent=rankFirst
    fileCurrent=fileFirst

    if rankLast>rankFirst:
        rankStep=1
    elif rankLast<rankFirst:
        rankStep=-1
    else:
        rankStep=0

    if fileLast>fileFirst:
        fileStep=1
    elif fileLast<fileFirst:
        fileStep=-1
    else:
        fileStep=0

    while rankCurrent!=rankLast-rankStep or fileCurrent!=fileLast-fileStep:
        rankCurrent+=rankStep
        fileCurrent+=fileStep

        if board[rankCurrent][fileCurrent]!=".":
            return True

    return False

def isPieceLegal(board,Notation,rankDiff,fileDiff):
    isRookMove=(rankDiff==0 or fileDiff==0)
    isBishopMove=(abs(rankDiff)==abs(fileDiff))
    match board[Notation[0][0]][Notation[0][1]]:

        case "P":
            if (not board[Notation[1][0]][Notation[1][1]]==".") and abs(fileDiff)==1 and rankDiff==1:
                return True

            elif (board[Notation[1][0]][Notation[1][1]]==".") and rankDiff==1 and fileDiff==0:
                return True

            elif Notation[0][0] == 6 and (board[Notation[1][0]][Notation[1][1]]==".") and rankDiff==2 and fileDiff == 0 and (board[(Notation[1][0]+Notation[0][0])//2][Notation[1][1]]=="."):
                return True

            else:
                return False

        case "p":
            if (not board[Notation[1][0]][Notation[1][1]]==".") and abs(fileDiff)==1 and rankDiff==-1:
                return True

            elif (board[Notation[1][0]][Notation[1][1]]==".") and rankDiff==-1 and fileDiff==0:
                return True

            elif Notation[0][0] == 1 and (board[Notation[1][0]][Notation[1][1]]==".") and rankDiff==-2 and fileDiff == 0 and (board[(Notation[1][0]+Notation[0][0])//2][Notation[1][1]]=="."):
                return True

            else:
                return False
        
        case "N"|"n":
            if (abs(rankDiff),abs(fileDiff))==(1,2):
                return True
            elif (abs(rankDiff),abs(fileDiff))==(2,1):
                return True
            else:
                return False
        
        case "R"|"r":
            if isRookMove and (not isPathBlocked(board,Notation)):
                return True
            else:
                return False
        case "B"|"b":
            if isBishopMove and (not isPathBlocked(board,Notation)):
                return True
            else:
                return False
        case "Q"|"q":
            if (isRookMove or isBishopMove) and (not isPathBlocked(board,Notation)):
                return True
            else:
                return False
        case "K"|"k":
            if abs(rankDiff)<=1 and abs(fileDiff)<=1:
                return True
            else:
                return False

board=createBoard()
displayBoard(board)
movenumber=1
game(board,movenumber)