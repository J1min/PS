N, M, K = map(int, input().split())
graph = [[] for _ in range(N+1)]
visited = [0] * (N+1)
for i in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
result = []

count = 0
# [0, 2, 3, 4, 1, 0]
def dfs(start):
    global count
    result.append(start)
    visited[start] = count
    for v in graph[start]:
        if not visited[v]:
            count += 1
            dfs(v)

dfs(K)
visited = visited[::-1]
for i in range(1, M+1):
    print(visited[i])