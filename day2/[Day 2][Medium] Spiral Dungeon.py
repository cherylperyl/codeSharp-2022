#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'spiral_dungeon' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts 2D_INTEGER_ARRAY dungeon as parameter.
#

def returnNextStep(step_dir, curr_coor, l, w):
    curr_r, curr_c = curr_coor[0], curr_coor[1]
    step = int(step_dir[1])
    if step_dir[0] == "r":
        if (curr_r + step) < l and (curr_r + step) >= 0:
            return (curr_r + step, curr_c)
    else:
        if (curr_c + step) < w and (curr_c) + step >= 0:
            return (curr_r, curr_c + step)

def spiral_dungeon(dungeon):
    l = len(dungeon)
    if l == 0:
        return []
    w = len(dungeon[0])
    if w == 0:
        return []

    seen = [[0 for _ in range(w)] for _ in range(l)]
    direction = 0
    step_dir = ("r", 1)
    dir_to_turn = [("r", 1),("c", 1), ("r", -1), ("c", -1)]
    curr_coor = (0,0)

    path = []

    for _ in range(l*w):
        path.append(curr_coor)
        seen[curr_coor[0]][curr_coor[1]] = "s"
        next_step = returnNextStep(step_dir, curr_coor, l, w)
        if next_step == None or seen[next_step[0]][next_step[1]] == "s":
            direction = (direction + 1) % 4
            step_dir = dir_to_turn[direction]
            curr_coor = returnNextStep(step_dir, curr_coor, l, w)
        else:
            curr_coor = next_step
    
    result = []
    for r, c in path:
        result.append(dungeon[r][c])
    
    return result


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    dungeon = []

    for _ in range(n):
        dungeon.append(list(map(int, input().rstrip().split())))

    solution = spiral_dungeon(dungeon)

    fptr.write(' '.join(map(str, solution)))
    fptr.write('\n')

    fptr.close()