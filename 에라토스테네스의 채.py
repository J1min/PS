import sys

def is_sosu(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


N = int(sys.stdin.readline().rstrip())
while not is_sosu(N):
    for i in range(2, N):
        if N % i == 0:
            N //= i
            print(i)
            break
print(N)