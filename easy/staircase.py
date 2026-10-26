r"""Problem    : Staircase
Difficulty : Easy
Domain     : Algorithms > Warmup
URL        : https://www.hackerrank.com/challenges/staircase/problem

Description
-----------
Staircase detail

This is a staircase of size $n = 4$:

	   #
	  ##
	 ###
	####

Its base and height are both equal to $n$.  It is drawn using `#` symbols and spaces. **The last line is not preceded by any spaces.**

Write a program that prints a staircase of size $n$.

**Function Description**

Complete the $staircase$ function with the following parameter(s):

- $int\ n$: an integer

**Print**

Print a staircase as described above. No value should be returned.
**Note**: The last line is not preceded by spaces. All lines are right-aligned.

Input Format
------------
A single integer, $n$, denoting the size of the staircase.

Constraints
-----------
$0 \lt n \le 100$ .

Sample Input
------------
6

Sample Output
-------------
#
    ##
   ###
  ####
 #####
######
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
# Complete the 'staircase' function below.
#
# The function accepts INTEGER n as parameter.
#

def staircase(n):
    # Write your code hereprint("#")
    
    for i in range(1,n+1):
        j=0
        s=0
        while s<n-i:
            print(" ",end="")
            s+=1
        while j<i:
            print("#",end="")
            j+=1
        print()
            

if __name__ == '__main__':
    n = int(input().strip())

    staircase(n)
