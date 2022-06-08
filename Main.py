a1, a2, a3 = map(int, input().split())

for i in range(a3,0,-1):
  if a1 % i ==0 and a2 % i ==0 and a3 % i ==0:
    print(i)
    break