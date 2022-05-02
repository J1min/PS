grade = []
n = int(input())
for i in range(n):
    name, score = input().split()
    score = int(score)
    grade.append([score, name])
    grade = sorted(grade)

print(grade[n-3][1])
