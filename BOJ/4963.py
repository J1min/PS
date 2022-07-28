import collections
dx = [1, 1, -1, -1, 1, -1, 0, 0]
dy = [0, 1, 0, 1, -1, -1, 1, -1]
def bfs(x, y):
    queue = collections.deque([(x, y)])
    while queue:
        x, y = queue.popleft()
        for i in range(8):
            nx, ny = x+dx[i], y+dy[i]
            if 0 <= nx < M and 0 <= ny < N and graph[nx][ny] == 1:
                graph[nx][ny] = 0
                queue.append((nx, ny))
N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(M)]
while N != 0:
    count = 0
    for x in range(M):
        for y in range(N):
            if graph[x][y] == 1:
                bfs(x, y)
                count += 1
    print(count)
    N, M = map(int, input().split())
    graph = [list(map(int, input().split())) for _ in range(M)]