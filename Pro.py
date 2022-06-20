arr = [1, 3, 8, -2, 2, 3]
arr_cnt = []
for i in arr:
    cnt = arr.count(i)
    arr.append(cnt)
print(arr_cnt)
