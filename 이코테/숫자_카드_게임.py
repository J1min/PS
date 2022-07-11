N, M = map(int, input().split())
result = 0
for i in range(N):
    cards = list(map(int, input().split()))
    min_value = min(cards)
    result = max(min_value, result)
print(result)