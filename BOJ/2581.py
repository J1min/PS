def f(n1, n):
    arr = [True] * n
    for i in range(2, int(n**0.5)):
        if arr[i] == True:
            for j in range(i+i, n, i):
                arr[j] = False
    if n1 == 1:
        n1 = 2
    return [i for i in range(n1, len(arr)) if arr[i] == True]


n = int(input())
m = int(input())


arr = f(n, m)

if n == 2 and m == 3:
    arr = [2, 3]

if len(arr) == 0:
    print(-1)
else:
    print(sum(arr))
    print(min(arr))
