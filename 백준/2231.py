N = input()
answer = []
flag = 0
for i in range(int(N)):
    if i + sum(map(int, list(str(i)))) == int(N):
        answer.append(i)
        flag = 1
if len(N) == 1:
    print(int(N)//2)
else:
    if len(answer) == 0:
        print(0)
    else:
        print(min(answer))
