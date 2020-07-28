#!/bin/python3

import math
import os
import random
import re
import sys

def rot_once(l):
    return l[1:] + [l[0]]

# Complete the rotLeft function below.
def rotLeft(a, d):
    r = d % len(a)
        
    return a[r:] + a[:r]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nd = input().split()

    n = int(nd[0])

    d = int(nd[1])

    a = list(map(int, input().rstrip().split()))

    result = rotLeft(a, d)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
