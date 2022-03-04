#!/bin/python3

import math
import os
import random
import re
import sys
from typing import List

#
# Complete the custom_iterator class below.
#
# Your custom_iterator object will be instantiated and called as such:
# obj = custom_iterator(nums)
# param_1 = obj.next()

class custom_iterator:

    def __init__(self, nums: List[List[int]]):
        self.List = nums
        self.flat = []
        for i in range(len(nums)-1, -1, -1):
            if type(nums[i]) == int:
                self.flat.append(nums[i])
            else:
                for j in range(len(nums[i])-1, -1, -1):
                    self.flat.append(nums[i][j])

    def next(self) -> int:
        if len(self.flat) != 0:
            return self.flat.pop()
        else:
            return -1
        # num = self.num
        # self.num += 1
        # return num

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    num_lines = int(input().strip())
    
    _input = []

    for _ in range(num_lines):
        line = input().rstrip().split()
        line = [int(e) for e in line]
        _input.append(line)
        
    num_next = int(input().strip())
        
    obj = custom_iterator(_input)
    for _ in range(num_next):
        fptr.write(str(obj.next()))
        if (_ != num_next-1): 
            fptr.write(" ")
    fptr.write('\n')

    fptr.close()