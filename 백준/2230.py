N, M = map(int, input().split())
numbers = []
for i in range(N):
    numbers.append(int(input()))
start, end, sum_ = 0, 0, 0
min_ = float("inf")
numbers = sorted(numbers)

while start < N and end < N:
    sum_ = numbers[end] - numbers[start]
    if sum_ >= M:
        min_ = min(min_, sum_)
        start += 1
    else:
        end += 1
print(min_)