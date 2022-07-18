import sys
N, M = map(int, sys.stdin.readline().split())
arr = [0] * (M+1)
sum_ = 0
N %= (9000000000000000000)
M %= (9000000000000000000)
arr[1], arr[2] = 1, 1
for i in range(3, M+1):
    arr[i] = arr[i-1] + arr[i-2]
for i in range(N, M+1):
    sum_ += arr[i] % 9000000000000000000
print(sum_)