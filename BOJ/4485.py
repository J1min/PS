import collections
N = int(input())


def bfs(N, graph):
    queue = collections.deque([(0, 0)])
    while queue:
        x, y = queue.popleft()
        (graph[x-1][y], graph[x+1][y], graph[x][y-1], graph[x][y+1])
        
        



while N != 0:
    graph = [list(map(int, input().split())) for _ in range(N)]
    bfs(N, graph)
    N = int(input())
