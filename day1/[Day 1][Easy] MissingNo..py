#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'missingNo' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def missingNo(arr):
    # Write your code here
    max_n = max(arr)
    min_n = min(arr)
    
    missing = []
    for i in range(min_n, max_n+1):
        if i not in arr:
            missing.append(i)
            
    return missing
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = missingNo(arr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()