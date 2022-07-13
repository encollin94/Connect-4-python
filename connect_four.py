#code  from July 10, 2022 https://www.youtube.com/watch?v=UYgyRArKDEs, July 13, 2022 https://www.youtube.com/watch?v=zD-Xuu_Jpe4, July 13, 2022 https://www.youtube.com/watch?v=SDz3P_Ctm7U
#helps create matrixes
import numpy as np
import pygame
import sys

BLUE=(5,5,110)
CIRCLE=(0,0,20)

#number of rows in board/ permanent so all caps variable(code etiqeutte)
ROW_COUNT = 6

#number of columns in board/ permanent so all caps variable(code etiqeutte)
COLUMN_COUNT = 7

#create matrix of zeros by (row,clumn)
def create_board():
    board=np.zeros((ROW_COUNT,COLUMN_COUNT))
    return board

#defines a variable that will place a piece in the matrix
def drop_piece(board, row, col, piece):
    board[row][col] = piece

#defines a variable that will see if top row has been filled
def is_valid_location(board, col):
    return board[ROW_COUNT-1][col]==0

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
#define winng move, function to determine if someone has won
def winning_move(board,piece):
    #Check horizontal locations for a win
    for c in range(COLUMN_COUNT-3):
        for r in range(ROW_COUNT):
            if board[r][c] == piece and board[r][c+1] == piece and board[r][c+2] == piece and board[r][c+3] == piece and board[r][c]:
                    return True
    #Check for vertical win
    for c in range(COLUMN_COUNT):
        for r in range(ROW_COUNT-3):
            if board[r][c] == piece and board[r+1][c] == piece and board[r+2][c] == piece and board[r+3][c] == piece and board[r][c]:
                    return True
    #Check for postively sloped diagonals
    for c in range(COLUMN_COUNT-3):
        for r in range(ROW_COUNT-3):
            if board[r][c] == piece and board[r+1][c+1] == piece and board[r+2][c+2] == piece and board[r+3][c+3] == piece and board[r][c]:
                    return True
    #Check for negatively sloped diagonals
    for c in range(COLUMN_COUNT-3):
        for r in range(3,ROW_COUNT):1
    
        if board[r][c] == piece and board[r-1][c+1] == piece and board[r-2][c+2] == piece and board[r-3][c+3] == piece and board[r][c]:
                    return True

#defina  functions that will make the board game graphics
def draw_board(board):
    for c in range(COLUMN_COUNT):
        for r in range(ROW_COUNT):
            pygame.draw.rect(screen,BLUE,(c*SQUARESIZE, r*SQUARESIZE+SQUARESIZE,SQUARESIZE, SQUARESIZE))
            pygame.draw.circle(screen,CIRCLE,(int(c*SQUARESIZE+SQUARESIZE/2), int(r*SQUARESIZE+SQUARESIZE+SQUARESIZE/2)), RADIUS)

#assign the all of create_board to variable board
board = create_board()
#prints board in the defined correct orientation
print_board(board)

#intialize variable that tell when game is over. game is not over until variable is converted to true
game_over= False
#create a variable that will decide what players turn it is
turn = 0

#initiate pygame, event based game library, reads how you move mouse and key strokes as individual events
pygame.init()
#create how big you want board, measurement all in pixels
SQUARESIZE = 100
width = COLUMN_COUNT*SQUARESIZE
height= (ROW_COUNT+1)*SQUARESIZE

size =(width,height)

RADIUS= int(SQUARESIZE/2-5)

screen = pygame.display.set_mode(size)
draw_board(board)
pygame.display.update()

#start game  and loop through until game_over is True
while not game_over:
    #establish the events that pygame will read in the game
    for event in pygame.event.get():
        #allows player to exit out of game by clicking the close button in top right corner/should establish a quit in all games
        if event.type == pygame.QUIT:
            sys.exit()
        #creates an event type for when you click mouse, all of game is using this funtion so put all of game functionality under mouse button down 
        if event.type == pygame.MOUSEBUTTONDOWN: 
            continue
        

            #Ask for Player 1 Input
            if turn == 0:
                col = int(input("Player 1 Make your Selection (0-6)"))
                #uses player in put to see if the input is valid
                if is_valid_location(board,col):
                    #if valid then we will retrieve the next available row that is still a 0
                    row = get_next_open_row(board,col)
                    #in the row and column we will drop player 1 piece which is a 1
                    drop_piece(board, row, col, 1)

                    #defines if player win1 and stopes game
                    if winning_move(board, 1):
                        print("PLAYER 1 Wins! Congrats!")
                        game_over = True

             #Ask for Player 2 input
            else:
                col = int(input("Player 2 Make your selection (0-6)"))
                #uses player in put to see if the input is valid
                if is_valid_location(board,col):
                    #if valid then we will retrieve the next available row that is still a 0
                    row = get_next_open_row(board,col)
                    #in the row and column we will drop player 2 piece which is a 2
                    drop_piece(board, row, col, 2)
                     #defines if player 2 win and stops game
                    if winning_move(board, 2):
                        print("PLAYER 2 Wins! Congrats!")
                        game_over = True

            #prints board in the defined correct orientation
            print_board(board)        
            #increase turn by 1
            turn += 1
            #makes turn either 0 or 1 so that it will easily flip between Player 1 and Player 2
            turn = turn%2

