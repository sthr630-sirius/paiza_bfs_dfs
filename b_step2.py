from collections import deque
n, x = map(int, input().split())

x -= 1

g = [[] for _ in range(n)]
for _ in range(n-1):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    g[a].append(b)
    g[b].append(a)

is_visited = [False]*n
step = [0]*n
next_v_list = deque()

next_v = x
next_v_list.append(next_v)
is_visited[next_v] = True
step[next_v] = 0

while next_v_list:
    now_v = next_v_list.popleft()
    for next_v in g[now_v]:
        if not is_visited[next_v]:
            next_v_list.append(next_v)
            is_visited[next_v] = True
            step[next_v] = step[now_v] + 1

for i in range(len(step)):
    if step[i] == 3:
        print(i+1)