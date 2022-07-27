# 반례는 아마 없을건데 
# 시간초과가 나네 ㅋㅋ;;

N = int(input())
numbers = sorted(list(map(int, input().split())))
min = float("inf")

for i in range(N-2):
    start, end = i+1, i+2
    while start < end and 0 <= start < N and end < N:
        summary = numbers[i] + numbers[start] + numbers[end]
        index = [i, start, end]
        if summary > 0:
            start -= 1
        elif summary < 0:
            end += 1
        if abs(summary) < abs(min) and end <= N:
            min = summary
            answer = index

answer = [numbers[answer[0]], numbers[answer[1]], numbers[answer[2]]]
answer.sort()

print(*answer)
