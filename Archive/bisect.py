import bisect

array = [1, 2, 3, 3, 3, 3, 4, 4, 8, 9]


def count_by_range(array, left, right):
    right = bisect.bisect_right(array, right)
    left = bisect.bisect_left(array, left)
    return right - left

print(count_by_range(array, 4, 4)) 
print(count_by_range(array, -1, 3))