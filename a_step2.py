from collections import deque

def withinField(h, w, y, x):
    if 0<= y <h and 0<= x <w:
        return True
    else:
        return False

def underMaxStep(max_step, step):
    if step < max_step:
        return True
    else:
        return False

h, w = map(int, input().split())
y, x = map(int, input().split())

delta = [[-1, 0], [0, -1], [0, 1], [1, 0]]

max_step = 3

field = [["."]*w for _ in range(h)]
visited = [[False]*w for _ in range(h)]
next_p = deque()

"""
p = [y, x, step]
"""
next_p.append([y, x, 0])
field[y][x] = "*"
visited[y][ x] = True

while next_p:
    np = next_p.popleft()
    y = np[0]
    x = np[1]
    step = np[2]

    for dy, dx in delta:
        if withinField(h, w, y+dy, x+dx) and not visited[y+dy][x+dx] and underMaxStep(max_step, step):
            next_p.append([y+dy, x+dx, step+1])
            field[y+dy][x+dx] = "*"
            visited[y+dy][x+dx] = True

for i in range(h):
    print(*field[i], sep="")

