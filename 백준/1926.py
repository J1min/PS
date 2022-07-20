import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)
N, M = map(int, input().split())
graph = []
visited = [[False] * N for _ in range(M)]
count = 0
for i in range(N):
    graph.append(list(map(int, input().split())))


def dfs(x, y):
    if x <= -1 and x >= N and y <= -1 and y >= N:
        return False
    else:
        # visited[x][y] = True
        dfs(x-1, y)
        dfs(x+1, y)
        dfs(x, y-1)
        dfs(x, y+1)
        return True
    return False


for i in range(N):
    for j in range(M):
        if dfs(i, j) == True:
            count += 1

print(count)