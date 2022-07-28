import collections

N, M, K = map(int, input().split())
graph = [[] for _ in range(N+1)]
visited = [0] * (N+1)
count = 1

for i in range(M):
    A, B = map(int, input().split())
    graph[A].append(B)
    graph[B].append(A)

for i in range(N+1):
    graph[i].sort(reverse=True)


def bfs(start):
    global count
    queue = collections.deque([start])
    visited[start] = 1
    while queue:
        now = queue.popleft()
        for i in graph[now]:
            if visited[i] == 0:
                count += 1
                visited[i] = count
                queue.append(i)


bfs(K)

for i in range(1, N+1):
    print(visited[i])
