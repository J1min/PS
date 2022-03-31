n = int(input())
ok = 0
for i in range(n):
    arr = list(map(int, input().split()))
    cnt = arr[0]
    arr.pop(0)
    avg = sum(arr, 0) / len(arr)
    for i in arr:
        if(i > avg):
            ok += 1
    print("{:.3f}%".format((ok/(len(arr)))*100))
    ok = 0
    arr = []
