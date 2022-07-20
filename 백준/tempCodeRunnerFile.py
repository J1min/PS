import sys
sys.setrecursionlimit(10**9)
N = int(input())
graph = []
visited = [[False] * N for _ in range(N)]
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

count = 0

for _ in range(N):
    graph.append(list(map(int, input())))


def dfs(x, y):
    global count
    if x < 0 or x >= N or y < 0 or y >= N:
        return False
    if graph[x][y] == 1:
        count += 1
        graph[x][y] = 0
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            dfs(nx, ny)
        return True
    return False


numbers = []

for i in range(N):
    for j in range(N):
        if dfs(i, j) == True:
            numbers.append(count)
            count = 0
print(len(numbers))
for i in numbers:
    print(i)