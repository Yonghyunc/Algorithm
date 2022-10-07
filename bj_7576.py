# 백준 7576. 토마토

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(x, y):
    queue = []
    for i in range(m):
        for j in range(n):
            if box[i][j] == 1:
                queue.append((i, j))

    while queue:
        x, y = queue.pop(0)
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if 0 <= nx < m and 0 <= ny < n:
                if box[nx][ny] == 0:
                    queue.append((nx, ny))
                    box[nx][ny] = 1






n, m = map(int, input().split())        # 세로, 가로
box = [list(map(int, input().split())) for _ in range(m)]

