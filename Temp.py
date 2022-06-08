def binary(num):
    save = []
    
    while True:
        a = int(num / 2)
        b = int(num % 2)
        save.insert(0, b)
        
        if a != 0:
            num = a
        else:
            break
            
    final = ''.join(map(str, save))
    print(final)

num = int(input("10진수를 입력하시오 : "))
binary(num)