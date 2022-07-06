N = int(input())
distance = list(map(int, input().split())) # 거리를 담은 배열
price = list(map(int, input().split())) # 도시의 기름값을 담은 배열
money = 0
nowMin = float("inf") # 무한대
for i in range(len(distance)): # distance의 길이만큼 반복
    if nowMin > price[i]: # 주유소 최솟값을 nowMin에 저장해줌
        nowMin = price[i] 
    money += nowMin * distance[i] # 거리 * 최소값을 money에 누적
print(money) # 최종 가격 