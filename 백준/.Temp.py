N, M = map(int, input().split())

graph = [list(map(str, input())) for i in range(M)]
count = 0
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def dfs(x, y, color):
    global count   
    graph[x][y] = 'v'
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < M and 0 <= ny < N:
            if graph[nx][ny] != 'v' and graph[nx][ny] == color:
                count = dfs(nx, ny, color)
    return count


for i in range(N):
    for j in range(M):
        dfs(i, j, "W")
print(count)
