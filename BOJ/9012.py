N = int(input())
for i in range(N):
    summary = 0
    flag = 0
    brackets = input()
    for j in brackets:
        if j == "(":
            summary += 1
        elif j == ")":
            summary -= 1
        if summary < 0 :
            break
    if summary == 0:
        flag = 1
    print(["NO", "YES"][flag])
