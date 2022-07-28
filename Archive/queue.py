from collections import deque

queue = deque()

queue.append(5)
queue.append(4)
queue.append(3)
queue.append(2)
queue.append(1)
# queue = [5, 4, 3, 2, 1]
print(queue.popleft()) # 5
print(queue.pop()) # 1