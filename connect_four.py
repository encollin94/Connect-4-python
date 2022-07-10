#helps create matrixes
import numpy as np

#number of rows in board/ permanent so all caps variable
ROW_COUNT = 6

#number of columns in board/ permanent so all caps variable
COLUMN_COUNT = 7

#create matrix of zeros by (row,clumn)
def create_board():
    board=np.zeros((6,7))
    return board

#defines a variable that will place a piece in the matrix
def drop_piece(board, row, col, piece):
    board[row][col] = piece

#defines a variable that will see if top row has been filled
def is_valid_location(board, col):
    return board[5][col]==0

#checks to see which row in matrix is the next open row
def get_next_open_row(board,col):
    #r will count from 0 to ROW_COUNT-1
    for r in range(ROW_COUNT):
        #check if position on board is a zero
        if board[r][col] == 0:
            #will return first instance of a row that is 0 from 0 to ROW_COUNT-1
            return r
#need to flip board so our(0,0) in the matrix starts at bottom right as opposed to top right
def print_board(board):
    print(np.flip(board,0))

#assign the all of create_board to variable board
board = create_board()
#prints board in the defined correct orientation
print_board(board)

#intialize variable that tell when game is over. game is not over until variable is converted to true
game_over= False
#create a variable that will decide what players turn it is
turn = 0

#start game  and loop through until game_over is True
while not game_over:
    #Ask for Player 1 Input
    if turn == 0:
        col = int(input("Player 1 Make your Selection (0-6)"))
        #uses player in put to see if the input is valid
        if is_valid_location(board,col):
            #if valid then we will retrieve the next available row that is still a 0
            row = get_next_open_row(board,col)
            #in the row and column we will drop player 1 piece which is a 1
            drop_piece(board, row, col, 1)

    #Ask for Player 2 input
    else:
        col = int(input("Player 2 Make your selection (0-6)"))
        #uses player in put to see if the input is valid
        if is_valid_location(board,col):
            #if valid then we will retrieve the next available row that is still a 0
            row = get_next_open_row(board,col)
            #in the row and column we will drop player 2 piece which is a 2
            drop_piece(board, row, col, 2)

    #prints board in the defined correct orientation
    print_board(board)        
    #increase turn by 1
    turn += 1
    #makes turn either 0 or 1 so that it will easily flip between Player 1 and Player 2
    turn = turn%2

