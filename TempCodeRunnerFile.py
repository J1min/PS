from itertools import permutations
n, m = map(int, input().split())
arr = list(map(int, input().split()))

for i in list(permutations(arr, 3)):
    arr.append(abs(m-sum(i)))
print(m - min(arr))
