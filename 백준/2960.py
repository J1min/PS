N, M = map(int, input().split())

def sosu(n):
    prime = [True] * (n+1) 
    delete = []
    for i in range(2, int(n**0.5)+1):  
        if prime[i] == True: 
            for j in range(i, n+1, i):  
                if prime[j] == True:
                    delete.append(j)
                    prime[j] = False
                
    return delete

numbers = sosu(N)
print(numbers)