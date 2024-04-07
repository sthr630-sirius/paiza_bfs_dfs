from my_graphviz import indirected_graph
from collections import deque

n, m = map(int, input().split())
g = [[] * n for _ in range(n)]
"""
graphviz用
"""
gg = [[] * n for _ in range(n)]

for _ in range(m):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    g[a].append(b)
    g[b].append(a)

    """
    graphviz用にedgeの重複を省略
    """
    gg[a].append(b)

is_visited = [False] * n
color = ["white"] * n
is_bipartite = True

for i in range(n):
    """
    未訪問の頂点全てから全探索を開始する
    """
    if not is_visited[i]:
        nxt_vertices = deque()

        nxt_v = i
        nxt_vertices.append(nxt_v)
        color[nxt_v] = "blue"
        is_visited[nxt_v] = True
        print(f"out graph paint @{nxt_v}")
        indirected_graph.OutGraph(gg, color, -1)

        while nxt_vertices:
            now_v = nxt_vertices.popleft()
            for nxt_v in g[now_v]:
                if not is_visited[nxt_v]:
                    nxt_vertices.append(nxt_v)
                    is_visited[nxt_v] = True

                    if color[now_v] == "blue":
                        color[nxt_v] = "red"
                    else:
                        color[nxt_v] = "blue"

                    """
                    色塗りの遷移をgraphvizを利用して可視化
                    """
                    print(f"out graph paint @{nxt_v}")
                    indirected_graph.OutGraph(gg, color, now_v)

for i in range(n):
    if g[i]:
        for v in g[i]:
            if color[i] == color[v]:
                is_bipartite = False

if is_bipartite:
    print("Yes")
else:
    print("No")
