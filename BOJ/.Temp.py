import itertools
temp = list(map(int, input().split()))
numbers = temp[1:]
N = temp[0]
while temp[0] != 0:
    numbers = temp[1:]
    N = temp[0]

    for i in itertools.combinations(numbers, 6):
        print(*i)
    print()
    temp = list(map(int, input().split()))
    