import bisect
_ = input()
A = list(map(int, input().split()))
_ = input()
M = list(map(int, input().split()))

for i in M:
  print(bisect.bisect(A, i))