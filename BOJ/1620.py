# 나는야 포켓몬 마스터 이다솜 집합과 맵
# 포켓몬 도감을 만들면 됨
# 이름 > 번호 리턴
# 번호 > 이름 리턴 이런식
N, M = map(int, input().split())
dictionary = {} 
for i in range(1,N+1):
  q = input()
  dictionary[str(i)] = q # 번호 : 이름
  dictionary[q] = str(i) # 이름 : 번호 이런식으로 그냥 둘다 박음 
for j in range(M): # 입력받은거 리턴 ㄱㄱ
  print(dictionary[input()])