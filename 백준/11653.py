v = int(input())
i = 2
while v != 1:
    if v % i == 0:
        v /= i
        print(i)
    else:
        i += 1