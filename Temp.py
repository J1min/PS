n = input()
arr = []
check = list(0 for i in range(26))
now1 = 0
max1 = -1

for i in n:
    arr.append(i)

for i in arr:
    now = ord(i)-65
    if now >= 32:
        now -= 32
    print("ord : ",now)
    check[now] += 1


for i in range(26):
  print(check[i]<max1)
print(max1)