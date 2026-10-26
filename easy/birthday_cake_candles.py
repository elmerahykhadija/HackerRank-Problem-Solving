r"""Problem    : Birthday Cake Candles
Difficulty : Easy
Domain     : Algorithms > Warmup
URL        : https://www.hackerrank.com/challenges/birthday-cake-candles/problem

Description
-----------
You are in charge of the cake for a child's birthday. It will have one candle for each year of their total age. They will only be able to blow out the tallest of the candles. Your task is to count how many candles are the tallest.

**Example**

$candles = [4, 4, 1, 3]$

The tallest candles are `4` units high. There are `2` candles with this height, so the function should return `2`.

**Function Description**

Complete the function $birthdayCakeCandles$ with the following parameter(s):

- $int\ candles[n]$: the candle heights

**Returns**

- $int$: the number of candles that are tallest

Input Format
------------
The first line contains a single integer, $n$, the size of $candles[]$.
The second line contains $n$ space-separated integers, where each integer $i$ describes the height of $candles[i]$.

Constraints
-----------
- $1 \le n \le 10^{5}$
- $1 \le candles[i] \le 10^{7}$

Sample Input
------------
4
3 2 1 3

Sample Output
-------------
2
"""

# ============================================================
# Solution
# ============================================================

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'birthdayCakeCandles' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY candles as parameter.
#

def birthdayCakeCandles(candles):
    maximum=max(candles)
    n=0
    for i in candles:
        if maximum==i:
            n+=1
    return n
    # Write your code here

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    candles_count = int(input().strip())

    candles = list(map(int, input().rstrip().split()))

    result = birthdayCakeCandles(candles)

    fptr.write(str(result) + '\n')

    fptr.close()
