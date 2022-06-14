A, B = map(int, input().split())

A100 = A // 100
A10 = A // 10 - (10 * A100)
A1 = A % 10
B100 = B // 100
B10 = B // 10 - (10 * B100)
B1 = B % 10

Aw = A1 * 100 + A10 * 10 + A100
Bw = B1 * 100 + B10 * 10 + B100

if Aw > Bw:
    print(Aw)
else:
    print(Bw)
