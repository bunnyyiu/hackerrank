#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the diagonalDifference function below.
def diagonalDifference(arr):
    leftSum = 0;
    rightSum = 0;
    
    for i in range(0, len(arr)):
        leftSum += arr[i][i]
        rightSum += arr[i][len(arr) - 1 - i]
    return abs(leftSum - rightSum)
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
