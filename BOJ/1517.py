N = int(input())
numbers = list(map(int, input().split()))
stop = int(input())
i = 0
while stop > 0 and i < 0:
    if numbers[i+1] > numbers[i]:
        numbers[i], numbers[i+1] = numbers[i+1], numbers[i]
        stop -= 1
    i += 1

print(*numbers)
