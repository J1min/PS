import itertools

def sosu(N): # 소수판별 함수
    for i in range(2, N):
        if N % i == 0:
            return False
    return True

N, M = map(int, input().split())
weights = list(map(int, input().split()))
answer = []

for i in itertools.combinations(weights, M): # 조합 사용해서 모든 경우의 수 검토
    if sosu(sum(i)) == True and sum(i) not in answer: # 몸무게가 소수이며, 소수인 몸무게 조합들이 겹치지 않게
        answer.append(sum(i))

print(*answer) # unpacking 사용해서 깔끔하게 출력하기