import itertools


def multiply(array):
    summary = 1
    for i in range(len(array)):
        summary *= array[i]
    return summary


N = int(input())
words = []
len_list = []

for i in range(N):
    word = list(input())
    words.append(word)
    len_list.append(len(word))

length = len(sum(words, []))
numbers = [str(i) for i in range(9, 9-length, -1)]
max_ = float("-inf")

for i in itertools.permutations(numbers, length):
    print(i)
    # max_ = max(max_, )
print(max_)
