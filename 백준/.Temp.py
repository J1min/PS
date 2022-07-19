X = int(input())
count = 0
if X % 64 != X:
    X %= 64
    count += 1
if X % 32 != X:
    X %= 32
    count += 1
if X % 16 != X:
    X %= 16
    count += 1
if X % 8 != X:
    X %= 8
    count += 1
if X % 4 != X:
    X %= 4
    count += 1
if X % 2 != X:
    X %= 2
    count += 1

if X % 2 == 1:
    print(count + 1)
else:
    print(count)