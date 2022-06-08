n = int(input()) # 3, 이진수의 길이
arr = ['0'] # 길이에 맞는 이진수들을 넣는 배열
i = 0 # 반복에 쓰일 친구
count = 0

while 1:
  i += 1
  if len(bin(i)) <= n+2:
    arr.append(bin(i)[2:]) # ob를 뺀 진짜 이진수들을 모아놓음
  elif len(bin(i)) >= n+2:
    print(arr)
    for j in arr:
      if j not in "00":
        count += 1
    break

print(count)
