# 좌표 압축
N = int(input())
result = [0] * N
arr = list(map(int, input().split()))
sorted_arr = sorted(arr)
for i in range(N):
  # if sorted_arr.index(arr[i]) not in result:
  result[i] = sorted_arr.index(arr[i])
print(*result)