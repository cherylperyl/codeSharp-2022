#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'compress' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def compress(s):
    # Write your code here
    prev_ch = ""
    curr_count = 0
    return_str = ""
    
    for ch in (s + "."):
        if prev_ch == "":
            prev_ch = ch
            curr_count += 1
        elif ch == prev_ch:
            curr_count += 1
        else:
            if curr_count > 2:
                return_str += prev_ch + str(curr_count)
            else:
                return_str += prev_ch*curr_count
            prev_ch = ch
            curr_count = 1
            
    return return_str

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = compress(s)

    fptr.write(result + '\n')

    fptr.close()