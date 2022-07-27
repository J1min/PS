N = int(input())
numbers = sorted(list(map(int, input().split())))
min_ = float("inf")
answer = []

for i in range(N-2):
    if min_ > abs(numbers[i]+numbers[i+1]+numbers[i+2]):
        min_ = abs(numbers[i]+numbers[i+1]+numbers[i+2])
        answer.append([numbers[i], numbers[i+1], numbers[i+2]])

print(*answer)
