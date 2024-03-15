from collections import deque

h, w = map(int, input().split())

field = [list(input()) for _ in range(h)]

ans = 0
delta = [[0, -1], [1, 0], [0, 1], [-1, 0]]

for i in range(h):
    for j in range(w):
        if field[i][j] == ".":
            ans += 1

            next_ps = deque()

            next_y = i
            next_x = j
            field[next_y][next_x] = ans
            next_ps.append([next_y, next_x])

            while next_ps:
                now_p = next_ps.pop()
                now_y = now_p[0]
                now_x = now_p[1]
                for dy, dx in delta:
                    next_y = now_y + dy
                    next_x = now_x + dx
                    if 0 <= next_y < h and 0 <= next_x < w and field[next_y][next_x] == ".":
                        field[next_y][next_x] = ans
                        next_ps.append([next_y, next_x])

print(ans)

#for fieldi in field:
#    print(fieldi)
