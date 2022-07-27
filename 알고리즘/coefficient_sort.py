# 이게 모든 데이터가 양의 정수인 경우에는 가장 빠름
# 숫자번지 index에 개수를 카운트 해주고
# 출력하면 됨 

array = [6, 7, 8, 5, 9, 2, 3, 4, 1, 0, 1, 2, 3, 4,
         5, 2, 2, 3, 12, 3, 12, 2, 12, 2, 2, 3, 1, 2]
count = [0] * (max(array) + 1)

for i in range(len(array)):
    count[array[i]] += 1

for i in range(len(count)):
    for j in range(count[i]):
        print(i, end=' ')
