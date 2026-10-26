r"""Problem    : Between Two Sets
Difficulty : Easy
Domain     : Algorithms > Implementation
URL        : https://www.hackerrank.com/challenges/between-two-sets/problem

Description
-----------
There will be two arrays of integers.  Determine all integers that satisfy the following two conditions:

1. The elements of the first array are all factors of the integer being considered
2. The integer being considered is a factor of all elements of the second array

These numbers are referred to as being *between* the two arrays.  Determine how many such numbers exist.

**Example**
$a = [2, 6]$
$b = [24, 36]$

There are two numbers between the arrays: $6$ and $12$.
$6\%2 = 0$, $6\%6 = 0$, $24\%6 = 0$ and $36\%6 = 0$ for the first value.
$12\%2 = 0$, $12\%6 = 0$ and $24\%12 = 0$, $36\%12 = 0$ for the second value.
Return $2$.

**Function Description**

Complete the *getTotalX* function in the editor below.  It should return the number of integers that are betwen the sets.

getTotalX has the following parameter(s):

- *int a[n]*: an array of integers
- *int b[m]*: an array of integers

**Returns**

- *int:* the number of integers that are between the sets

Input Format
------------
The first line contains two space-separated integers, $n$ and $m$, the number of elements in arrays $a$ and $b$.
The second line contains $n$ distinct space-separated integers $a[i]$ where $0 \le i \lt n$.
The third line contains $m$ distinct space-separated integers $b[j]$ where $0 \le j \lt m$.

Constraints
-----------
- $1 \le n, m \le 10$
- $1 \le a[i] \le 100$
- $1 \le b[j] \le 100$

Sample Input
------------
2 3
2 4
16 32 96

Sample Output
-------------
3
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

import math
def getTotalX(a, b):
    # detect all possible factors of b:
    factors=[]
    for i in range(1,min(b)+1):
        count=0
        for j in b:
            if j%i==0:
                count+=1
        if count==len(b):
            factors.append(i)
    #verify the condition 2
    verified=[]
    for i in factors:
        count=0
        for j in a:
            if i%j==0:
                count+=1
        if count==len(a):
            verified.append(i)
    return len(verified)
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    brr = list(map(int, input().rstrip().split()))

    total = getTotalX(arr, brr)

    fptr.write(str(total) + '\n')

    fptr.close()
