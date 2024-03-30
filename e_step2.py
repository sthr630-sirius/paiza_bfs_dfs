from collections import deque

def dfs(g, x, y):
    nxt_vertices = deque()
    is_visited = [False]*n
    visited_cnt = 0

    for gi in g:
        gi.sort(reverse=True)

    nxt_v = x
    nxt_vertices.append(x)

    while nxt_vertices:
        now_v = nxt_vertices.pop()
        #print(now_v)

        if not is_visited[now_v]:
            is_visited[now_v] = True
            visited_cnt += 1

            if now_v == y:
                #print(visited_cnt)
                return visited_cnt

            for nxt_v in g[now_v]:
                #print(nxt_v)
                if not is_visited[nxt_v]:
                    nxt_vertices.append(nxt_v)

def bfs(g, x, y):
    nxt_vertices = deque()
    is_visited = [False]*n
    visited_cnt = 0

    for gi in g:
        gi.sort()

    nxt_v = x
    nxt_vertices.append(nxt_v)
    is_visited[nxt_v] = True

    while nxt_vertices:
        now_v = nxt_vertices.popleft()
        visited_cnt += 1

        if now_v == y:
            #print(now_v)
            #print(y)
            #print(visited_cnt)
            return visited_cnt

        #print(now_v)
        for nxt_v in g[now_v]:
            if not is_visited[nxt_v]:
                nxt_vertices.append(nxt_v)
                is_visited[nxt_v] = True

n, x, y = map(int, input().split())
g = [[] for _ in range(n)]

x -= 1
y -= 1

for _ in range(n-1):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    g[a].append(b)
    g[b].append(a)

#for gi in g:
#    print(gi)

if dfs(g, x, y) < bfs(g, x, y):
    print("dfs")
elif dfs(g, x, y) > bfs(g, x, y):
    print("bfs")
else:
    print("same")