def dfs(x, y):
    # 벽을 만나면 False 반환
    if x < -1 or x > N-1 or y < -1 or y > M-1:
        return False
    # 현재 index가 이미 방문했던 곳이라면 False 반환
    if visited[x][y] == True:
        return False
    # 현재 위치 방문 처리
    visited[x][y] = True
    # 현재 index의 모양이 '-'라면
    if graph[x][y] == '-' and (y == M-1 or graph[x][y+1] == '-'):
        dfs(x, y+1) # 오른쪽으로 이동하고
    elif graph[x][y] == '|' and (x == N-1 or graph[x+1][y] == '|'):
        dfs(x+1, y) # 아래쪽으로 이동
    return True

N, M = map(int, input().split())
graph = []
for _ in range(N):
    graph.append(list(input()))

visited = [[False]*M for _ in range(N)]

count = 0
for x in range(N):
    for y in range(M):
        if dfs(x, y) == True:
            count += 1
            
print(count)