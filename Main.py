# start ->
# 1
# 1 2
# 3 2 1
# 1 2 3 4
# 5 4 3 2 1
# end ->
# 1
# 2 1
# 1 2 3
# 4 3 2 1
# 1 2 3 4 5
l1 = []
l2 = []
n = int(input())
if n == 1:
    print("1/1")
elif n == 2:
    print("1/2")
for i in range(1, n):  # 1 ~ 5
    start = 0
    if i % 2 == 0:  # 짝수일 경우
        for j in range(1, i+1):
            l1.append(j)
        for j1 in range(i, 0, -1):
            l2.append(j1)
    else:  # 홀수일 경우
        for k in range(i, 0, -1):
            l1.append(k)
        for k1 in range(1, i+1):
            l2.append(k1)
if n > 2:
    print(f'{l1[n-1]}/{l2[n-1]}')

# # start 구현
# for i in range(1, 6):  # 1 ~ 5
#     start = 0
#     if i % 2 == 0:  # 짝수일 경우
#         for j in range(1, i+1):
#             start = j
#             print("start", start)
#     else:  # 홀수일 경우
#         for k in range(i, 0, -1):
#             start = k
#             print("start", start)
# # end 구현
# for i in range(1, 6):  # 1 ~ 5
#     end = 0
#     if i % 2 == 0:  # 짝수일 경우
#         for j in range(i, 0, -1):
#             end = j
#             print("end", end)
#     else:  # 홀수일 경우
#         for k in range(1, i+1):
#             end = k
#             print("end", end)
