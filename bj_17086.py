# 백준 17086. 아기 상어 2

from collections import deque

dx = [-1, 1, 0, 0, -1, 1, -1, 1]
dy = [0, 0, -1, 1, -1, -1, 1, 1]


def distance(x, y):
    dis_list = []

    queue = deque()
    queue.append((x, y, 1))

    visited = [[0] * m for _ in range(n)]
    visited[x][y] = 1

    while queue:
        nx, ny, dis = queue.popleft()
        # print(nx, ny, dis)
        for d in range(8):
            nx += dx[d]
            ny += dy[d]
            if 0 <= nx < n and 0 <= ny < m:
                if visited[nx][ny] == 0 and arr[nx][ny] == 0:
                    visited[nx][ny] = dis
                    queue.append((nx, ny, dis + 1))
                elif arr[nx][ny] == -1:
                    dis_list.append(dis)
                    print(dis)

        print(visited)


    if dis_list:
        min_dis.append(min(dis_list))




n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

min_dis = []

for i in range(n):
    for j in range(m):
        if arr[i][j] == 1:
            arr[i][j] = -1
# print(arr)

for i in range(n):
    for j in range(m):
        distance(i, j)

print(min_dis)

