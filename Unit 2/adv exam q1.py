#!/bin/python3

import math
import os
import random
import re
import sys
import ast


# Enter your code here. Read input from STDIN. Print output to STDOUT
#
# Complete the 'roman_to_int' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def roman_to_int(s):
    # Write your code here
    conv_dic = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D' : 500, 'M': 1000 }
    #special_dic = {'IV': 4, 'IX': 9, 'XL': 40, 'XC': 90, 'CD': 400, 'CM': 900}
    conv_num = 0
    for i in range(len(s)):
        
        if i < len(s) - 1 and conv_dic[s[i]] < conv_dic[s[i + 1]]:
            conv_num -= conv_dic[s[i]]
        else:
            conv_num += conv_dic[s[i]]
    
    return conv_num
if __name__ == '__main__':    
    outfile = open(os.environ['OUTPUT_PATH'], 'w')
    input_data = sys.stdin.read().strip().split('\n')
    
    for line in input_data:
        s = line.strip().strip('"')  
        result = roman_to_int(s)
        outfile.write(str(result) + '\n')
    outfile.close()
