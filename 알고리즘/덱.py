from collections import deque
N = int(input())
deck = deque()
for i in range(N):
    q = input().split()
    if q[0] == "push_back":
        deck.append(q[1])
    elif q[0] == "push_front":
        deck.appendleft(q[1])
    elif q[0] == "front":
        if len(deck) != 0:
            print(deck[0])
        else:
            print(-1)
    elif q[0] == "back":
        if len(deck) != 0:
            print(deck[-1])
        else:
            print(-1)
    elif q[0] == "pop_front":
        if len(deck) != 0:
            print(deck.popleft())
        else:
            print(-1)
    elif q[0] == "pop_back":
        if len(deck) != 0:
            print(deck.pop())
        else:
            print(-1)
    elif q[0] == "size":
        print(len(deck))
    elif q[0] == "empty":
        if len(deck) == 0:
            print(1)
        else:
            print(0)
