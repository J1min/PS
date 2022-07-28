import sys
from collections import deque
queue = deque()
N = int(sys.stdin.readline().rstrip())
for i in range(N):
    q = sys.stdin.readline().split()
    if q[0] == 'push':
        queue.append(q[1])
    elif q[0] == 'pop':
        if len(queue) != 0:
            print(queue.popleft())
        else:
            print(-1)
    elif q[0] == 'size':
        print(len(queue))
    elif q[0] == 'empty':
        if len(queue) == 0:
            print(1)
        else:
            print(0)
    elif q[0] == 'front':
        if len(queue) != 0:
            print(queue[0])
        else:
            print(-1)
    elif q[0] == 'back':
        if len(queue) != 0:
            print(queue[-1])
        else:
            print(-1)