# A = [3, 5, 2, 7]인 경우 NGE(1) = 5, NGE(2) = 7, NGE(3) = 7, NGE(4) = -1이다. 
# A = [9, 5, 4, 8]인 경우에는 NGE(1) = -1, NGE(2) = 8, NGE(3) = 8, NGE(4) = -1이다.

N = int(input())
numbers = list(map(int, input().split()))
for i in range(1, N):
    now = numbers[i:]
    # print(numbers[i-1], now)
    for j in now:
        flag = False
        if j > numbers[i-1]:
            print(j, end=' ')
            flag = True
            continue
    if not flag:
        print(-1, end=' ')
print(-1)