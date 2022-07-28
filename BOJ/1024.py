N, M = map(int, input().split())
numbers = [i for i in range(N)]
result = [0]
for i in range(N):
    if sum(result) > N:
        print(-1)
    if len(result) >= M and sum(result) == N:
        print("len(result) >= M and sum(result) == N")
        print(result)
    elif sum(result) < N and len(result) > M:
        print("sum(result) < N and len(result) > M:")
        result.append(i)
        print(result)
    elif sum(result) < N and len(result) < M:
        print("sum(result) < N and len(result) < M:")
        result.append(i)
        print(result)
# print(*result)