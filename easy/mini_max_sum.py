r"""Problem    : Mini-Max Sum
Difficulty : Easy
Domain     : Algorithms > Warmup
URL        : https://www.hackerrank.com/challenges/mini-max-sum/problem

Description
-----------
Given five positive integers, find the minimum and maximum values that can be calculated by summing exactly four of the five integers. Then print the respective minimum and maximum values as a single line of two space-separated long integers.

**Example**
$arr = [1, 3, 5, 7, 9]$

The minimum sum is $1 + 3 + 5 + 7 = 16$ and the maximum sum is $3 + 5 + 7 + 9 = 24$.  The function prints

    16 24

**Function Description**

Complete the $miniMaxSum$ function with the following parameter(s):

- $arr[5]$: an array of $5$ integers

**Print**

Print two space-separated integers on one line: the minimum sum and the maximum sum of $4$ of $5$ elements.No value should be returned.

**Note** For some languages, like C, C++, and Java, the sums may require that you use a long integer due to their size.

Input Format
------------
A single line of five space-separated integers.

Constraints
-----------
$1 \le arr[i] \le 10^9$

Sample Input
------------
1 2 3 4 5

Sample Output
-------------
10 14
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
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    arr.sort()
    minimum=0
    maximum=0
    for i in range(0,4):
        minimum+=arr[i]
    for j in range(4,0,-1):
        maximum+=arr[j]
    print(f"{minimum} {maximum}") 
if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
