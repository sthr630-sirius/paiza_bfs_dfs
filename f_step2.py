from collections import deque

n, m = map(int, input().split())
g = [[]*n for _ in range(n)]
for _ in range(m):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    g[a].append(b)
    g[b].append(a)

is_visited = [False]*n
color = ["blue"]*n
nxt_vertices = deque()

nxt_v = 0
nxt_vertices.append(nxt_v)
color[nxt_v] = "blue"
is_visited[nxt_v] = True
is_bipartite = True

while nxt_vertices:
    now_v = nxt_vertices.popleft()
    for nxt_v in g[now_v]:
        #if color[now_v] == color[nxt_v]:
        #    is_bipartite = False
        if not is_visited[nxt_v]:
            nxt_vertices.append(nxt_v)
            is_visited[nxt_v] = True

            if color[now_v] == "blue":
                color[nxt_v] = "red"
            else:
                color[nxt_v] = "blue"

for i in range(n):
    for v in g[i]:
        if color[i] == color[v]:
            is_bipartite = False

#print(color)
#print(is_visited)

if is_bipartite:
    print("Yes")
else:
    print("No")

#print(is_visited)
#print(is_bipartite)
#for gi in g:
#    print(*gi)