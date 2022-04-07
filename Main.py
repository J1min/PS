num = int(input())

arr = list(map(int, input().split()))
newarr = []
M = max(arr)


for i in arr:
    q = i/M*100
    newarr.append(q)
avg = sum(arr) / len(arr)
