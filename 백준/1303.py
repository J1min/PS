N, M = map(int, input().split())

graph = [list(map(str, input())) for i in range(M)]
count = 0
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]


def dfs(x, y, color):
    global count
    if graph[x][y] == color:
        graph[x][y] = 'v'
        count += 1
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < N:
                if graph[nx][ny] != 'v' and graph[nx][ny] == color:
                    dfs(nx, ny, color)
        return True


white = 0
blue = 0

for i in range(M):
    for j in range(N):
        if dfs(i, j, "W"):
            white += count**2
            count = 0
for i in range(M):
    for j in range(N):
        if dfs(i, j, "B"):
            blue += count**2
            count = 0
print(white, blue)
