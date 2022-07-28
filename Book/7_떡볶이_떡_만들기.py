import sys
input = sys.stdin.readline

N, request = map(int, input().split())
rice_cake = list(map(int, input().split()))
success = 0
start, end = 0, max(rice_cake)

while start <= end:
    mid = (start+end) // 2
    cutted = 0

    for i in rice_cake:
        if i > mid:
            cutted += (i - mid)

    if cutted < request:
        end = mid-1
    else:
        success = mid
        start = mid+1
 
print(success)
