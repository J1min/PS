import math
N1, N2 = map(int, input().split())
M1, M2 = map(int, input().split())
분모 = math.lcm(N2, M2)

print(분모//N2 * N1 + 분모//M2 * M1, 분모)