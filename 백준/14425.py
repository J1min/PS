N, M = map(int, input().split())
dict_ = {}
count = 0
for i in range(N):
    dict_[input()] = 1
for j in range(M):
    q = input()
    try:
        if dict_[q] == 1:
            count += 1
    except KeyError:
        pass
print(count)