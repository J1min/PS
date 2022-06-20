n = int(input())
first = list(input()) # 첫번째 문자열은 그냥 바로 받고 7번줄의 for문의 range에 -1 해줌
real = [0] * len(first) # ?? 가 섞인 정답 문자열 담는 곳
if n == 1: # 만약 문자열이 하나밖에 없으면 아래 for 문이 안돌아가고 000000 으로 real 리스트가 채워짐, 그걸 방지하기 위함
    real = list(first) 
for i in range(n-1): # 위에서 1번쨰 문자열을 받았으니까 -1번 돌아감
    q = list(input()) # 입력을 받고
    for j in range(len(first)): # 어짜피 문자열 길이는 같으니까 first, q 둘다 상관 XX
        if real[j] != "?": # 이미 ?로 대치한 문자열을 제외하고
            if first[j] != q[j]: # 처음 입력받은 친구와 마지막에 입력받은 친구의 [i] 번지가 다를 떄
                real[j] = "?" # "?" 집어넣기
            else: # 아닐 경우에는 그냥 해당 문자 집어넣기
                real[j] = first[j]
for i in real:
    print(i, end="") # 출력문