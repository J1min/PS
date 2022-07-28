def dfs(x, y):
    global count
    if x-1 < 0 and y-1 < 0:
        return False
    dfs(x+1,y)
    dfs(x-1,y)
    dfs(x,y+1)
    dfs(x,y-1)
    


N ,M = map(int, input().split())
count = 0

graph = [[]*(N+1) for _ in range(N+1)]
visited = [0] * (N+1)

for i in range(N):
    graph[i] = list(input())

dfs(1)
print(count)
