# 파도반 수열
# 달팽이 느낌으로 수가 늘어나는데
# 신기함ㅋㅋ

# 점화식 
# * 초기값이 P(0) = P(1) = P(2) = 1인 정수 P(n)의 나열이다. 
# * 이후의 값은 P(n) = P(n-2) + P(n-3)으로 나타낸다.
Padovan = [0] * 101
Padovan[0], Padovan[1], Padovan[2] = 1, 1, 1
def dp(N):
    if Padovan[N] != 0:
        return Padovan[N]
    else:
        Padovan[N] = dp(N-2) + dp(N-3)
        return Padovan[N]
N = int(input())
for i in range(N):
    print(dp(int(input())-1))