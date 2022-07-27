N = int(input())
numbers = list(map(int, input().split()))
stop = int(input())

for i in range(N):
    for j in range(i):
        if numbers[i] > numbers[j] and stop > 0:
            numbers[i], numbers[j] = numbers[j], numbers[i]
            stop -= 1

print(*numbers)
