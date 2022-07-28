import math, itertools
N = int(input())

for i in range(N):
    numbers = list(map(int, input().split()))
    M = numbers.pop(0)
    summary = 0
    for j in itertools.combinations(numbers, 2):
        summary += math.gcd(j[0], j[1])
    print(summary)
