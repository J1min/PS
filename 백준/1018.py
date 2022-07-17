N, M = map(int, input().split())
board = []
min_ = float("inf")
BW_board = [["B", "W", "B", "W", "B", "W", "B", "W"],
            ["W", "B", "W", "B", "W", "B", "W", "B"],
            ["B", "W", "B", "W", "B", "W", "B", "W"],
            ["W", "B", "W", "B", "W", "B", "W", "B"],
            ["B", "W", "B", "W", "B", "W", "B", "W"],
            ["W", "B", "W", "B", "W", "B", "W", "B"],
            ["B", "W", "B", "W", "B", "W", "B", "W"],
            ["W", "B", "W", "B", "W", "B", "W", "B"]]

def search(x, y):
    gap = 0
    for i in range(8):
        for j in range(8):
            if BW_board[i][j] != board[i+x][j+y]:
                gap += 1
    return min(gap, 64-gap)
for i in range(N):
    board.append(list(input()))
for i in range(N-7):
    for j in range(M-7):
        min_ = min(min_, search(i, j))
print(min_)