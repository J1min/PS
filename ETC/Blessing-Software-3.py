number = list(map(int, input().split()))
number2 = []

for i in range(1, len(number)):
    if number[i] != 0:
        number2.append(number[i])
    else:
        number2.pop()    
        
print(sum(number2))