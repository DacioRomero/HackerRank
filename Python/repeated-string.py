#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the repeatedString function below.
def repeatedString(s, n):
    count = 0

    if n > len(s):
        for char in s:
            if char == 'a':
                count += 1

        count *= n // len(s)
    
    for char in s[:n % len(s)]:
        if char == 'a':
            count += 1

    return count
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    n = int(input())

    result = repeatedString(s, n)

    fptr.write(str(result) + '\n')

    fptr.close()
