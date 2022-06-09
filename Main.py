def solution(n):
  i = 0
  while True:
    if n == 1:
      return i
    if i >= 500:
      return -1
    if n % 2 == 0:
      n /= 2
    else:
      n = n * 3 + 1
    i += 1
