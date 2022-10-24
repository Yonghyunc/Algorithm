# 백준 16236. 아기 상어

n = int(input())

sea = [list(map(int, input().split())) for _ in range(n)]
print(sea)

for x in range(n):
    for y in range(n):
        if sea[x][y] == 9:
            sx, sy = x, y

shark = 2
fish_cnt = 0
time_cnt = 0

# 상, 좌, 하, 우
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

find_queue = []
fish_queue = []
while True:
    visited = [[False] * n for _ in range(n)]
    find_queue= [(sx, sy, 0)]

    while find_queue:
        nx, ny, dis = find_queue.pop()
        visited[sx][sy] = True
        visit_cnt = 1
        for d in range(4):
            if 0 <= nx + dx[d] < n and 0 <= ny + dy[d] < n:
                if not visited[nx + dx[d]][ny + dy[d]]:
                    if sea[nx + dx[d]][ny + dy[d]] == 0 or sea[nx + dx[d]][ny + dy[d]] == shark:
                        find_queue.append((nx + dx[d], ny + dy[d], dis + 1))
                        visited[nx + dx[d]][ny + dy[d]] = True
                        visit_cnt += 1
                    elif 0 < sea[nx + dx[d]][ny + dy[d]] < shark:
                        fish_cnt += 1
                        time_cnt += dis + 1
                        sx = nx + dx[d]
                        sy = ny + dy[d]
                    else:
                        visited[nx + dx[d]][ny + dy[d]] = True
                        visit_cnt += 1
    if fish_cnt == shark:
        shark += 1
        fish_cnt = 0

    if visit_cnt == n * n:
        time_cnt = 0
        break

print(time_cnt)


