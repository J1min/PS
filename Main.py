import sys

n, m = map(int, sys.stdin.readline().split())

lst = []
for i in range(n):
    lst.append(int(sys.stdin.readline()))
lst.sort()

start = 0
end = 0
min_value = sys.maxsize

while start < n and end < n: # start, end가 모두 데이터 크기보다 작다면
    result = lst[end] - lst[start] # 그 차를 구함
    if result >= m: # 차가 목표값보다 더 크다면 
        min_value = min(lst[end] - lst[start], min_value) # 그 중 가장 작은값을 min_value에 넣음
        start += 1 # 그 후 start 포인터 하나 증가
    else: # 목표값보다 작다면 
        end += 1 # end 포인터 하나 증가
print(min_value)