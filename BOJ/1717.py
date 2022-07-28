# 유니온 파인드 문제임 
# 근데 그거 코테에 안나오지 않나
# 그래서 할 의욕이 없어짐

N, M = map(int, input().split())
sets = [[i] for i in range(1, N+1)]

for i in range(M):
    xSet, ySet = [], []
    order, x, y = map(int, input().split())

    if order == 0:
        for j in range(len(sets)):
            if xSet != [] and ySet != []:
                break
            if x in sets[j]:
                xSet = sets[j]
            if y in sets[j]:
                ySet = sets[j]

    elif order == 1:
        flag = 0
        for j in range(len(sets)):
            if x in sets[j] and y in sets[j]:
                flag = 1
                break
        print(["NO", "YES"][flag])
