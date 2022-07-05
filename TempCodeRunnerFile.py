_ = input()
sum = 0
n = list(input())
arr = []
for i in n:
    arr.append(ord(i)-96)

for i in range(len(arr)):
    sum += arr[i] * (31 ** i)
    sum %= 1234567891

print(sum)
