import re
N = input()
N = re.sub('[BLESSINGSOFTWARE]', '', N)
for i in N:
    if i != " ":
        print(i, end="")