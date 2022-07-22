N = int(input())
string = input()
for i in range(len(string)):
    if i % N == 0:
        print(string[i], end='')