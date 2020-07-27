#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c):
    pos = 0
    jumps = 0

    while pos < len(c) - 1:
        if pos + 2 < len(c) and c[pos + 2] == 1:
            pos += 1
        else:
            pos += 2
        
        jumps += 1
    
    return jumps

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c)

    fptr.write(str(result) + '\n')

    fptr.close()
