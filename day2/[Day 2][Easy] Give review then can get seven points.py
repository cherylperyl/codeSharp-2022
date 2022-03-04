#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'compileReviews' function below.
#
# The function is expected to return a 2D_STRING_ARRAY.
# The function accepts 2D_STRING_ARRAY reviewList as parameter.
#

def compileReviews(reviewList):
    # Write your code here
    review_dict = {}
    
    for pid, review in reviewList:
        rating = int(review.split("/")[0])
        if pid not in review_dict:
            review_dict[pid] = (rating , 1)
        else:
            total = review_dict[pid][0] + rating
            count = review_dict[pid][1] + 1
            review_dict[pid] = (total, count)
            
    result_list = []
    for key, value in review_dict.items():
        rating = round(value[0]/value[1])
        result_list.append([key, str(rating) + '/5'])
        
    result_list = sorted(result_list, key=lambda x:x[0])
    return result_list

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    reviewList_rows = int(input().strip())
    reviewList_columns = int(input().strip())

    reviewList = []

    for _ in range(reviewList_rows):
        reviewList.append(input().rstrip().split())

    results = compileReviews(reviewList)

    fptr.write('\n'.join([' '.join(x) for x in results]))
    fptr.write('\n')

    fptr.close()
    
    