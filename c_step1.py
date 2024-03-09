from collections import deque
n, m, x = map(int, input().split())

x -= 1

g = [[] for _ in range(n)]
for _ in range(m):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    g[a].append(b)
    g[b].append(a)

for gi in g:
    gi.sort()

next_v_que = deque()
is_visited = [False]*n

next_v = x
print(next_v+1)
next_v_que.append(next_v)
is_visited[next_v] = True


while next_v_que:
    now_v = next_v_que.popleft()
    for next_v in g[now_v]:
        if not is_visited[next_v]:
            print(next_v+1)
            next_v_que.append(next_v)
            is_visited[next_v] = True

