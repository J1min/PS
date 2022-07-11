N = int(input())
which = [1, 1]
move = list(map(str, input().split()))
for i in move:
    if i == "R" and which[1] != N:
        which[1] += 1
    elif i == "L" and which[1] != 1:
        which[1] += 1
    elif i == "U" and which[0] != 1:
        which[0] += 1
    elif i == "D" and which[0] != N:
        which[0] += 1
print(*which)