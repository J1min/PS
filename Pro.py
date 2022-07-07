# 좌표 압축
# N = int(input())
# result = [0] * N
# arr = list(map(int, input().split()))
# sorted_arr = sorted(arr)
# for i in range(N):
#   # if sorted_arr.index(arr[i]) not in result:
#   result[i] = sorted_arr.index(arr[i])
# print(*result)

def is_sosu(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


N = int(input())
while not is_sosu(N):
    for i in range(2, N):
        if N % i == 0:
            N //= i
            print(i)
            break
print(N)