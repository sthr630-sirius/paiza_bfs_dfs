from collections import deque

h, w, y, x = map(int, input().split())

next_ps  = deque()
delta = [[0, -1], [1, 0], [0, 1], [-1, 0]]
max_step = 3

next_y = y
next_x = x
next_step = 0

next_ps.append([next_y, next_x, next_step])

counter = 0

while next_ps:
    now_p = next_ps.pop()
    now_y = now_p[0]
    now_x = now_p[1]
    now_step = now_p[2]
    #print(f"y:{now_y}, x:{now_x}, step:{now_step}")
    if now_step == max_step:
        print(now_y, now_x)
    for dy, dx in delta:
        next_y = now_y + dy
        next_x = now_x + dx
        if 0 <= next_y < h and 0 <= next_x < w and now_step <= max_step-1:
            next_step = now_step + 1
            next_ps.append([next_y, next_x, next_step])