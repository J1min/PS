n = int(input())
arr = []
for i in range(n):
    arr.append(list(map(int, input().split())))
arr = sorted(arr)
for i in arr:
  print(i[0], i[1])