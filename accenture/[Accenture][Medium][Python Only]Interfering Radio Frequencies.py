#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'is_interfere_with_existing_application' function below.
#
# The function is expected to return a BOOLEAN.
# The function accepts following parameters:
#  1. STRING_ARRAY current_application
#  2. 2D_STRING_ARRAY existing_applications
#

def is_interfere_with_existing_application(current_application, existing_applications):
    # Write your code here
    max_lat = 0
    max_lng = 0
    for freq, lat, lng, dist in existing_applications:
        if(lat + dist) > max_lat:
            max_lat = lat+dist
        if(lng + dist) > max_lng:
            max_lng = lng+dist
    
    space = [["x" for _ in range(max_lat)] for _ in range(max_lng)]
    
    for freq, lat, lng, dist in existing_applications:
        for i in range(lat-dist-1, lat+dist):
            for j in range(lng-dist-1, lng+dist):
                if (i >= 0 and i < max_lat and j >= 0 and j < max_lng):
                    space[j][i] = freq
    
    freq, lat, lng, dist = current_application
    for i in range(lat-dist-1, lat+dist):
            for j in range(lng-dist-1, lng+dist):
                if (i >= 0 and i < max_lat and j >= 0 and j < max_lng):
                    if space[j][i] == freq:
                        return True
    return False
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    num_existing = int(input().strip())

    line = input().rstrip().split()
    current_application = [line[0], int(line[1]), int(line[2]), int(line[3])]

    existing_applications = []

    for _ in range(num_existing):
        line = input().rstrip().split()
        existing_applications.append([line[0], int(line[1]), int(line[2]), int(line[3])])

    solution = is_interfere_with_existing_application(current_application, existing_applications)

    fptr.write(str(int(solution)) + '\n')

    fptr.close()