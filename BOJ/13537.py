# 이 멋진 수열에 쿼리를! << 이거 얻고싶어서 깝치던건데 도저히 못하겟다
# 개빡.

N = int(input()) 
numbers = list(map(int, input().split()))
M = int(input())
for i in range(M):
    i, j, k = map(int, input().split())
    count = 0
    for j in numbers[i-1:j]:
        if j > k:
            count += 1
    print(count)
