N, M = map(int, input().split())
graph = [list(map(str, input())) for _ in range(N)]
count = 0

for i in range(N):
    before = "이잉"
    for j in range(M):
        if graph[i][j] != before:
            before = graph[i][j]
            count += 1

print(count)