#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'fibonacci_digits' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER n as parameter.
#

def fibonacci_digits(n):
    # Write your code here
    if n < 2:
        return 1
    e = (1 + 5**0.5) / 2
    return math.ceil((n + math.log10(5) / 2 - 1) / math.log10(e))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    solution = fibonacci_digits(n)

    fptr.write(str(solution) + '\n')

    fptr.close()