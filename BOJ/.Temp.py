start = 1
def set_wallet(money):
    global start
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
    wallet.pop()
    return wallet
print(set_wallet(47))