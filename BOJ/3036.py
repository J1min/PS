import math
N = int(input())
numbers = list(map(int, input().split()))
best = numbers[0]
for i in range(1, N):
    print(f'{best // math.gcd(best, numbers[i])}/{numbers[i]//math.gcd(best, numbers[i])}')
