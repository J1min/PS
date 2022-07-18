import sys
sys.setrecursionlimit(10**9)


def dfs(graph, v, visited):
    visited[v] = True
    print(v)
    for x in graph[v]:
        if not visited[x]:
            dfs(graph, x, visited)


N, M, R = map(int, input().split())
graph = []
visited = [0 for i in range(N)]

for _ in range(N):
    graph.append(list(map(int, input().split())))

dfs(graph, R, visited)
