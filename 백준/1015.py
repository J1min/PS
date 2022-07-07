# 기타줄 문제 (그리디 알고리즘)

N, M = map(int, input().split())
arr = []
oneList = []  # 줄 1개 살때의 돈
sixList = []  # 줄 6개 살떄의 돈
money = 0
for i in range(M):
    arr.append(list(map(int, input().split())))  # 입력 쭈루룩 받고

for i in arr:
    sixList.append(i[0])
for i in arr:
    oneList.append(i[1])  # 초기설정 완료

while N >= 1:  # N이 1 이상일 때
    if N >= 6:  # 필요한 줄이 6개 이상
        if min(sixList) < min(oneList) * 6:  # 만약 6개세트를 사는게 1개짜리 6개를 사는것보다 이득이면
            N -= 6  # 6개를 사야죠 뭐
            money += min(sixList)
        else:
            N -= 1  # 근데 1개 사는게 이득일수도 있잖아요
            money += min(oneList)  # 그럼 1개 사는거죠
    else:  # 줄이 5개 이하 필요할때는요
        if min(sixList) < min(oneList) * N:  # 1개씩 N개를 사는거 VS 6개셋 사는거 비교해요
            N -= 6  # 6개셋이 싸다면
            money += min(sixList)  # 그걸 사요
        else:  # 근데 1개 * N개를 산다면
            N -= 1
            money += min(oneList)  # 1개씩 사겠쥬

print(money)  # 최종가격이에요
