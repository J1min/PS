while True:
    arr = []
    q = input()
    for i in q:
        if i == "(":
            arr.append(i)
        elif i == ")":
            arr.pop()
    print(arr)