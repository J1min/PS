T = int(input())

for _ in range(T):
    floor = [[1, 2, 3, 4, 5] ]
    N = int(input())
    M = int(input())
    now_floor = [0] * M
    for j in range(N):
        for k in range(M):
            now_floor.append([]) 


# 3층 3호에 살려고 한다면 2층 1호, 2층 2호, 2층 3호에 사는 사람들의 합만큼 3층 3호에 데리고 살아야 한다.
# 그럼 3층 2호를 산다고 하면 어떨까?
# 2층 1호, 2층 2호에 사는 사람들의 합만큼 데리고 살아야 한다.
# 그렇다면 3층 3호에 데리고 살아야 하는 인원은
# 3층 2호에 데리고 살아야 하는 인원 + 2층 3호에 데리고 살아야 하는 인원이 된다.


# 4층	1	6	21	56	126
# 3층	1	5	15	35	70
# 2층	1	4	10	20	35
# 1층	1	3	6	10	15
# 0층	1	2	3	4	5

# for문 2번 돌려서 리스트 뽑아낸 뒤에 [x-1][y-1] 조지면 나올거같은디;;
