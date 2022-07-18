N = int(input())
for i in range(N):
    sum_ = 0
    brackets = list(input())
    for j in brackets:
        if j == "(":
            sum_ += 1
        elif j == ")":
            sum_ -= 1
        if sum_ < 0:
            print("NO")
            break
    if sum_ == 0:
        print("YES")
    elif sum_ > 0:
        print("NO")
