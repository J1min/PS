fibo = [0] * 100
fibo[0], fibo[1], fibo[2] = 0, 1, 1
N = int(input())
c1, c2 = 0, 0


def f(N):
    global c1
    if N == 1 or N == 2:
        c1 += 1
        return 1
    else:
        return f(N-1) + f(N-2)


def 디피보나치(N):
    global c2
    
    if fibo[N] != 0:
        return fibo[N]
    else:
        c2 += 1
        fibo[N] = 디피보나치(N-1) + 디피보나치(N-2)
        return fibo[N]


f(N)
디피보나치(N)
print(c1, c2)
