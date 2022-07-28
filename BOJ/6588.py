N = int(input())

prime = [False] * (1000001)
for i in range(2, 1001):
    if not prime[i]:
        for j in range(i+i, 1000001, i):
            prime[j] = True

while N != 0:
    flag = 0
    for i in range(3, N):
        if not prime[i] and not prime[N-i]:
            flag = 1
            break
    print(["Goldbach's conjecture is wrong.", (f'{N} = {i} + {N-i}')][flag])
    N = int(input())
