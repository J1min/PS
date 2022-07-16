N = int(input())
numbers = list(map(int, input().split()))
s_numbers = sorted(numbers)
used = []
usedDict = dict()
for i in range(len(s_numbers)+1):
    usedDict[i] = 0
for i in numbers:
    if s_numbers.index(i) in used: # 만약 있을경우 야 ㅋㅋ
        usedDict[s_numbers.index(i)] += 1
        used.append(s_numbers.index(i)+usedDict[s_numbers.index(i)])
    else: # 없을 경우 (개꿀 ㅋㅋ)
        used.append(s_numbers.index(i))
print(*used)
