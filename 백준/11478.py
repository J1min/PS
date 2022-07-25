S = str(input())
ans = []
for i in range(len(S)):
    for j in range(len(S)-i):
        ans.append(S[j:j+i+1])
print(len(set(ans)))
