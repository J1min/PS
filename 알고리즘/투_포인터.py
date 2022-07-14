N = int(input())
numbers = list(map(int, input().split()))
target = int(input())

now = 0

start = 0
end = 1

while now != target:
    now = sum(numbers[start:end])
    if target < now:
        start += 1
    elif target > now:
        end += 1
    print(now)
    print(numbers[start: end])
    