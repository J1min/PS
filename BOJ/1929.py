N, M = map(int, input().split())

def f(M,N):
    sosu = [True] * (N+1)
    for i in range(2,int(N**0.5)+2):
        if sosu[i] == True:
            for j in range(i+i, N+1, i):
                sosu[j] = False
    return [i for i in range(M, N+1) if sosu[i] == True and i != 1]

for i in f(N, M):
    print(i)