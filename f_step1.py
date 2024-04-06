from collections import deque
"""
stack code

n, m, x = map(int, input().split())
g = [[] for _ in range(n)]
x -= 1

nxt_vertices = deque()
is_visited = [False]*n

for _ in range(m):
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
        print(now_v+1)
        is_visited[now_v] = True

        for nxt_v in g[now_v]:
            if not is_visited[nxt_v]:
                nxt_vertices.append(nxt_v)

        #print(f"deque:{nxt_vertices}")
        #print("")
"""

"""
recursive code
"""
import sys
sys.setrecursionlimit(10**6)
def dfs(g, is_visited, now_v):
    is_visited[now_v] = True
    #print(f"now : {now_v+1}")
    print(now_v+1)

    for nxt_v in g[now_v]:
        if not is_visited[nxt_v]:
            dfs(g, is_visited, nxt_v)

    return

n, m, x = map(int, input().split())
g = [[] for _ in range(n)]
x -= 1

is_visited = [False]*n

for _ in range(m):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    g[a].append(b)
    g[b].append(a)

for gi in g:
    gi.sort()

dfs(g, is_visited, x)