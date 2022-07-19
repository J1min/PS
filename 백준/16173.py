def dfs(step, x, y):
    dfs(x+step, y)
    dfs(x, y+step)

N = int(input())
graph = [[]]
for i in range(N):
    graph.append(list(map(int, input().split())))


dfs(graph[0][0], 0, 0)