n = int(input())

def chae(n):
    prime = [True] * n
    m = int(n ** 0.5)
    for i in range(2, m+1):
      if prime[i] == True:
        for j in range(i*2, n, i):
          prime[j] = False
    return [i for i in range(2, n) if prime[i] == True]

print(chae(n))
