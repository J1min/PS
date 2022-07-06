board = []
for i in range(9):
    arr = []
    for j in range(9):
        if i%2 == 0:
            if j % 2 == 0:
                arr.append("B")
            else:
                arr.append("W")
        else:
            if j % 2 == 0:
                arr.append("W")
            else:
                arr.append("B")
    board.append(arr)
print(board)
