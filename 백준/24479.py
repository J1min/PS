import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N, M, K = map(int, input().split())
graph = [[] for _ in range(N+1)]
visited = [0] * (N+1)
count = 1

for i in range(M):
    A, B = map(int, input().split())
    graph[A].append(B)
    graph[B].append(A)


def dfs(start):
    global count
    visited[start] = count
    graph[start].sort(reverse=True)
    for i in graph[start]:
        if visited[i] == 0:
            count += 1
            dfs(i)


dfs(K)

for i in range(1, N + 1):
    print(visited[i])