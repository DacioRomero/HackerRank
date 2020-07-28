#!/bin/python3

import math
import os
import random
import re
import sys

def calc_sum(arr, x, y):
    top = arr[y]
    middle = arr[y + 1]
    bottom = arr[y + 2]

    return (
        top[x] + top[x + 1] + top[x + 2] +
        middle[x + 1] +
        bottom[x] + bottom[x + 1] + bottom[x + 2]
    )

# Complete the hourglassSum function below.
def hourglassSum(arr):
    m = -math.inf

    for y in range(len(arr) - 2):
        for x in range(len(arr[y]) - 2):
            s = calc_sum(arr, x, y)

            if m < s:
                m = s
    
    return m

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
