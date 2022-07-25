dish = ["^"]
N = input()
height = 0
for i in range(len(N)):
    if N[i] != dish[-1]:
        height += 10
        dish.append(N[i])
    else:
        height += 5
        dish.append(N[i])

print(height)