def sosu(n):
    prime = [True] * n
    for i in range(2, int(n**0.5)):
        if prime[i] == True:
            for j in range(i+i, n, i):
                prime[j] = False
    return [i for i in range(2, n) if prime[i] == True]


def is_sosu(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


N = int(input())
sosulist = sosu(int(N**0.5))

if is_sosu(N) == True:
    print(N)

else:
    while N != 1:
        for i in range(2, N):
            if N % i == 0:
                N //= i
                print(i)
                break
print(N)
