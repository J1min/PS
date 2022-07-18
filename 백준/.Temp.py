N, M = map(int, input().split())
while N != 0:
    if M < N and N % M == 0: print('multiple')
    elif M > N and M % N == 0: print('factor')
    else: print('neither')
    N, M = map(int, input().split())
