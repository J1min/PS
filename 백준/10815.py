dict_ = {}
N = int(input())
arr = list(map(int, input().split()))
M = int(input())
exist = list(map(int, input().split()))

for i in exist:
    dict_[i] = 0
for i in arr:
    dict_[i] = 0
for i in arr:
    dict_[i] = 1

for i in exist:
    print(dict_[i], end=' ')