# [1, 2, 3, 5, 7, 9, 10, 11, 12]
N = int(input())
numbers = sorted(list(map(int, input().split())))
target = int(input())

start, end, count = 0, N-1, 0
# print(numbers)
while start < end: # 투포인터 탐색 ㄱㄱ
    sum_ = numbers[start] + numbers[end]
    if sum_ < target:
        start += 1
    elif sum_ == target:
        count += 1
        end -= 1
    else:
        end -= 1
print(count)