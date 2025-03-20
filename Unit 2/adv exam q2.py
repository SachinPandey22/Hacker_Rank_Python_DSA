#!/bin/python3

import math
import os
import random
import re
import sys
import ast
import json


#
# Complete the 'array_rank_transform' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def array_rank_transform(arr):
    # Write your code here
    arr2 = sorted(set(arr))
    lst = []
    rank_dic = {val: idx for idx, val in enumerate(arr2, start=1)}
    for a in arr:
        lst.append(rank_dic[a])
    return lst

if __name__ == '__main__':
    outfile = open(os.environ['OUTPUT_PATH'], 'w')
    input_lines = sys.stdin.read().strip().split('\n')
    
    for line in input_lines:
        if line:  # Check if the line is not empty
            arr = json.loads(line)  # Parse the line as JSON
            result = array_rank_transform(arr)
            outfile.write(str(result) + '\n')
    outfile.close()