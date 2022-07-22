import collections
N, M, K = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(M)]
zc = 0
for i in range(M):
    for j in range(N):
        if graph[i][j] == 0:
            zc += 1

flag = 0


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

start = []

queue = collections.deque()

for i in range(M):
    for j in range(N):
        if graph[i][j] == 1:
            queue.append((i, j))

def bfs():
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if 0 <= nx < M and 0 <= ny < N and graph[nx][ny] == 0:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))

bfs()
max_ = float("-inf")
if zc == 0:
    flag = 2
else:
    for i in range(M):
        for j in range(N):
            if graph[i][j] == 0:
                flag = 1
                break
            else:
                max_ = max(graph[i][j], max_)

print([max_-1, -1, 0][flag])