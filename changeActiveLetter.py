
activeLetter = 'x'

board = [0,1,2,3,4,5,6,7,8,9]
def drawBoard (board):
     # "board" is a list of 10 strings representing the board (ignore index 0)
    print"   |   |"
    print"board[1]|board[2]|board[3]"
    print"   |   |"
    print"-----------"
    print"   |   |"
    print"board[4]|board[5]|board[6]"
    print"   |   |"
    print"-----------"
    print"   |   |"
    print"board[7]|board[8]|board[9]"
    print"   |   |"

def inputPlayerLetter ():
    playerLetter = input('Choose X or O:')

def playerGoes():
    playerTurn = input('Choose a number between 1 and 9')
    

def assignTurns ():
    if inputPlayerLetter() == X:
        playerGoes()
    else:
        computerMove()

def computerMove():
    import random
    number = (random.randint (1,9))
    updateBoard()
       
def changeActiveLetter (activeLetter):
    if activeLetter == 'x':
        activeLetter = 'o'
    else: activeLetter = 'x'
    return activeLetter
answer = changeActiveLetter (activeLetter)

def updateBoard():


    def checkWin():
        if [1] == 'x' and [2] == 'x'and [3] == 'x':
            Win = True
        elif [4] == 'x' and [5] == 'x' and [6] == 'x':
            Win = True
        elif [7] == 'x' and [8] == 'x' and [9] == 'x':
            Win = True
        elif [1] == 'x' and [4] == 'x' and [7] == 'x':
            Win = True
        elif [2] == 'x' and [5] == 'x' and [8] == 'x':
            Win = True
        elif [3] == 'x' and [6] == 'x' and [9] == 'x':
            Win = True
        elif [1] == 'x' and [5] == 'x' and [9] == 'x':
            Win = True
        elif [3] == 'x' and [5] == 'x' and [7] == 'x':
            Win = True
        elif [1] == 'o' and [2] == 'o' and [3] == 'o':
            Win = True
        elif [4] == 'o' and [5] == 'o' and [6] == 'o':
            Win = True
        elif [7] == 'o' and [8] == 'o' and [9] == 'o':
            Win = True
        elif [1] == 'o' and [4] == 'o' and [7] == 'o':
            Win = True
        elif [2] == 'o' and [5] == 'o' and [8] == 'o':
            Win = True
        elif [3] == 'o' and [6] == 'o' and [9] == 'o':
            Win = True
        elif [1] == 'o' and [5] == 'o' and [9] == 'o':
            Win = True
        elif [3] == 'o' and [5] == 'o' and [7] == 'o':
            Win = True
        else:
            Win = False

def playerInput():


    def playGame():
        drawBoard(board)
        inputPlayerLetter()
        assignTurns()
        checkWin()
        if playerLetter == activeLetter:
            playerGoes()
        else:
            computerGoes()
            changeActiveLetter()

gameBoard = drawBoard(board)
print gameBoard
    
