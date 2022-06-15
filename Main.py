n = int(input())

line = 1

while n > line:
  n -= line
  line += 1

print(line)

# n = 5 인 경우 
# 5 > 1
# 5 - 1
# n = 4
# line = 2
# n = 2
# line = 3
# 2 - 3 = -1 이므로 컷
# 3번째 줄임
