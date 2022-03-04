#!/bin/python3

import math
import os
import random
import re
import sys
import datetime as dt

#
# Complete the 'validate' function below.
#
# The function is expected to return a BOOLEAN.
# The function accepts STRING cert_id as parameter.
#

def validate(cert_id):
    # Write your code here
    cert_id_component = cert_id.split("-")
    
    date, course_code, issue_code, check = cert_id_component[0], cert_id_component[1], cert_id_component[2], cert_id_component[3]
    
    
    d, m, y = int(date[0:2]), int(date[2:4]), int(date[4:])
    # check date
    try:
        if dt.datetime(y,m,d) > dt.datetime.now():
            return 0
    except ValueError:
        return 0
    
    cc_p, ic_p = 1, 1
    for ch in course_code:
        cc_p *= int(ch)

    for ch in issue_code:
        ic_p *= int(ch)
    
    if y >= 2016:
        result = (cc_p + ic_p + (y-2016)) % 10
    else:
        result = (cc_p + ic_p) % 10
    
    if result == int(check):
        return 1
    return 0

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    cert_id = input()

    solution = validate(cert_id)

    fptr.write(str(int(solution)) + '\n')

    fptr.close()