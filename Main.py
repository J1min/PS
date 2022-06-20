n = int(input())
a = []
for i in range(n):
    a.append(int(input()))
dp = [0 for i in range(n)]

for i in range(n):
    for j in range(i):
        if a[i] > a[j] and dp[i] < dp[j]:
            dp[i] = dp[j]
    dp[i] += 1
print(n - max(dp)) # 줄 세우기
print(max(dp)) # 증가하는 부분 수열  
