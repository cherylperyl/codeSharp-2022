#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'solution_finder' function below.
#
# The function is expected to return a STRING_ARRAY.
# The function accepts following parameters:
#  1. 2D_CHARACTER_ARRAY board
#  2. STRING_ARRAY dictionary
#

def solution_finder(board, dictionary):
    found = []
    board_r = len(board)
    board_c = len(board[0])

    letter_coor = {}
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] not in letter_coor:
                letter_coor[board[i][j]] = [(i,j)]
            else:
                letter_coor[board[i][j]].append((i,j))

    for word in dictionary:
        first_ch = True
        curr_paths = []
        curr_length = 1
        next_paths = []
        for ch in word:
            if ch not in letter_coor:
                break
            elif first_ch:
                curr_paths = [[coor] for coor in letter_coor[ch]]
                first_ch = False
            elif len(curr_paths) == 0:
                break
            
            for path in curr_paths:
                curr_coor = path[-1]
                r, c = curr_coor[0], curr_coor[1]
                if curr_length == len(word) and ch == board[r][c]:
                    found.append(word)
                elif ch == board[r][c]:
                    if (r+1 < board_r) and (r+1, c) not in path: # add on to list
                        new_path = path + [(r+1, c)]
                        next_paths.append(new_path)
                    if (r-1 >= 0) and (r-1, c) not in path: 
                        new_path = path + [(r-1, c)]
                        next_paths.append(new_path)
                    if (c+1 < board_c) and (r, c+1) not in path:
                        new_path = path + [(r, c+1)]
                        next_paths.append(new_path)
                    if (c-1 >= 0) and (r, c-1) not in path:
                        new_path = path + [(r, c-1)]
                        next_paths.append(new_path)
        
            curr_paths = next_paths
            next_paths = []
            
            curr_length += 1
            
    return sorted(set(found))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    board_len = int(input().strip())

    board = []

    for _ in range(board_len):
        board.append(list(map(lambda x: x[0], input().rstrip().split())))

    dict_len = int(input().strip())

    dictionary = input().rstrip().split()

    solution = solution_finder(board, dictionary)

    fptr.write(' '.join(solution))
    fptr.write('\n')

    fptr.close()

