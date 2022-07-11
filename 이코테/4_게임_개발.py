def check(X, Y, direction):
    global count
    if direction == 0:  # 북
        # 서 남 동 북
        if Map[X][Y-1] == 0:  # 서
            Y = Y-1
            Map[X][Y] = 2
            count += 1
            direction = 3
        if Map[X+1][Y] == 0:  # 남
            X = X+1
            Map[X][Y] = 2
            count += 1
            direction = 2
        if Map[X][Y+1] == 0:  # 동
            Map[X][Y-1] = 2
            count += 1
            direction = 1
        if Map[X-1][Y] == 0:  # 북
            Map[X][Y-1] = 2
            count += 1
            direction = 0
    elif direction == 1:  # 동
        # 북 서 남 동
        print(Map[X-1][Y])  # 북
        print(Map[X][Y-1])  # 서
        print(Map[X+1][Y])  # 남
        print(Map[X][Y+1])  # 동
    elif direction == 2:  # 남
        # 동 북 서 남
        print(Map[X][Y+1])  # 동
        print(Map[X-1][Y])  # 북
        print(Map[X][Y-1])  # 서
        print(Map[X+1][Y])  # 남
    elif direction == 3:  # 서
        # 남 동 북 서
        print(Map[X+1][Y])  # 남
        print(Map[X][Y+1])  # 동
        print(Map[X-1][Y])  # 북
        print(Map[X][Y-1])  # 서


N, M = map(int, input().split())
X, Y, direction = map(int, input().split())
Map = []
count = 0
for i in range(N):
    Map.append(list(map(int, input().split())))

check(X, Y, direction)
