N, M, K = map(int, input().split())
number = sorted(list(map(int, input().split())))
summary = 0
for i in range(1, M+1):
    if i % K == 0:
        summary += number[-2]
    else:
        summary += number[-1]
print(summary)
