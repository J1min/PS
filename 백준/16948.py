import collections
N = int(input())
startX, startY, targetX, targetY = map(int, input().split())
dx = [-2, -2, 0, 0, 2, 2]
dy = [-1, +1, -2, +2, -1, +1]
graph = [[-1] * N for _ in range(N)]

def bfs(startX, startY):
    queue = collections.deque([(startX, startY)])
    graph[startX][startY] = 0
    while queue:
        x, y = queue.popleft()
        count += 1
        for i in range(6):
            nx, ny = x+dx[i], y+dy[i]
            if 0 <= nx <= N and 0 <= ny < N and graph[nx][ny] == -1:
                queue.append((nx, ny))
                graph[nx][ny] = graph[x][y] + 1


bfs(startX, startY)

print(graph[targetX][targetY])
