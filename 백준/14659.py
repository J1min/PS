# 14659 한조서열정리
N = int(input()) 
arr = list(map(int, input().split()))

result = []
count = 0
height = arr[0] # 현재 계산할 봉우리

for i in range(1, len(arr)):
    if height > arr[i]: # arr[i]가 봉우리보다 더 작으면 (뒤에 봉우리가 앞의 봉우리보다 크면)
        count += 1 # 잡은사람 ++
    else: # 근데 만약 지금 봉우리가 그 전 봉우리보다 더 크다면
        height = arr[i] # 해당 봉우리는 끝, 새로 계산할 봉우리를 세팅하고
        result.append(count) # 계산해놓은 잡은사람을 리스트에 추가
        count = 0 # 잡은사람 초기화
result.append(count)  # 그리고 만약 뒷부분에 쭈루룻 1 2 3 4 2 1 이런식으로 나와있으면 리스트에 
                      # 추가가 안되므로 마지막까지 깔끔하게 추가
print(max(result)) # 최고기록 ㄱㄱ
