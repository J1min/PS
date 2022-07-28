# PROBLEM - 수 정렬하기 4
# NUMBER - 11931
# DATE - 2022-07-28 11:32
# IDEA - 원래는 정렬함수 쓸건데 지금은 한번 직접구현 해봄

N = int(input())
numbers = []
for i in range(N):
    numbers.append(int(input()))


def quick_sort(array):
    if len(array) == 0:
        return array

    pivot = array[0]
    tail = array[1:]

    left = [x for x in tail if x > pivot]
    right = [x for x in tail if x <= pivot]

    return quick_sort(left) + [pivot] + quick_sort(right)

numbers = quick_sort(numbers)

for i in numbers:
    print(i)
