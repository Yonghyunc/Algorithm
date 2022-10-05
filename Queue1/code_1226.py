# 1226. [S/W 문제해결 기본] 7일차 - 미로1


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(x, y):
    global ans
    queue = [[x, y]]
    visited = [[False] * 16 for _ in range(16)]

    while queue:
        x, y = queue.pop(0)
        visited[x][y] = True

        for d in range(4):
            nx, ny = x + dx[d], y + dy[d]
            if 0 <= nx < 16 and 0 <= ny < 16:
                if not visited[nx][ny] and maze[nx][ny] == 0:
                    visited[nx][ny] = True
                    queue.append([nx, ny])

                if maze[nx][ny] == 3:
                    ans = 1
                    return



for _ in range(10):
    tc = int(input())
    maze = [list(map(int, input())) for _ in range(16)]
    ans = 0

    for i in range(16):
        for j in range(16):
            if maze[i][j] == 2:
                bfs(i, j)
    print(f'#{tc} {ans}')