# 백준 10158. 개미

# 시간초과

w, h = map(int, input().split())
p, q = map(int, input().split())
t = int(input())


move_p = "left"
move_q = "up"

for i in range(t):

    if move_p == "left":
        if 0 < p < w:
            p += 1
        else:
            p -= 1
            move_p = "right"

    else:
        if 0 < p < w:
            p -= 1
        else:
            p += 1
            move_p = "left"

    if move_q == "up":
        if 0 < q < h:
            q += 1
        else:
            q -= 1
            move_q = "down"

    else:
        if 0 < q < h:
            q -= 1
        else:
            q += 1
            move_q = "up"


print(p, q)