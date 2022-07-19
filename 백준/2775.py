T = int(input())

for _ in range(T):
    k = int(input())
    n = int(input())
    people = [i for i in range(1, n+1)]
    for __ in range(k):
        for j in range(1, n):
            people[j] += people[j-1]
            print(people)
    print(people[-1])


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