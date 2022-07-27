import itertools
N = int(input())


def utensil(N, M):
    prime = [False] * (M+1)
    for i in range(2, M):
        if prime[i] == False:
            for j in range(i+i, M, i):
                prime[j] = True
    return [i for i in range(N, M) if prime[i] == False]


while N != 0:
    numbers = utensil(2, N)
    answer = []
    for i in itertools.combinations(numbers, 2):
        if sum(i) == N:
            answer.append((i[0], i[1]))
    answer = sorted(answer, key=lambda number: number[1]-number[0])
    if len(answer) == 0:
        print("Goldbach's conjecture is wrong.")
    else:
        print(f'{N} = {answer[-1][0]} + {answer[-1][1]}')
    N = int(input())
