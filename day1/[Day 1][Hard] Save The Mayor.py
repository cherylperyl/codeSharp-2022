#!/bin/python3

import math
import os
import random
import re
import sys
from heapq import heappush, heappop

#
# Complete the 'minMana' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY lair as parameter.
#

def minMana(lair):
    # Your solution here should return the minimum mana you need to save the mayor
    numOfRows = len(lair)
    numOfCols = len(lair[0])
    
    priorityQ = []
    start_cost = (-lair[0][0] + 1) if (lair[0][0] <= 0) else 0
    
    heappush(priorityQ,(start_cost, lair[0][0], (0, 0)))
    visited = set()
    
    while not ((priorityQ[0][2][0] == numOfRows-1) and (priorityQ[0][2][1] == numOfCols-1)):
        priority = heappop(priorityQ)
        cost, curr_depth, coor = priority[0], priority[1], priority[2]
        curr_r, curr_c = coor[0], coor[1]
        visited.add((curr_r, curr_c))
        next_steps = []
        
        if curr_r != numOfRows-1 and (curr_r+1, curr_c) not in visited: #means i can move down
            next_steps.append((curr_r+1, curr_c))
        
        if curr_c != numOfCols-1 and (curr_r, curr_c+1) not in visited: #means i can move right
            next_steps.append((curr_r, curr_c+1))
            
        for next_r, next_c in next_steps:
            new_depth = curr_depth + lair[next_r][next_c]
            if -new_depth >= cost:
                new_cost = -new_depth+1
            else:
                new_cost = cost
                    
            heappush(priorityQ,(new_cost, new_depth, (next_r, next_c)))
            
    if priorityQ[0][0] == 0:
        return 1
    return priorityQ[0][0]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    m = int(input().strip())

    n = int(input().strip())

    lair = []

    for _ in range(m):
        lair.append(list(map(int, input().rstrip().split())))

    manaNeeded = minMana(lair)

    fptr.write(str(manaNeeded) + '\n')

    fptr.close()