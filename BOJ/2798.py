def utensil(N, M):
    prime = [False] * (M+1)
    for i in range(2, int(M**0.5)+1):
        if prime[i] == False:
            for j in range(i+i, M+1, i):
                prime[j] = True
    if N == 1:
        N += 1
    answer = [i for i in range(N, M+1) if prime[i] == False]
    if len(answer) == 0:
        return [-1]
    return answer
N = int(input())
M = int(input())
if sum(utensil(N, M)) == -1:
    print(-1)
else:
    print(sum(utensil(N, M)))
    print(min(utensil(N, M)))