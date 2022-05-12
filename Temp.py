n = int(input())
usedCount = 0
usedList = []
for i in range(n):
    arr = list(input())
    print(arr)
    for j in arr: 
        if j not in usedList:
            print(j)
            usedList.append(j)
            usedCount += 1
    usedList = []

print(usedCount)
