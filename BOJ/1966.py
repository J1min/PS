T = int(input())
for i in range(T):
    N, M = map(int, input().split())
    numbers = list(map(int, input().split()))
    s_numbers = sorted(numbers, reverse=True)
    numbers[M] = 'v'
    s_numbers[M] = 'v'

    while numbers != s_numbers:
        numbers.append(numbers.pop(0))
    print(numbers)

    # print("index", s_numbers.index(specific)+1)
    # print("count", numbers.count(specific)-1)
