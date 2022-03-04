#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'getFlag' function below.
#
# The function is expected to return a STRING.
#

def getFlag():
    # Write your code here
    return "code#2022!"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    result = getFlag()

    fptr.write(result + '\n')

    fptr.close()