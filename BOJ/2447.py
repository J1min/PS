N = int(input())

stars = [["***"], ["* *"], ["***"]] * (N*3)

# *********
# * ** ** *
# *********
# ***   ***
# * *   * *
# ***   ***
# *********
# * ** ** *
# *********

for i in range(1, N+1):
    if i % 5 == 0:
        print("   ")
    if i%3 == 0:
        print()
    else:
        print(stars[i], end="")