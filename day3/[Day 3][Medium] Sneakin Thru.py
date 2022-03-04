#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'sneakinThru' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER ic
#  2. INTEGER num
#

def findXOR(x):
    mod = x%4

    if mod == 0:
        return x
    elif mod == 1:
        return 1
    elif mod == 2:
        return x+1
    elif mod == 3:
        return 0
    
def findXORrange(l,r):
    l_XOR = findXOR(l-1)
    r_XOR = findXOR(r)
    return (l_XOR ^ r_XOR)

def sneakinThru(ic, num):
    # Your Solution here
    curr_ic = ic
    checksum = findXORrange(curr_ic, curr_ic + num-1)
    curr_ic += num
    for i in range(2, num):
        checksum ^= findXORrange(curr_ic, curr_ic + num - i)
        curr_ic += num
    return checksum^curr_ic

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ic = int(input().strip())

    num = int(input().strip())

    checksum = sneakinThru(ic, num)

    fptr.write(str(checksum) + '\n')

    fptr.close()