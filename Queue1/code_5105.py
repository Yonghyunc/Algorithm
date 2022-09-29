# 5105. [파이썬 S/W 문제해결 기본] 6일차 - 미로의 거리

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(x, y):
    queue = [[x, y]]

    while queue:
        x, y = queue.pop(0)
        visited[x][y] = True

        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if 0 <= nx < n and 0 <= ny < n:
                if not visited[nx][ny] and maze[nx][ny] == 0:
                    queue.append([nx, ny])
                    visited[nx][ny] = True
                    distance[nx][ny] = distance[x][y] + 1           # 이동거리

                if maze[nx][ny] == 3:                               # 도착점을 찾으면
                    return distance[x][y]                           # 그 이전 지점의 이동거리를 반환


for tc in range(1, int(input()) + 1):
    n = int(input())
    maze = [list(map(int, input())) for _ in range(n)]
    visited = [[False] * n for _ in range(n)]                       # 방문 여부
    distance = [[0] * n for _ in range(n)]                          # 출발점에서 해당 지점까지의 이동거리
    for i in range(n):
        for j in range(n):
            if maze[i][j] == 2:
                ans = bfs(i, j)                                     # maze[i][j]가 시작점
    if ans:                                                         # 값이 있으면 해당 값 출력
        print(f'#{tc} {ans}')
    else:                                                           # 값이 존재하지 않으면 0 출력
        print(f'#{tc} 0')
