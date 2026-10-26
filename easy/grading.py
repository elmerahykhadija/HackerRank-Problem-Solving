r"""Problem    : Grading Students
Difficulty : Easy
Domain     : Algorithms > Implementation
URL        : https://www.hackerrank.com/challenges/grading/problem

Description
-----------
HackerLand University has the following grading policy:

* Every student receives a $grade$ in the inclusive range from $0$ to $100$.
* Any $grade$ less than $40$ is a failing grade.

Sam is a professor at the university and likes to round each student's $grade$ according to these rules:

* If the difference between the $grade$ and the next multiple of $5$ is less than $3$, round $grade$ up to the next multiple of $5$.
* If the value of $grade$ is less than $38$, no rounding occurs as the result will still be a failing grade.

**Examples**

- $grade = 84$ round to $85$ (85 - 84 is less than 3)
- $grade = 29$ do not round (result is less than 38)
- $grade = 57$ do not round (60 - 57 is 3 or higher)

Given the initial value of $grade$ for each of Sam's $n$ students, write code to automate the rounding process.

**Function Description**

Complete the function $gradingStudents$ with the following parameter(s):

- $int\ grades[n]$: the grades before rounding

**Returns**

- $int[n]$: the grades after rounding

Input Format
------------
The first line contains a single integer, $n$, the number of students.
Each line $i$ of the $n$ subsequent lines contains a single integer, $grades[i]$.

Constraints
-----------
* $ 1 \le n \le 60 $
* $ 0 \le grades[i] \le 100 $

Sample Input
------------
4
73
67
38
33

Sample Output
-------------
75
67
40
33
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



def gradingStudents(grades):
    
    output=[]
    for i in range(len(grades)) :
        next_multiple=((grades[i]//5)+1)*5
        if next_multiple-grades[i] < 3 and grades[i]>=38:
            output.append(next_multiple)
        else :
            output.append(grades[i])
    return output
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    grades_count = int(input().strip())

    grades = []

    for _ in range(grades_count):
        grades_item = int(input().strip())
        grades.append(grades_item)

    result = gradingStudents(grades)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
