import math
n = int(input())

# 1	1	6 14
# 2	2	7 21
# 3	4	8 22
# 4	11	9 24
# 5	12	10 41

n10 = n % 100
n1 = n % 10

n10 /= 3
n1 %= 3

n10 = math.floor(n10)
n1 = math.floor(n1)


if n1 == 0:
    n1 = 1

if n10 >= 2 & n1 == 4:
    n10 -= 1
    n1 = 3

if n10 % 3 == 0:
    n10 -= 1
    

print(n10, n1, end="")
