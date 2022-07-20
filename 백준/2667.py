N = int(input())

graph = [list(map(int, input())) for _ in range(N)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

count = 0

def dfs(x, y):
    global count
    if graph[x][y] == 1:
        graph[x][y] = 0
        count += 1
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if 0 <= nx < N and 0 <= ny < N:
                dfs(nx, ny)
        return True
numbers = []
for i in range(N):
    for j in range(N):
        if dfs(i, j):
            numbers.append(count)
            count = 0

numbers.sort()
print(len(numbers))
for i in numbers:
    print(i)