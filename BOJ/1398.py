import sys
# PROBLEM - 동전 문제
# TIER - G2
# NUMBER - 1398
# DATE - 2022-07-30 11:49
# IDEA - 그리디임 이게 동전이 차차차 순서대로 늘어나는데
# while 돌려서 동전 < 금액 될때까지 금액을 올리고
# 그 바로 전에있는 동전을 쓰면 됨
input = sys.stdin.readline
N = int(input().rstrip())
money = [int(input().rstrip()) for _ in range(N)]
answer = []


def set_wallet(money):
    start = 1
    wallet = [start]
    while start < money:
        if len(str(start)) % 2 == 1:
            start *= 10
            wallet.append(start)
        elif str(start)[:2] == '25':
            start *= 4
            wallet.append(start)
        else:
            start *= 25
            start //= 10
            wallet.append(start)
    if wallet[-1] >= 10:
        wallet.pop()
    return wallet


for i in range(N):
    count = 1
    my_wallet = set_wallet(money[i])
    while True:
        print(my_wallet)
        if money[i] - my_wallet[-1] > 0:
            money[i] -= my_wallet[-1]
            count += 1
        else:
            if len(my_wallet) == 1:
                print(count)
                break
            my_wallet.pop()
