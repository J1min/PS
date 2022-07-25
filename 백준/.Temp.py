# 다른 배열 (DP 테이블)을 이용해서
# 뭔가 하면 될 것 같지만 
# 구현 방식이 감이 도저히 안잡힘

# N = int(input())
# numbers = list(map(int, input().split()))
# count = [0] * N

# for i in range(N):
#     if now < numbers[i]:
#         now = numbers[i]
#         count[i] = 1

n = int(input())
a = list(map(int, input().split()))
dp = [0 for i in range(n)]
for i in range(n):
    for j in range(i):
        if a[i] > a[j] and dp[i] < dp[j]:
            dp[i] = dp[j]
    dp[i] += 1
print(dp)