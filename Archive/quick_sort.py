array = [6, 7, 8, 5, 9, 2, 3, 4, 1]

def quick_sort(array):
    if len(array) <= 1:
        return array
    
    pivot = array[0]
    tail = array[1:]
    
    left = [x for x in tail if x <= pivot]
    right = [x for x in tail if x > pivot]
    
    return quick_sort(left) + [pivot] + quick_sort(right)

print(quick_sort(array))