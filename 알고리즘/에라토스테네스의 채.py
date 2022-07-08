def sosu(n):
    prime = [True] * n  # True ===== 소수임
    for i in range(2, int(n**0.5)):  # n의제곱만큼만 돌아도 ㄱㅊ
        if prime[i] == True:  # 솟수면
            for j in range(i+i, n, i):  # 그 소수의 배수
                prime[j] = False  # 전부다 합성수
    return [i for i in range(2, n) if prime[i] == True]  # 솟수만출력

print(sosu(9))