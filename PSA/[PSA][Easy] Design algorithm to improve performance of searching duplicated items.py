#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'no_match_exists' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY list1
#  2. INTEGER_ARRAY list2
#

def no_match_exists(list1, list2):

    # Write your code here
    list1, list2 = set(list1), set(list2)
    for i in list1:
        if i in list2:
            return 0
    return 1

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    len1 = int(input().strip())

    list1 = list(map(int, input().rstrip().split()))

    len2 = int(input().strip())

    list2 = list(map(int, input().rstrip().split()))

    solution = no_match_exists(list1, list2)

    fptr.write(str(solution) + '\n')

    fptr.close()