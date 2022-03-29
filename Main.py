nameArr = list()
scoreArr = list()

n, m = input().split()
n = int(n)
m = int(m)

for i in range(n):
    name, score = input().split()
    score = int(score)
    nameArr.append(name)
    scoreArr.append(score)

# print(nameArr, scoreArr)
diction = dict(zip(nameArr, scoreArr))
# diction = sorted(diction.items())

for i in diction.keys():
    if i < m:
        print(i)
        i += 1
