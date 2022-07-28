N = int(input())
name = []
name_set = set()
answer = []
for i in range(N):
    q = input()
    name.append(q[0])
    name_set = set(name)

for i in name_set:
    if name.count(i) >= 5:
        answer.append(i)

if len(answer) == 0:
    print("PREDAJA")
else:
    answer.sort()
    print("".join(answer))