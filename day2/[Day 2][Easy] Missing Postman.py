#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'validateEmail' function below.
#
# The function is expected to return a BOOLEAN.
# The function accepts STRING s as parameter.
#

def validateEmail(s):
    # Write your code here
    email_id, domain = s.split("@")
    result = 1
    for ch in email_id:
        if not ch.isalnum() and ch != ".":
            result = 0
            
    period_cnt = 0
    for ch in email_id:
        if ch == ".":
            period_cnt += 1
        else:
            period_cnt = 0
        if period_cnt > 1:
            result = 0
            break
            
    if domain[0] == "." or domain[0] == "-" or domain[-1] == "." or domain[-1] == "-" or email_id[0]=="." or email_id[-1] == ".":
        result = 0
            
    period_cnt = 0
    hyphen_cnt = 0
    for ch in domain:
        if ch == ".":
            period_cnt += 1
            hyphen_cnt = 0
        elif ch == "-":
            hyphen_cnt += 1
            period_cnt = 0
        else:
            period_cnt = 0
        if period_cnt > 1 or hyphen_cnt > 1:
            result = 0
            break
        
    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    email = input()

    result = validateEmail(email)

    fptr.write(str(int(result)) + '\n')

    fptr.close()

