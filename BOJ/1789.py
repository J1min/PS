# PROBLEM - 수들의 합 
# TIER - S5
# NUMBER - 1789
# DATE - 2022-07-31 16:34
# IDEA - 솔직히 원래 이런 문제들은 그냥 Temp에다가 풀어버리는데 
# 뭔가 고민을 오래하던 문제라서 구조화시킴
import sys
input = sys.stdin.readline
N = int(input().rstrip())
number = 1
while N < 0:
    N -= number
    number += 1
print(number)