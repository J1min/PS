number = list(map(int, input().split()))
for i in range(1, len(number)-2):
    if number[i] == 0:
        number.pop(i+1)
