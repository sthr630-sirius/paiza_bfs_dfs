from collections import deque

n, x = map(int, input().split())
g = [[] for _ in range(n)]

x -= 1

nxt_vertices = deque()
is_visited = [False]*n

for _ in range(n-1):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    g[a].append(b)
    g[b].append(a)

for gi in g:
    gi.sort(reverse=True)

nxt_v = x
nxt_vertices.append(nxt_v)

while nxt_vertices:
    now_v = nxt_vertices.pop()
    if not is_visited[now_v]:
        is_visited[now_v] = True
        print(now_v+1)
        for nxt_v in g[now_v]:
            if not is_visited[nxt_v]:
                nxt_vertices.append(nxt_v)
            #is_visited[nxt_v] = True