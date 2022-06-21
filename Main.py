import sys
input = sys.stdin.readline
arr = []
n = int(input().strip())
for i in range(n):
    q = input().strip()
    if q not in arr:
        arr.append(q)
arr = sorted(arr)
print(arr)
arr = sorted(arr, key=len)
print(arr)
# for i in arr:
#     print(i)