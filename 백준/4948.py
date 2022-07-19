def sosu(N):
    prime = [False] * ((2*N)+1)
    for i in range(2, int(2*N)+1):
        if prime[i] == False:
            for j in range(i+i, (2*N), i):
                prime[j] = True
    return [i for i in range(N+1, (2*N)) if prime[i] == False]

N = int(input())
while N != 0:
    if N == 1:
        print(1)
    else:
        print(len(sosu(N)))
    N = int(input())