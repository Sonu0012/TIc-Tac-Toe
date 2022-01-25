import random
board = ['#',' ',' ',' ',' ',' ',' ',' ',' ',' ']
#function to  print the game board
def printBoard(board):
    print("            ")
    print(f" {board[7]} | {board[8]} | {board[9]} ")
    print("___|___|___")
    print("   |   |   ")
    print(f" {board[4]} | {board[5]} | {board[6]} ")
    print("___|___|___")
    print("   |   |   ")
    print(f" {board[1]} | {board[2]} | {board[3]} ")
    print("              ")


#defining x or o to players
def marker():
    mark = " "
    while mark not in ['x','o']:
        mark = input("Player 1 input your marker : ")
        if mark not in ['x','o']:
            print("Enter valid input ")

    if mark=='x':
        return ('x','o')
    if mark =='o':
        return ('o','x')            

#placing the marker on the board from user
def placeMarker(board,marker,position):
    board[position]=marker
    return board

#analysing if any player won vthe game
def winGame(board,mark):
    return (board[1] == mark and board[2]==mark and board[3]==mark or
    board[4] == mark and board[5]==mark and board[6]==mark or
    board[7] == mark and board[8]==mark and board[9]==mark or
    board[1] == mark and board[4]==mark and board[7]==mark or 
    board[2] == mark and board[5]==mark and board[8]==mark or
    board[3] == mark and board[6]==mark and board[9]==mark or
    board[1] == mark and board[5]==mark and board[9]==mark or
    board[7] == mark and board[5]==mark and board[3]==mark)


#turn of player
def turn():
    choice = random.randint(1,2)
    if choice==1:
        return 'Player 1'
    else:
        return 'Player 2'    

#space check function
def spaceCheck(board, posi):
    return board[posi]==" "

#board full check
def boardFull(board):
    for i in range(1,10):
        if board[i]==" ":
            return False
    return True

#players choice
def playerChoice(board):
    position=0

    while position not in [1,2,3,4,5,6,7,8,9] or not spaceCheck(board,position):
        position = int(input ("Enter your position where you want mark : "))

        if position not in [1,2,3,4,5,6,7,8,9]:
            print ("Enter a valid position") 
        else:
            if not spaceCheck(board, position):
                print("your position is aleready occupied enter valid one")

    return position  


#want to continue playing or not
def endGame():
    choice = 'o'
    while choice not in ['y','n']:
        choice = input("Enter if you wnt to play again(y,n) : ")

        if choice not in ['y','n']:
            print("enter a valid choice")

    if choice=='y':
        return True
    if choice=='n':
        return False



gameOn=True
while gameOn:
    theBoard=['#',' ',' ',' ',' ',' ',' ',' ',' ',' ']
    printBoard(theBoard)
    player1, player2 = marker()
    print(f"Player 1 is {player1}")
    print(f"Player 2 is {player2}")
    myturn = turn()
    print(f"\n\n{myturn} will go first")

    con=True
    while con:
        if myturn == 'Player 1':
            posi = playerChoice(theBoard)
            placeMarker(theBoard,player1,posi)
            printBoard(theBoard)

            if winGame(theBoard,player1):
                print("Congratulations ! Player 1 won the game")
                con = False
            else:
                if boardFull(theBoard):
                    print("Game is a draw")
                    break
                else:
                    myturn = 'Player 2'
        
        else:
            posi = playerChoice(theBoard)
            placeMarker(theBoard,player2,posi)
            printBoard(theBoard)

            if winGame(theBoard,player2):
                print("Congratulations! Player 2 You won the game")
                con = False
            else:
                if boardFull(theBoard):
                    print("Game is a draw")
                    break
                else:
                    myturn= 'Player 1'
    
    gameOn=endGame()




    





