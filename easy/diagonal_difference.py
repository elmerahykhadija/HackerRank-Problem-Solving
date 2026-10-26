r"""Problem    : Diagonal Difference
Difficulty : Easy
Domain     : Algorithms > Warmup
URL        : https://www.hackerrank.com/challenges/diagonal-difference/problem

Description
-----------
Given a square matrix, calculate the absolute difference between the sums of its diagonals.

For example, the square matrix $arr$ is shown below:

	1 2 3
    4 5 6
    9 8 9

- The left-to-right diagonal = $1 + 5 + 9 = 15$.
- The right-to-left diagonal = $3 + 5 + 9 = 17$.

Their absolute difference is $|15 - 17| = 2$.

**Function description**

Complete the $\textit{diagonalDifference}$ function with the following parameter:

-	$int\ arr[n][m]$: a 2-D array of integers

**Return**

-	$int$: the absolute difference in sums along the diagonals

Input Format
------------
The first line contains a single integer, $n$,  the number of rows and columns in the square matrix $arr$.
Each of the next $n$ lines describes a row, $arr[i]$, and consists of $n$ space-separated integers $arr[i][j]$.

Constraints
-----------
+ $-100 \le arr[i][j] \le 100$

Sample Input
------------
STDIN      Function
-----      --------
3           arr[][] sizes n = 3, m = 3
11 2 4     arr = [[11, 2, 4], [4, 5, 6], [10, 8, -12]]
4 5 6
10 8 -12

Sample Output
-------------
15
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
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):
    diag=[0,0]
    for i in range(len(arr)):
        diag[0]+=arr[i][i]
        diag[1]+=arr[i][len(arr)-i-1]
    
    return abs(diag[0]-diag[1])
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
