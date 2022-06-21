n, m = map(int, input().split())
arr = list(map(int, input().split()))
sum1 = 0
min1 = []
arr2 = []
for i in range(n):
    for j in range(i+1, n):
        for k in range(j+1, n):
            if n > (i + j + k):
                min1.append(m-(arr[i] + arr[j] + arr[k]))
print(min(min1))
