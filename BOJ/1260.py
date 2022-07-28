import sys
from collections import deque
input = sys.stdin.readline

n, m, start = map(int, input().split())
visited = [False]*(n+1)
graph = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(len(graph)):
    graph[i].sort()

def dfs(start):
    visited[start] = True
    print(start, end=" ")
    for i in graph[start]:
        if not visited[i]:
            dfs(i)
            
def bfs(start):
    queue = deque([start])
    visited[start] = True
    while queue:
        now = queue.popleft()
        print(now, end=" ")
        for i in graph[now]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True
dfs(start)
print()
visited = [False]*(n+1)
bfs(start)