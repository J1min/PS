N = int(input())
number = [i for i in range(1, N+1)]
print(number[0], end=" ")
while len(number) != 1:
    number.pop(0)
    number.append(number.pop(0))
    print(number[0], end=" ")