numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def binary_search(array, target, start, end):
    if start > end:
        return False
    mid = (start + end) // 2
    if target == array[mid]:
        return mid
    elif target < array[mid]:
        return binary_search(array, target, start, mid - 1)
    else:
        return binary_search(array, target, mid + 1, end)



result = binary_search(numbers, 3, 0, 9)

if not result:
    print("값이없데수")
else:
    print(result+1)
    
