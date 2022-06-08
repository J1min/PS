n = int(input()) # 3, 이진수의 길이
arr = [] # 길이에 맞는 이진수들을 넣는 배열
i = 0 # 반복에 쓰일 친구
count = 0

while 1:
  binary = bin(i)[2:]
  if len(binary) <= n:
    arr.append(binary.zfill(n)) # ob를 뺀 진짜 이진수들을 모아놓음
  elif len(binary) > n:
    for j in arr:
      if "00" not in j:
        count += 1
    break
  i += 1
  

print(count)
