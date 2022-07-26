import sys
input = sys.stdin.readline
N, M, K = map(int, input().split())
score = [0] * N
summary = 0

for i in range(N):
    score[i] = (tuple(map(int, input().split())))

special = set(score)  # 특별상 받을 리스트
bone = set(score)  # 본상 받을 리스트
special = list(special) #
bone = list(bone) #

# special = list(set([tuple((award)) for award in special]))
# bone = list(set([tuple((award)) for award in bone]))

special = sorted(special, key=lambda x: x[0], reverse=True)  # 특별상 받을 리스트
special = special[:M]

bone = set(bone)-set(special)
bone = sorted(bone, key=lambda x: x[1], reverse=True)  # 본상 받을 리스트
bone = list(bone)[:K]

answer = special + bone  # 정해진 인원수만큼 자르고 합침

for i in answer:
    summary += i[0]  # 심판이 준 점수만 추가
print(summary)
