# 좌표 압축
# N = int(input())
# result = [0] * N
# arr = list(map(int, input().split()))
# sorted_arr = sorted(arr)
# for i in range(N):
#   # if sorted_arr.index(arr[i]) not in result:
#   result[i] = sorted_arr.index(arr[i])
# print(*result)

def sosu(n):
    prime = [True] * n
    for i in range(2, int(n**0.5)):
        if prime[i] == True:
            for j in range(i+i, n, i):
                prime[j] = False
    return [i for i in range(2, n) if prime[i] == True]

N = int(input())
sosulist = sosu(N)

while True:
    if N in sosulist:
        break
    for i in sosulist:
        if N % i == 0:
            N //= i
            print(i)
            break
print(N)