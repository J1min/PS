def dfs(x, y, shape):
    if shape == "-" and x+1 < M:
        dfs(x+1, y, shape)
        return True
    elif shape == "|" and y+1 < N:
        dfs(x, y+1, shape)
        return True
    return False
N, M = map(int, input().split())
graph = [list(input()) for _ in range(N)]
count = 0

for x in range(M):
    for y in range(N):
        if not dfs(x, y, "-"):
            count += 1
for x in range(M):
    for y in range(N):
        if not dfs(x, y, "|"):
            count += 1
print(count)