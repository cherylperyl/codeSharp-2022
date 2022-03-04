#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'is_party_possible' function below.
#
# The function is expected to return a BOOLEAN.
# The function accepts 2D_CHARACTER_ARRAY relationships as parameter.
#

def is_party_possible(relationships):
    # Write your code here
    relation_dict = {}
    for s, h in relationships:
        relation_dict[s] = h
        
    curr_h = None
        
    for s, h in relationships:
        curr_h = h
        checked = set()
        while curr_h in relation_dict and curr_h not in checked:
            checked.add(curr_h)
            curr_h = relation_dict[curr_h]
            if curr_h == s:
                return False

    # inverse = set()
    # for s, h in relationships:
    #     inverse.add((h,s))
    # for s,h in relationships:
    #     if (s,h) in inverse:
    #         return False
    return True

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    relationships = []

    for _ in range(n):
        relationships.append(list(map(lambda x: x[0], input().rstrip().split())))

    solution = is_party_possible(relationships)

    fptr.write(str(int(solution)) + '\n')

    fptr.close()

