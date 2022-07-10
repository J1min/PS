import sys
input = lambda: sys.stdin.readline().rstrip()

for _ in range(int(input())) :
    n = int(input())
    a = list(map(int, input().split()))

    l, flag = -1, 1
    
    for x in a :
        x = min(x, n-x+1)
        if x < l : x = n-x+1
        if x < l : flag = 0
        l = x
    print(["NO", "YES"][flag])