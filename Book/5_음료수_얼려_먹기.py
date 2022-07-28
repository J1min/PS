import collections
N, M = map(int, input().split())
graph = [list(map(int, input())) for _ in range(N)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

count = 0


def bfs(x, y):
    queue = collections.deque([(x, y)])
    if graph[x][y] == 1:
        return False
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if 0 <= nx < N and 0 <= ny < M:
                if graph[nx][ny] == 0:
                    graph[nx][ny] = 1
                    queue.append((nx, ny))
    return True


for i in range(N):
    for j in range(M):
        if bfs(i, j):
            count += 1
print(count)
