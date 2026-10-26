r"""Problem    : Time Conversion
Difficulty : Easy
Domain     : Algorithms > Warmup
URL        : https://www.hackerrank.com/challenges/time-conversion/problem

Description
-----------
Given a time in [$12$-hour AM/PM format](https://en.wikipedia.org/wiki/12-hour_clock), convert it to military (24-hour) time.

Note:
- 12:00:00AM on a 12-hour clock is 00:00:00 on a 24-hour clock.
- 12:00:00PM on a 12-hour clock is 12:00:00 on a 24-hour clock.

**Example**

- $\text{s = '12:01:00PM'}$

  Return '12:01:00'.

- $\text{s = '12:01:00AM'}$

  Return '00:01:00'.

**Function Description**

Complete the $timeConversion$ function with the following parameter(s):

- $string\ s$: a time in $12$ hour format

**Returns**

- $string$: the time in $24$ hour format

Input Format
------------
A single string $s$ that represents a time in $12$-hour clock format (i.e.: $\text{hh:mm:ssAM}$ or $\text{hh:mm:ssPM}$).

Constraints
-----------
- All input times are valid

Sample Input
------------
07:05:45PM

Sample Output
-------------
19:05:45
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
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    # Write your code here
    d={ "01":"13",
    "02":"14",
    "03":"15",
    "04":"16",
    "05":"17",
    "06":"18",
    "07":"19",
    "08":"20",
    "09":"21",
    "10":"22",
    "11":"23",
    "12":"00"}
    l=list(s)
    if l[8]=='A' and l[:2]==["1","2"]:
        return "00" +"".join(l[2:8])
    elif (l[8]=='P' and l[:2]==["1","2"]) or l[8]=='A':
        return "".join(l[:8])
    
    x=d["".join(l[:2])]
    return x+"".join(l[2:8])
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()
