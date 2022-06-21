def solution(lottos, win_nums):
    best = 0
    worst = 0
    for i in lottos:
        if i in win_nums or i == 0:
            best += 1
    bestGrade = 7 - best
    worstGrade = 7 - (best - lottos.count(0))

    if bestGrade == 7:
        bestGrade -= 1
    if worstGrade == 7:
        worstGrade -= 1
    return [bestGrade, worstGrade]

print(solution([1, 2, 3, 4, 5, 6], [7, 8, 9, 10, 11, 12]))