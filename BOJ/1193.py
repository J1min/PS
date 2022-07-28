# PROBLEM - 분수찾기
# NUMBER - 1193
# DATE - 2022-07-27 23:15
# IDEA - 짝, 홀에 따라서 문제가 주어지는 패턴이 다름,
# N 입력 받아서 짝 홀 구별하고 그 범위에 맞는 값 뽑아주자.

N = int(input())
line = 1

while N > line:  # 몇번줄인지 구해주고
    N -= line
    line += 1

if line % 2 == 0:  # 짝수라인 홀수라인 각각 다른 솔루션 도입
    a = N
    b = line-N+1
else:
    a = line-N+1
    b = N
print(f'{a}/{b}')
