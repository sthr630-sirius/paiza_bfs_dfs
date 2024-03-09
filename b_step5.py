from collections import deque
n, x, y = map(int, input().split())

x -= 1
y -= 1
#target_step = l

g = [[] for _ in range(n)]
for _ in range(n-1):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    g[a].append(b)
    g[b].append(a)

is_visited = [False]*n
step = [0]*n
prev_v = [-1]*n
next_v_list = deque()

next_v = x
next_v_list.append(next_v)
is_visited[next_v] = True
step[next_v] = 0
prev_v[next_v] = -1

while next_v_list:
    now_v = next_v_list.popleft()
    for next_v in g[now_v]:
        if not is_visited[next_v]:
            next_v_list.append(next_v)
            is_visited[next_v] = True
            step[next_v] = step[now_v] + 1
            prev_v[next_v] = now_v

path_v = y
path = []

for _ in range(step[y]+1):
    path.append(path_v)
    path_v = prev_v[path_v]

for v in path[::-1]:
    print(v+1)