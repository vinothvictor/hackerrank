#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    # Write your code here
    positve=list()
    negative=list()
    zero=list()
    
    for a in arr:
        if a==0:
            zero.append(a)
        elif a<0:
            negative.append(a)
        elif a>0:
            positve.append(a)
            
    positve_val=len(positve)/len(arr)
    negative_val=len(negative)/len(arr)
    zero_val=len(zero)/len(arr)
    
    return "{:.6f},{:.6f},{:.6f}".format(positve_val,negative_val,zero_val)
            
    
    
if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))
    # print(arr)
    values=plusMinus(arr)
    for val in values.split(','):
        print(val)