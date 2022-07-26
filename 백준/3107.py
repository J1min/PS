import collections

N = list(input().split("::"))
real = []
length = 0

for i in range(len(N)):
    real.append(N[i].split(":"))
    length += len(N[i].split(":"))

real.insert(1, [""] * (8 - length))
real = sum(real, [])

for i in range(len(real)):
    if i == len(real) - 1:
        print(real[i].zfill(4), end="")
    else:
        print(real[i].zfill(4), end=":")
