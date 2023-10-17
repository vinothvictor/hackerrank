#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    # Write your code here
    # arr_sort=sorted(arr)
    # arr_sum=list()
    # for i in range(len(arr_sort)):
    #     arr_app=list()
    #     for val in arr_sort:
    #         if arr_sort.index(val)!=i:
    #             arr_app.append(val)
    #     arr_sum.append(sum(arr_app))
    # new_sorted_arr=sorted(arr_sum)
    # print(new_sorted_arr[0],' ',new_sorted_arr[-1])
    # arr_sort=sorted(arr)
    # arr_sum=list()
    
    # for i in range(len(arr_sort)):
    #     arr_add=list()
    #     for val in arr_sort:
    #         if arr_sort.index(val)!=i:
    #            arr_add.append(val)
    #     arr_sum.append(sum(arr_add))
        
    # new_sort=sorted(arr_sum)
    # print(new_sort[0],' ',new_sort[-1]) 
    print(sum(arr)-max(arr), sum(arr)-min(arr))

if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))
    miniMaxSum(arr)