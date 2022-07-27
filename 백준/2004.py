import math
n, r = map(int, input().split())
def nCr(n, r):
    return str(math.factorial(n) // (math.factorial(r) * math.factorial(n-r)))[::-1]
count = 0
for i in nCr(n, r):
    if i == '0':
        count += 1
    else:
        print(count)
        break