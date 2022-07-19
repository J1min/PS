import itertools


def sosu(N):
    prime = [False] * N
    for i in range(2, N):
        if prime[i] == False:
            for j in range(i+i, N, i):
                prime[j] = True
    return [i for i in range(2, N) if prime[i] == False]


N = int(input())
for i in range(N):
    result = []
    target = int(input())
    sosuList = sosu(target)
    for i in itertools.permutations(sosuList, 2):
        if sum(i) == target:
            result.append(list(i))
    for j in sosuList:
        if j*2 == target:
            print(j, j)
            break
    else:
        result = sorted(result, key=lambda x: abs(x[0] - x[1]))
        print(*result[0])
