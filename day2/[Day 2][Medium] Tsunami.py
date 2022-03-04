#!/bin/python3

from math import ceil, sqrt
import os
import random
import re
import sys

#
# Complete the 'can_build' function below.
#
# The function is expected to return a BOOLEAN.
# The function accepts INTEGER area as parameter.
#

def can_build(area):
    # Write your code here
    for i in range(ceil(sqrt(area))):
        if sqrt(area - i**2).is_integer():
            return True
    return False

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    area = int(input().strip())

    solution = can_build(area)

    fptr.write(str(int(solution)) + '\n')

    fptr.close()