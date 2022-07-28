M, N = map(int, input().split())
graph = [list(input()) for _ in range(N)]
count = 0

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def dfs(x, y, color):
    global count
    if graph[x][y] == color:
        count += 1
        graph[x][y] = 'v'
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if 0 <= nx < N and 0 <= ny < M:
                dfs(nx, ny, color)
        return True
    return False


white, blue = 0, 0

for i in range(N):
    for j in range(M):
        if dfs(i, j, "W"):
            white += count**2
            count = 0

for i in range(N):
    for j in range(M):
        if dfs(i, j, "B"):
            blue += count**2
            count = 0

print(white, blue)
