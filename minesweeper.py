import random
import sys
import os

def generate_board(gridsize):
    board = [[0] * gridsize for _ in range(gridsize)]
    return board

def place_mines(board, minesnum, row, column):
    # Initialized
    mine_positions = []
    gridsize = len(board)
    positions = [(i, j) for i in range(1, gridsize + 1) for j in range(1, gridsize + 1)]
    
    # Remove the first click position
    positions.remove((column, row))  
    
    # Random Select the mine position
    mine_positions = random.sample(positions, minesnum)
    
    # Record in board
    for position in mine_positions:
        x, y = position
        board[y-1][x-1] = -1

    return mine_positions

def print_board(board):
    for row in board:
        for cell in row:
            if cell != -1:
                print(" ", end="")
            print(cell, end=" ")
        print()
        
def check(board, row, column):
    if board[column - 1][row - 1] == -1:
        return False
    return True

def error(num, gridsize):
    if num == 0:
        print("Invalid input: The number of mines and grid size should be positive integers.")
    elif num == 1:
        print("Invalid input: The number of mines should be less than the grid size.")
    elif num == 2:
        print("Invalid input. Please make sure the input is in the format (int, int).")
    elif num == 3:
        print("Invalid input range. Please make sure the ranges of row and column are from 1 to", gridsize, ".")
    elif num == 4:
        print("Invalid input. Please enter the integer set (row, column) to make a click.")
    elif num == 5:
        print("Successfully exit the game.")
    elif num == 6:
        print("The gridsize or number of mines are invalid.")
    elif num == 7:
        print("The number of mines should be less than the grid size.")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Input Error: python3 minesweeper.py [number of mines] [grid size]")
        sys.exit(1)
    minesnum = int(sys.argv[1])
    gridsize = int(sys.argv[2])
    if gridsize < 0 or minesnum < 0:
        error(6, gridsize)
        sys.exit(1)
    elif minesnum >= gridsize * gridsize:
        error(7, gridsize)
        sys.exit(1)
    
    # Generate board by gridsize
    board = generate_board(gridsize)
    print("------------------------------------\n")
    print("Welcome to Minesweeper!\n")
    print("Remember that:Top left corner is (1,1) and bottom right corner is (", gridsize, ",", gridsize, ")\n")
    print("the number on the board represents different meanings: '-1' means mine, '0' means not revealed yet.\n")
    print("Enter coordinates (row, column) to make a click which row and column is integers.\n")
    print("Enter 'q' to leave the game\n")
    print("------------------------------------")
    
    while True:
        first_click = input("Enter coordinates (row, column) as the first click: ")
        if not first_click:
            error(2, gridsize)
            continue
        elif first_click == 'q':
            error(5, gridsize)
            sys.exit()
        try:
            row, column = map(int, first_click.split(','))
            if row <= 0 or row >= gridsize or column <= 0 or column >= gridsize:
                error(3, gridsize)
                continue
            break
        except ValueError:
            error(4, gridsize)
            continue

    board[column - 1][row - 1] = 1
    # Generate Mine with the first click value
    mine_positions = place_mines(board, minesnum, row, column)
    
    print("Generated Board:")
    print_board(board)
    print("Mine Positions:")
    print(mine_positions)
    
    #-----------------Additional Progress-----------------
    # click_count = 2
    # while True:
    #     user_input = input("Enter coordinates (row, column) for further move: ")
    #     if not user_input:
    #         print("Invalid input. Please make sure the input is in the format (int, int).")
    #         continue
    #     elif user_input == 'q':
    #         print("End the game")
    #         break
    #     try:
    #         row, column = map(int, user_input.split(','))
    #         if row <= 0 or row >= gridsize or column <= 0 or column >= gridsize:
    #             print("Invalid input range. Please make sure the ranges of row and column are from 1 to", gridsize, ".")
    #             continue
    #         elif check(board, row, column) == False:
    #             print("Game Over")
    #             break
    #         else:
    #             board[column - 1][row - 1] = click_count
    #             click_count += 1
    #             print_board(board)
                
    #     except ValueError:
    #         print("Invalid input. Please enter the integer set (row, column) to make a click.")
    #         continue