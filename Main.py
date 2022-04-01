result = []

def number1(num):
    if num <= 10000:
        for i in range(len(str(num))):
            result.append(str(num[i: i + 1]))
        num = sum(result) + int(num)
        print(num)
        number(num)
        result = []
    else:
        return

n = 1

number1(n)