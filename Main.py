n = int(input())
arr = list(map(int, input().split()))
arr = sorted(arr)
for i in arr:
  print(i, end=" ")