q = "0"
while q != '.':
    try:
        arr = []
        q = input()
        for i in q:
            if i == "(" and arr[-1] == ")":
                arr.append(i)
                print("yes")
            elif i == ")" and arr[-1] == "(": 
                arr.pop()
                print("yes")
            elif i == "[" and arr[-1] == "]":
                arr.append(i)
                print("yes")
            elif i == "]" and arr[-1] == "[":
                arr.pop()
                print("yes")
            else:
                print("no")
    except IndexError:
        print("no")
