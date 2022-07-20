from collections import deque
N, M = map(int, input().split())
visited = [False] * (N+1)
graph = [[] for _ in range(N+1)]

count = 0

for i in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(b)

for i in range(len(graph)):
    graph[i].sort()

def bfs(start):
    global count
    queue = deque([start])
    visited[start] = True
    time += 1
    while queue:
        now = queue.popleft()
        print(now, end=' ')
        for x in graph[now]:
            if not visited[x]:
                queue.append(x)
                count += 1
                visited[x] = True

bfs(1)
print()
print(count)