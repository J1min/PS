N = list(map(str, input().split("-")))
numbers = []
sum_ = 0
for i in N:
    numbers.append(sum(map(int,i.split("+"))))
sum_ += numbers[0]
for i in range(1, len(numbers)):
    sum_ -= numbers[i]
print(sum_)