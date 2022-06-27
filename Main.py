n, m, k = map(int, input().split())
arr = list(map(int, input().split()))
arr = sorted(arr)
next_max = m % k
real_max = 0
if next_max == 0:
  next_max = m - k
real_max = m - next_max
print((arr[-1] * real_max) + (arr[-2] * next_max))
