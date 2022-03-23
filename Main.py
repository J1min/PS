n = input().upper()
check = list(0 for i in range(26))
b = -1
count = 0

for i in n:
    check[ord(i)-65] += 1

for i in range(26):
    if(check[i] > b):
        b = check[i]
        count = i

if check.count(max(check))>1:
    print("?")
else:
    print(chr(count+65))

