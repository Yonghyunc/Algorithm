# 백준 10158. 개미

# 델타이동으로 풀면 시간초과...!

w, h = map(int, input().split())
p, q = map(int, input().split())
t = int(input())

visited = [[False] * (h + 1) for _ in range(w + 1)]

dx = [1, -1, -1, -1]
dy = [1, 1, -1, 1]


d = 0
end = False
while not end and t > 0:
    can = False
    cnt = 0
    while cnt <= 4 and not end:

        if 0 <= p + dx[d] <= w and 0 <= q + dy[d] <= h:
            if not visited[p + dx[d]][q + dy[d]]:
                # print(p + dx[d], q + dy[d], t - 1)
                p, q = p + dx[d], q + dy[d]
                visited[p][q] = True
                # print(p, q)
                t -= 1
                can = True
                if t == 0:
                    print(p, q)
                    end = True
        else:
            d += 1
            cnt += 1

        if d > 3:
            d = 0

        if not can and cnt == 4:
            break

    p, q = p - dx[d], q - dy[d]
    t -= 1



