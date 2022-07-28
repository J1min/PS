import bisect
N, target = map(int, input().split())
numbers = list(map(int, input().split()))

def count_by_range(numbers, left, right): 
    right = bisect.bisect_right(numbers, right) # 우측 제일 마지막 target 
    left = bisect.bisect_left(numbers, left) # 좌측 제일 마지막 target
    return right - left # 두개의 인덱스를 빼주면 그 숫자의 개수가 나옴

count = count_by_range(numbers, target, target)
if count == 0:
    print("없데수")
else:
    print(count)
