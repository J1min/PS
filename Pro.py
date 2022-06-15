n = int(input())

for i in range(n):
    a, b = map(int, input().split())
    if a != 10:
      print(a ** (b%10)%10)
    else:
      print(10)