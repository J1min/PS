def sosu(n):
    prime = [True] * (n+1)  # True ===== 소수임
    for i in range(2, int(n**0.5)+1):  # n의제곱만큼만 돌아도 ㄱㅊ
        if prime[i] == True:  # 솟수면
            for j in range(i+i, n+1, i):  # 그 소수의 배수
                prime[j] = False  # 전부다 합성수
    return [i for i in range(2, n+1) if prime[i] == True]  # 솟수만출력

print(sosu(9))