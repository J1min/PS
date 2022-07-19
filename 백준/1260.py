import sys
sys.setrecursionlimit(10**9) 
N, M, K = map(int, input().split())
graph = [[]*N for _ in range(N+1)]
visited = [False] * N

def dfs(v):
    visited[v] = True
    print(v, end=" ")
    for x in graph[v]:
        if visited[x] == False:
            dfs(x)
for i in range(N):
    for j in range(N):
        graph[i].append(j)
        graph[j].append(i)
dfs(1)