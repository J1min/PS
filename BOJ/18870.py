N = int(input())
n = list(map(int, input().split()))
set_ = sorted(set(n))
dic = dict(zip(set_, [i for i in range(len(set_))]))
for i in n:
    print(dic[i], end=" ")