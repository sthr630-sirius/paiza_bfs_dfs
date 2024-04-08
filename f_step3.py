from collections import deque

def bfs(g, is_visited, v):
    nxt_vertices = deque()

    nxt_v = v
    nxt_vertices.append(nxt_v)
    is_visited[nxt_v] = True

    while nxt_vertices:
        now_v = nxt_vertices.popleft()
        for nxt_v in g[now_v]:
            if not is_visited[nxt_v]:
                nxt_vertices.append(nxt_v)
                is_visited[nxt_v] = True


n, m = map(int, input().split())
g = [[] for _ in range(n)]
for _ in range(m):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    g[a].append(b)
    g[b].append(a)

#for gi in g:
#    print(*gi)

is_visited = [False]*n
cnt = 0

for v in range(n):
    if not is_visited[v]:
        bfs(g, is_visited, v)
        cnt += 1

print(cnt)