import itertools
N, M = map(int, input().split())
numbers = list(map(int, input().split()))
numbers.sort()
for i in itertools.permutations(numbers, M):
    print(*i)