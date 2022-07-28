import bisect
N = int(input())
numbers = sorted(list(map(int, input().split())))
M = int(input())
request = list(map(int, input().split()))

for i in request:
    if i not in numbers:
        bisect.insort(numbers, i)
print(numbers)