N = int(input())
_ = input()
for i in range(N):
    sum_ = 0
    M = int(input())
    for j in range(M):
        sum_ += int(input())
    if sum_ // N == M :
        print("YES")
    else:
        print("NO")