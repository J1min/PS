N = int(input())
numbers = sorted(list(map(int, input().split())))
sum_ = 0
for i in range(N):
    sum_ += sum(numbers[0:i+1])
print(sum_)
