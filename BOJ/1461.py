import collections
N, M = map(int, input().split())
distance = list(map(int, input().split()))
distance.sort()
if N == 1:
    print(distance[0])
else:
    books = collections.deque(distance)
    print(distance)
    # def R_L(distance, length, amount):  # 우측 > 좌측 순서로 탐색
    #     total = 0
    #     while len(distance) != 0:
    #         print(distance)
    #         now = distance[-1]
    #         for i in range(amount):
    #             if len(distance) != 0:
    #                 distance.pop()
    #         if len(distance) != 0:
    #             total += abs(now-distance[-1])
    #     return total

    print(R_L(books, N, M))
