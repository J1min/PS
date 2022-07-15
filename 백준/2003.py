N, M = map(int, input().split())
numbers = list()
count = 0
start, end = 0, 1
while True:
    sum_ = sum(numbers[start:end])
    if sum_ == M:
        count += 1
    else:
        if sum_ > M:
            start += 1
        elif sum_ < M:
            end += 1
print(count)