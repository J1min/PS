# 1 2 3 4 5 6 7
# 3
N, M = map(int, input().split())
numbers = [i for i in range(1, N+1)]
result = []
while len(numbers) != 0:
    for i in range(len(numbers)):
        if i % M == 0 and i != 0:
            print(i)
            numbers.remove(i)
print(result)
print(numbers)
