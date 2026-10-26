r"""Problem    : Solve Me First
Difficulty : Easy
Domain     : Algorithms > Warmup
URL        : https://www.hackerrank.com/challenges/solve-me-first/problem

Description
-----------
Complete the function $solveMeFirst$ to compute the sum of two integers.

**Example**
$a = 7$
$b = 3$

Return $10$.

**Function Description**

Complete the $solveMeFirst$ function with the following parameters:

- $int\ a$: the first value
- $int\ b$: the second value

Returns
- $int$: the sum of $a$ and $b$

Constraints
-----------
$1 \le a, b \le 1000$

Sample Input
------------
a = 2
b = 3

Sample Output
-------------
5
"""

# ============================================================
# Solution
# ============================================================



def solveMeFirst(a,b):
	# Hint: Type return a+b below
    return a+b


num1 = int(input())
num2 = int(input())
res = solveMeFirst(num1,num2)
print(res)
