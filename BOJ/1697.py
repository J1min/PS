import sys
# PROBLEM - 숨바꼭질 
# TIER - S1
# NUMBER - 1697
# DATE - 2022-07-29 16:44
# IDEA - 그래프 BFS 문제인데 그거 안쓰고 바텀업으로 함풀어봄 ㄱㄷ

N, M = map(int, input().split())
count = 0
while True:
    if M == N:
        print(count-1)
        break
    if (M/2) % 1 == 0.0 and M/2 > N:
        M //= 2
        count += 1
    else:
        M -= 1
        count += 1