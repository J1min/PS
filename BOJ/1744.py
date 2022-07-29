import sys
# PROBLEM - 수 묶기
# NUMBER - 1744
# DATE - 2022-07-29 14:40 ~ 16:20
# IDEA - 이것도 역시 그리디 입니다 허허
# 제일 큰 수끼리 곱해주면 될듯 함
# 근데 1은 안곱해주는게 더 크니까 조심!
# 그리고 내 생각에 0은 카운팅을 해서
# 음수들을 무력화시키는데 쓰면 좋을 것 같은데

# HISTORY - 실수로 pop 하는거 확인하고 print 안지워서 1시간날림 ㅋㅋ

N = int(sys.stdin.readline().rstrip())
numbers = [0] * N
for i in range(N):
    numbers[i] = int(sys.stdin.readline().rstrip())
numbers.sort()
result = []

plus = []
minus = []

if N == 1:
    print(numbers[0])
    sys.exit()

zero = 0

for i in range(N):
    if numbers[i] > 1:
        plus.append(numbers[i])
    elif numbers[i] == 1:
        result.append(1)
    elif numbers[i] == 0:
        zero += 1
    else:
        minus.append(numbers[i])

# print(minus)
# print(plus)

minus.sort(reverse=True)
if len(minus) >= 2:

    while True:
        if len(minus) < 2:
            break
        a, b = minus.pop(), minus.pop()
        result.append(a*b)

    # 마이너스끼리 다 곱해주고 나서 혹시나 0 있음 + 마이너스 한개 남아있음 인 경우에는 0*음수 해줌
minus.sort()

if zero != 0 and len(minus) == 1:
    minus.pop()

while True:
    if len(plus) < 2:
        break
    a, b = plus.pop(), plus.pop()
    result.append(a*b)


# print(plus, minus, result)
print(sum(plus + minus + result))
