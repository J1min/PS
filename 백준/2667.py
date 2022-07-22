N = int(input())
graph = [list(map(int, input())) for _ in range(N)]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

count = 0

def dfs(x, y):
    global count
    if graph[x][y] == 1: # 만약 있다면 
        graph[x][y] = 0 # 없어져라 
        count += 1 # 카운트 해주고 
        for i in range(4): # 4방향 전진
            nx, ny = x+dx[i], y+dy[i]
            if 0 <= nx < N and 0 <= ny < N:
                dfs(nx, ny)
        return True # 그리고 전진끝나면 (갈데없으면) True 리턴 
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