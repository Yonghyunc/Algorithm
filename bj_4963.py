# 4963. 섬의 개수

# 백준에서 발생하는 재귀 깊이 관련 런타임 에러를 해결하기 위해 재귀 깊이를 더 할당해줌
import sys
sys.setrecursionlimit(100000)


def dfs(x, y):
    visited[x][y] = True

    # 델타 이동
    for v in range(8):
        nx = x + dx[v]
        ny = y + dy[v]

        # 범위를 벗어나지 않고, 방문기록이 없으며, 배추가 존재하는 곳
        if 0 <= nx < h and 0 <= ny < w and not visited[nx][ny] and chart[nx][ny] == 1:
            dfs(nx, ny)


# 입력으로 0 0 을 받을 때까지 반복
while True:
    # w 너비, h 높이
    w, h = map(int, input().split())

    if w != 0 and h != 0:

        chart = [list(map(int, input().split())) for _ in range(h)]
        visited = [[False] * w for _ in range(h)]

        # 상하좌우 대각선
        dx = [-1, 1, 0, 0, -1, 1, -1, 1]
        dy = [0, 0, -1, 1, -1, 1, 1, -1]

        island = 0

        for i in range(h):
            for j in range(w):
                if not visited[i][j] and chart[i][j] == 1:
                    dfs(i, j)
                    island += 1

        print(island)

    else:
        break