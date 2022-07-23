import numpy as np
from math import *

grid = [[5,3,0,0,7,0,0,0,0],
        [6,0,0,1,9,5,0,0,0],
        [0,9,8,0,0,0,0,6,0],
        [8,0,0,0,6,0,0,0,3],
        [4,0,0,8,0,3,0,0,1],
        [7,0,0,0,2,0,0,0,6],
        [0,6,0,0,0,0,2,8,0],
        [0,0,0,0,1,9,0,0,5],
        [0,0,0,0,0,0,0,0,0]]


def find_empty(grid):
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j]==0:
                return [i,j]

    return None

def isvalid(grid,number,row,column):

    #find number in rows
    for i in range(len(grid)):
        if grid[row][i]==number:
            return False

    #find number in columns
    for i in range(len(grid)):
        if grid[i][column]==number:
            return False

    y=(column//3)*3
    x=(row//3)*3

    #find number in square
    for i in range(int(sqrt(len(grid)))):
        for j in range(int(sqrt(len(grid[i])))):
            if grid[i+x][j+y]==number:
                return False

    return True

def print_board(grid):
    for i in range(len(grid)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - - ")

        for j in range(len(grid[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")

            if j == 8:
                print(grid[i][j])
            else:
                print(str(grid[i][j]) + " ", end="")

def solve_sudoku(grid):
    # print_board( grid )
    # if none, then game is finished
    if find_empty(grid)==None:
        return True
    else:
        row,column=find_empty(grid)
    #try possible numbers from 1-9 and check if its valid
    for i in range(1,10):
        if isvalid(grid,i,row,column)==True:
            grid[row][column]=i
            #recrusive function
            if solve_sudoku(grid):
                return True
            else:
                #backtrack and reset to zero
                grid[row][column] = 0

    # If values are not valid
    return False


print_board(grid)
solve_sudoku(grid)
print("-----before------")
print("------after------")
print_board(grid)








