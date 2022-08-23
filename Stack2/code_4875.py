# 4875. [파이썬 S/W 문제해결 기본] 5일차 - 미로
# 8/23

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def dfs(arr, x, y):
    global success
    visited[x][y] = True    # 지나온 자리 표시

    if success == 1:        # 함수를 빠져나감
        return

    for k in range(4):      # 델타이동을 통해 경로 탐색
        x2 = x + dx[k]
        y2 = y + dy[k]

        if 0 <= x2 < n and 0 <= y2 < n:       # 인덱스 범위 내
            if arr[x2][y2] == 3:              # 도착점을 찾으면
                success = 1                   # success = 1
                return

            elif arr[x2][y2] == 0 and not visited[x2][y2]:     # 지나가지 않은 0이면
                dfs(arr, x2, y2)                               # 그 위치에서 4방향 탐색 가능하도록 함수 적용


for test_case in range(1, int(input()) + 1):
    n = int(input())
    maze = [list(map(int, input())) for _ in range(n)]
    visited = [[False] * n for _ in range(n)]
    success = 0

    # 출발점 찾기
    for i in range(n):
        for j in range(n):
            if maze[i][j] == 2:
                sx = i
                sy = j

    # 출발점에서부터 함수 실행
    dfs(maze, sx, sy)

    # 성공여부 출력
    print(f'#{test_case} {success}')





