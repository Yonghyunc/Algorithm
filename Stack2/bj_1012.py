# 1012. 유기농 배추

# 백준에서 발생하는 재귀 깊이 관련 런타임 에러를 해결하기 위해 재귀 깊이를 더 할당해줌
import sys
sys.setrecursionlimit(100000)


# 재귀 함수
# if문을 만족하지 않을 시 for문을 돌고, for문을 다 돌아도 만족을 하지 않을 시 현재 재귀 함수를 빠져나가 상위 재귀 함수의 for문을 돈다.
# 이 과정을 반복
def dfs(x, y):
    visited[x][y] = True

    # 델타 이동
    for v in range(4):
        nx = x + dx[v]
        ny = y + dy[v]

        # 범위를 벗어나지 않고, 방문기록이 없으며, 배추가 존재하는 곳
        if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and cab[nx][ny] == 1:
            dfs(nx, ny)


t = int(input())

for test_case in range(1, t + 1):
    m, n, k = map(int, input().split())
    cab = [[0] * m for _ in range(n)]
    visited = [[False] * m for _ in range(n)]

    # 배추 위치 표시
    for _ in range(k):
        a, b = map(int, input().split())
        cab[b][a] = 1

    # 상하좌우
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    worm = 0

    # 1. 이차원 리스트를 행 순회
    for i in range(n):
        for j in range(m):
            # 벌레가 없는 배추
            if not visited[i][j] and cab[i][j] == 1:
                # 2. 1이면 DFS 시작
                dfs(i, j)
                worm += 1

    print(worm)
