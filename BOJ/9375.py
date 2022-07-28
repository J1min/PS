import math
N = int(input())

for i in range(N):
    M = int(input())
    fashion = {}
    summary = 1
    for j in range(M):
        piece, kind = map(str, input().split())
        try:
            fashion[kind] += 1
        except:
            fashion[kind] = 1
        for i in fashion.values():
            summary *= (i+1)
        print(summary-1)
