import bisect
_ = int(input())
myCard = list(map(int, input().split()))
myCard = sorted(myCard)
lenRange = int(input())
isMyCard = list(map(int, input().split()))
answer = [0] * len(isMyCard)

for i in range(lenRange): 
    if myCard[bisect.bisect(myCard, isMyCard[i])] == myCard[i]:
        print(myCard[bisect.bisect(myCard, isMyCard[i])], myCard[i])
        answer[i] = 0
    else:
        answer[i] = 1
print(*answer)
