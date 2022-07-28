# 15
# 1~9 9개
# 10~15 12개
# ==> 21

# 115
# 1~9 9개 (9)
# 10~99 180개 (90)
# 100~115 48개 (16)
# ==> 237

# +@ : 100~999 = 2700

# 숫자들의 개수 : 9 180 2700 36000 ... 

N = int(input())

length = len(str(N))
summary = 0
if length == 1:
    print(N)
else :
    for i in range(length-1):
        summary += int(str(9*(i+1))+"0"*i)
    summary += length * (N - int("9" * (length-1)))
    print(summary)