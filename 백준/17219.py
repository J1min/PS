N, M = map(int, input().split())
notepad = {}
for i in range(N):
    site, id_ = input().split()
    notepad[site] = id_
for j in range(M):
    print(notepad[input()])