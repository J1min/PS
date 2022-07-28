N = input()
flag = False

arr = []

if "<" in N:
    answer = []
    N = N.replace("<", "!")
    N = N.replace(">", "!")
    for i in N:
        if i == "!":
            flag = not flag
            if flag:
                answer.append("".join(arr[::-1]))
                arr = []
            else:
                answer.append("".join(arr))
                arr = []
        else:
            arr.append(i)
    if answer[0] == "":
        answer.pop(0)
    for i in range(len(answer)):
        if i % 2 == 0:
            print(f"<{answer[i]}>", end="")
        else:
            answer[i] = answer[i].split()
            print(" ".join(answer[i][::-1]), end="")
    print(N.split('!')[-1][::-1])
else:
    if " " in N:
        for i in N.split():
            print(i[::-1], end=" ")
    else:
        print(N[::-1])
