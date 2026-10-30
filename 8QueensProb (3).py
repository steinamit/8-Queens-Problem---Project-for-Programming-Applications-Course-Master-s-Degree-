# -*- coding: utf-8 -*-
"""
Created on Thu Jan  2 13:16:31 2025

@author: amits
"""

#The solution to Task No. 1, submitted by Oria Shapira, Eden Shmuel, and Amit Stein
import time

def Legal_place(vec, row, col):
    #This function checks if a queen can be safely placed at a given row and col.
    for i in range(row):
        if (vec[i] == col or abs(vec[i] - col) == abs(i - row)):
            return False
    return True

def solve(vec, row, board_size, solutions):
    #Recursive function to find all solutions for the problem presented at the task.
    if row == board_size:
        solutions.append(vec[:])
        return solutions

    for col in range(board_size):
        if Legal_place(vec, row, col):
            vec[row] = col  # Place the queen.
            solve(vec, row + 1, board_size, solutions)
        else:
            vec[row] = -1  # backtrack: Remove the queen.

def print_all_solutions(solutions, board_size):
    #Print all the solutions graphically.
    for i, solution in enumerate(solutions):
        print(f"\nSolution {i + 1}:")
        for row in range(board_size):
            line = ""
            for col in range(board_size):
                if solution[row] == col:
                    line += "Q "  # Queen.
                else:
                    line += "X "  # Empty square.
            print(line)

def eight_queens_problem():
    #Solves the problem for board size `8 x 8`
    #Displays all solutions, their count, and the running time of the solution.
    board_size = 8
    vec = [-1] * board_size  # Initialize the board vector to [-1, -1, -1, -1, -1, -1, -1, -1]
    solutions = []  # List of lists of all valid solutions.
    
    # start measure the running time
    start_time = time.time()
    solve(vec, 0, board_size, solutions)

    # Display all solutions graphically
    print_all_solutions(solutions, board_size)

    #stop mesuring the runing time
    end_time = time.time()
    
    # Display the number of solutions and running time
    print(f"Number of solutions: {len(solutions)}")
    print(f"Running time: {end_time - start_time:.4f} seconds")

# Run the function for an 8x8 chessboard
eight_queens_problem()