#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'translate' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def translate(s):
    # Write your code here
    dictionary = {"A": "4",
                 "B":"8",
                 "C":"[",
                 "E":"3",
                  "I":"|",
                 "J":"]",
                 "O":"0",
                 "S":"$",
                 "T":"7",
                 "Z":"2",
                 "a":"@",
                 "b":"6",
                 "g":"9",
                 "l":"1",
                 "s":"5",
                 "t":"+", '4': 'A', '8': 'B', '[': 'C', '3': 'E', '|': 'I', ']': 'J', '0': 'O', '$': 'S', '7': 'T', '2': 'Z', '@': 'a', '6': 'b', '9': 'g', '1': 'l', '5': 's', '+': 't'}
        
    new_word = ""
    for ch in s:
        if ch in dictionary:
            new_word += dictionary[ch]
        else:
            new_word += ch
    
    return new_word

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = translate(s)

    fptr.write(result + '\n')

    fptr.close()