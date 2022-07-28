N = int(input())
numbers = []
for i in range(N):
    q = int(input())
    if q == 0:
        numbers.pop()
    else:
        numbers.append(q)
print(sum(numbers))