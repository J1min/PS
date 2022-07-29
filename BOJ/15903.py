# PROBLEM - 카드 합체 놀이
# NUMBER - 15903
# DATE - 2022-07-29 14:05
# IDEA - 그리디이다. 우선순위 큐를 사용해서 한다는데 일단 이거 안풀리면 힙부터 다시 공부한다

N, M = map(int, input().split())
numbers = sorted(list(map(int, input().split())))
result = []
while True:
    if M == 0:
        break
    a, b = numbers.pop(0), numbers.pop(0)
    numbers.append(a+b)
    numbers.append(a+b)
    numbers.sort()
    M -= 1

print(sum(numbers))
