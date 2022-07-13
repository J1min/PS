nowSticks = 64
sticks = []
stick = int(input())

totalStickLength = sum(sticks)
breakCount = 0


while nowSticks < stick:
    if nowSticks > stick:
        nowSticks //= 2
    else:
        sticks.append(nowSticks)

print(sticks)
