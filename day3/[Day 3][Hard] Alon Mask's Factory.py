#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'transport' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY pos as parameter.
#

from heapq import heappop, heappush

def convertPos(x):
    if x < 10:
        return 0, x
    return int(str(x)[0]), int(str(x)[1])

def extendPath(curr_coor):
    r, c = curr_coor[0], curr_coor[1]
    next_steps = []
    if (r+1) < 10:
        next_steps.append((r+1, c))
    if (c+1) < 10:
        next_steps.append((r, c+1))
    if (r-1) >= 0:
        next_steps.append((r-1, c))
    if (c-1) >= 0:
        next_steps.append((r, c-1))
    return next_steps

def bfs(start, end, oub):
    curr = start
    priorityQ = []
    heappush(priorityQ, (1, [start]))
    # count = 0

    while curr != end and len(priorityQ) > 0:
        priority = heappop(priorityQ)
        path = priority[1]
        curr = path[-1]
        
        # count += 1
        # print(f"iteration {count}")

        next_steps = extendPath(curr)
        for step in next_steps:
            # print(step)
            if step == end:
                new_path = path + [step]
                heappush(priorityQ, (len(new_path), new_path))
            elif (step not in set(path)) and (step not in oub):
                new_path = path + [step]
                # print(new_path)
                heappush(priorityQ, (len(new_path), new_path))

    if curr == end:
        return path
    else:
        return []

def transport(pos):
    # Write your code here
    
    possible_paths = []

    perms = [(0, 1, 2),
            (1, 2, 0)]

    for order in perms:
        one_iter = {}
        oub = set()
        stations = []

        for i in pos:
            coor = convertPos(i)
            stations.append(coor)
            oub.add(coor)
    
        for i in order:
            start = stations[i]
            end = stations[i+1]
            shortest_path = bfs(start, end, oub)
            if shortest_path != []: # only add when there is a shortest path
                for step in shortest_path:
                    oub.add(step)
                one_iter[i] = shortest_path[1:]
            
        if sorted(list(one_iter.keys())) == [0,1,2]:
            one_iter_list = []
            for i in range(len(stations)-1):
                one_iter_list.extend(one_iter[i])
            possible_paths.append(one_iter_list)

    sorted_possible_paths = sorted(possible_paths, key=lambda x: len(x))
    for path in possible_paths:
        print(path)
    optimal = sorted_possible_paths[0]

    f_result = []
    for r,c in optimal:
        f_result.append(int(str(r) + str(c)))
        
    return [pos[0]] + f_result
        
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    pos_count = int(input().strip())

    pos = list(map(int, input().rstrip().split()))

    solution = transport(pos)

    fptr.write(' '.join(map(str, solution)))
    fptr.write('\n')

    fptr.close()