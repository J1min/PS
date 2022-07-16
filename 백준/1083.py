N = int(input())
numbers = list(map(int, input().split()))
S = int(input())
count = 0

for i in range(N):
    for j in range(N):
        if numbers[i] > numbers[j] and S != 1:
            numbers[i], numbers[j] = numbers[j],numbers[i]
            S -= 1
        else:
            break
print(*numbers)