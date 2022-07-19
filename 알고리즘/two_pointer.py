n, m = map(int, input().split())
sum_, end, count = 0, 0, 0

for start in range(n):
    while sum_ < m and end < n:
        sum_ += data[end]
        end += 1
    if sum_ == m:
        count += 1
    sum_ -= data[start]
print(count)

