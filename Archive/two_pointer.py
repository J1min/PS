n, m = map(int, input().split())
summary, end, count = 0, 0, 0

for start in range(n):
    while summary < m and end < n:
        summary += data[end]
        end += 1
    if summary == m:
        count += 1
    summary -= data[start]
print(count)

