#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'fibs' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER n as parameter.
#

def fibs(n):
    # Write your code here
    f = [0, 1]     
    for i in range(2, n+1):
        f.append((f[i-1] + f[i-2])% 2147483647)
    return f[n]
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    output = fibs(n)

    fptr.write(str(output) + '\n')

    fptr.close()