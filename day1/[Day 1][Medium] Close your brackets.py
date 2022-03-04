#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'solution' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def solution(s):
    # Write your code here
    right, left = 0, 0
    for ch in s:
        if ch == "(":
            left += 1
        elif ch == ")":
            if left > 0:
                left -= 1
            else:
                right += 1
    return left+right

# # can use pop(0) and push()
# def solution(s):
#     stack = []
#     n = 1
#     for ch in s:
#         if ch == "(":
#             stack.append(ch)
#         elif len(stack) == 0 and ch == ")":
#             n += 1
#         else:
#             stack.pop()
#     return n + len(stack)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solution(s)

    fptr.write(str(result) + '\n')

    fptr.close()