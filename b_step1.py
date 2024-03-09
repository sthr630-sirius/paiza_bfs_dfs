n, x = map(int, input().split())
g = [[] for _ in range(n)]
for _ in range(n-1):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    g[a].append(b)
    g[b].append(a)

g[x-1].sort()

for i in range(len(g[x-1])):
    print(g[x-1][i]+1)