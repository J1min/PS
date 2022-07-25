N, M = map(int, input().split())
hear = []
see = []
for i in range(N):
    hear.append(input())
for i in range(M):
    see.append(input())
hear = set(hear)
see = set(see)
answer = list(hear & see)
answer.sort()
for i in answer:
    print(i)