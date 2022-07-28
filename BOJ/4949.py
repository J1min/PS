q = "0"
while q != '.':
    try:
        arr = []
        q = input()
        for i in q:
            if i == "(":
                arr.append(i)
            elif i == ")" and arr[-1] == "(":
                arr.pop()
            elif i == "[":
                arr.append(i)
            elif i == "]" and arr[-1] == "[":
                arr.pop()
        else:
            print("yes")
    except IndexError:
        print("no")
