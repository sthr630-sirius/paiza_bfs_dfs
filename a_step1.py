h, w = map(int, input().split())
y, x = map(int, input().split())

delta = [[-1, 0], [0, -1], [0, 1], [1, 0]]

field = [["."]*w for _ in range(h)]
visited = [[False]*w for _ in range(h)]
next_p = []

"""
p = [y, x, step]
"""
next_p.append([y, x, 0])
field[y][x] = "*"
visited[y][ x] = True

while next_p:
    np = next_p.pop(0)
    y = np[0]
    x = np[1]
    step = np[2]

    for dy, dx in delta:
        if 0<= y+dy and y+dy<h and 0<=x+dx and x+dx<w and visited[y+dy][x+dx] == False and step<1:
            next_p.append([y+dy, x+dx, step+1])
            field[y+dy][x+dx] = "*"
            visited[y+dy][x+dx] = True

for i in range(h):
    print("".join(field[i]))

