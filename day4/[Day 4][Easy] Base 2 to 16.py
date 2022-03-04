#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'bin2hex' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def bin2hex(s):
    dec = int(s, 2)
    hexadec = hex(dec)

    return hexadec[2:].upper()

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    hexstr = input()

    result = bin2hex(hexstr)

    fptr.write(result + '\n')

    fptr.close()

