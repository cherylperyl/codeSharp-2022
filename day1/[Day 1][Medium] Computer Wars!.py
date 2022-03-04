#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'fight' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def fight(arr):
    # Write your code here
    while (len(arr) != 1):
        fighter1 = max(arr)
        arr.remove(fighter1)
        fighter2 = max(arr)
        arr.remove(fighter2)
        arr.append(abs(fighter1 - fighter2))
    return arr[0]

# note: more efficient to use set()

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = fight(arr)

    fptr.write(str(result) + '\n')

    fptr.close()

