#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'find_number_of_clones' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY schedule as parameter.
#

def find_number_of_clones(schedule):
    # Write your code here
    timings = []
    for i in range(0,len(schedule),2):
        timings.append([schedule[i], schedule[i+1]])
        
    # print(schedule)
    # print(timings)
    
    timings = sorted(timings, key=lambda x:x[0])
    
    meetings_in_prog = [0]
    clones_needed = 0
    curr_time = 0
    
    for start, end in timings:
        curr_time = start
        for time in meetings_in_prog:
            if time <= curr_time:
                while time in meetings_in_prog:
                    meetings_in_prog.remove(time)
        meetings_in_prog.append(end)
        print(meetings_in_prog)
        if len(meetings_in_prog) > clones_needed:
            clones_needed = len(meetings_in_prog)
            
    return clones_needed
    
    
    
    
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    schedule = list(map(int, input().rstrip().split()))

    solution = find_number_of_clones(schedule)

    fptr.write(str(solution) + '\n')

    fptr.close()