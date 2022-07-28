import collections
N, M = map(int, input().split())
graph = [list(map(int, input())) for _ in range(M)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

queue = collections.deque([(0, 0)])
while queue:
    x, y = queue.popleft()
    for i in range(4):
        nx, ny = x+dx[i], y+dy[i]
        if 0 <= nx < M and 0 <= ny < N:
            if graph[nx][ny] == 0:
                graph[nx][ny] = 'v'
                queue.append((nx, ny))
            else:
                graph[nx][ny] = 'c'
                queue.append((nx, ny))

print(graph)
