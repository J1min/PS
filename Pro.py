import itertools
import math
n, k = map(int, input().split())
if n == k or k == 0:
    print(1)
else:
    print(math.factorial(n) // (math.factorial(k) * math.factorial(n-k)))

