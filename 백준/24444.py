import collections
N, M, K = map(int, input().split())
graph = [[] for _ in range(N+1)]
visited = [0] * (N+1)
for i in range(N):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def bfs(start):
    queue = collections.deque([start])
    count = 1
    visited[start] = count
    while queue:
        now = queue.popleft()
        for i in graph[now]:
            if not visited[i]:
                count += 1
                visited[i] = count
                queue.append(i)

bfs(K)
for i in range(len(visited)-1):
    print(visited[i+1])