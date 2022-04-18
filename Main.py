def Permutation(length):
    n = length
    perm = list()  # 0 for _ in range(n)
    numList = list(i for i in range(1, length+1))  # 나열해야하는 수의 목록

    if len(perm) == n or len(numList) == 0:
        print(perm)
        return

    for i in numList:
        perm.append(i)
        numList2 = numList - [i]
        Permutation(perm, numList2)
        perm.delete(i)

Permutation(3)