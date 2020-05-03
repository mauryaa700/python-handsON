import random
def drowBoard(board):
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')
    print('------------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('------------')
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')
#drowBoard([' ', ' ', ' ', ' ', 'X', 'O', ' ', 'X', ' ', 'O'])
# select the player letter be 'X' or "O" 
def inputPlayerLetter():
    letter=''
    while not(letter=='X' or letter=='O'):
        print("which letter u want to sellect")
        letter=input().upper()
# the first letter is player and sec is for computer
    if letter=='X':
        return['X','O']   
    else:
        return['O','X']   
def whoGoesFirst():
    if random.randint(0, 1) == 0:
        return 'computer'
    else:
        return 'player'     
def playAgain():
    print("Do u want to play again? (yes or no")
    return input().lower().startswith(y)

def makeMove(board,letter,move):
    board[move]=letter

def isWinner(bo,le):
    return((bo[7]==le and bo[8]==le and bo[9]==le) or # across the top
    (bo[4]==le and bo[5]==le and bo[6]==le) or        # across the middel
    (bo[1]==le and bo[2]==le and bo[3]==le) or         # accroess the bot
    (bo[7]==le and bo[4]==le and bo[1]==le) or         # down the left side 
    (bo[8]==le and bo[5]==le and bo[2]==le) or          # down the middle side 
    (bo[9]==le and bo[6]==le and bo[3]==le) or          # down the bot side
    (bo[7]==le and bo[5]==le and bo[3]==le) or           #diagnalleft to right
    (bo[9]==le and bo[5]==le and bo[1]==le))              # diag rt to lft

def getBoardCopy(board):
    dupeBoard=[]
    for i in board:
        dupeBoard.append(i)
    return dupeBoard

def isSpaceFree(board,move):
    return board[move]==' '

def getPlayerMove(board):
    move=' '
    while move not in ' 1 2 3 4 5 6 7 8 9'.split() or not isSpaceFree(board,int(move)):
        print("what is ur next move? (1-9)")    
        move=input()
        return int(move)       
def chooseRandomMoveFromList(board,movesList):
 # Returns a valid move from the passed list on the passed board.
 # Returns None if there is no valid move
    possibleMoves=[]  
    for i in movesList:
        if isSpaceFree(board, i):
            possibleMoves.append(i)  

    if len(possibleMoves)!=0:
        return random.choice(possibleMoves)
    else:
        return None

def getComputerMove(board, computerLetter):
    # Given a board and the computer's letter, determine where to move and return that move.
    if computerLetter=='X':
        playerLetter='O'
    else:
        playerLetter='X'    

        # Here is our algorithm for our Tic Tac Toe 
        #  # First, check if we can win in the next move
    for i in range(1, 10):
        copy = getBoardCopy(board)
        if isSpaceFree(copy, i):
            makeMove(copy, computerLetter, i)
            if isWinner(copy, computerLetter):
                return i 

# Check if the player could win on their next move, and block them.
    for i in range(1, 10):
        copy = getBoardCopy(board)
        if isSpaceFree(copy, i):
            makeMove(copy, playerLetter, i)
            if isWinner(copy, playerLetter):
                return i             


    # Try to take one of the corners, if they are free.
    move = chooseRandomMoveFromList(board, [1, 3, 7, 9])
    if move != None:
        return move
# Try to take the center, if it is free.
    if isSpaceFree(board,5):
        return 5
    # Move on one of the sides
    return chooseRandomMoveFromList(board, [2, 4, 6, 8])     

def isBoardFull(board):
    # Return True if every space on the board has been taken. Otherwise return False.
    for i in range(1, 10):
        if isSpaceFree(board, i):
            return False

    return True 

print('Welcome to tic tac toe')

while True:
    #reset the board
    theBoard=[' '] * 10
    playerLetter , computerLetter = inputPlayerLetter()
    turn=whoGoesFirst()
    print('the' + turn + 'will go first')
    gameIsPlaying =True

    while gameIsPlaying:
        if turn== "player":
            drowBoard(theBoard)
            move= getPlayerMove(theBoard)
            makeMove(theBoard, playerLetter, move)

            if isWinner(theBoard, playerLetter):
                drowBoard(theBoard)
                print('u have won the game!')
                gameIsPlaying=False
            else:
                if isBoardFull(theBoard):
                    drowBoard(theBoard)
                    print("the game is tie")
                    break
                else:
                    turn ="computer"    

        else:
            move = getComputerMove(theBoard, computerLetter)

            makeMove(theBoard, computerLetter, move)

            if isWinner(theBoard, computerLetter):

                drawBoard(theBoard)

                print('The computer has beaten you! You lose.')

                gameIsPlaying = False

            else:
                if isBoardFull(theBoard):
                    drowBoard(theBoard)
                    print("game is tie")
                    break
                else:
                    turn = 'player'

    if not playAgain():
        break                