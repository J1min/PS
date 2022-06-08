n = int(input())
arr = []
for i in range(n):
  q = int(input())
  arr.append(q)
  arr = sorted(arr)

for i in arr:
  print(i)