N = int(input())
arr = []
for i in range(N):
  arr.append(list(map(int, input().split())))
arr = sorted(arr)
arr = sorted(arr, key=lambda x: x[1]-x[0])
print(arr)