# 4875. [파이썬 S/W 문제해결 기본] 5일차 - 미로
# 8/23
# 실패작^^

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def dfs(arr, x, y):
    global success
    visited[x][y] = True

    if success == 1:  # 함수를 빠져나감
        return

    for k in range(4):  # 델타이동을 통해 경로 탐색
        x = x + dx[k]
        y = y + dy[k]
        print(x, y)

        if 0 <= x < n and 0 <= y < n:  # 인덱스 범위 내
            if arr[x][y] == 3:  # 도착점을 찾으면
                success = 1  # success = 1
                return

            elif arr[x][y] == 0 and not visited[x][y]:  # 지나가지 않은 0이면
                dfs(arr, x, y)  # 그 위치에서 4방향 탐색 가능하도록 함수 적용
                '''
                함수를 빠져나온 뒤 기존 x,y 값으로 돌아가는 코드가 없음
                dfs(maze, 0, 3)을 빠져나온 뒤
                dfs(maze, 1, 3)함수의 for문을 계속도는데, 
                델타이동이 1,3이 아닌 0,3에서 이루어지게 됨
                '''

            # 지나가지 않은 0이 아니거나, 3이 아닐 때
            else:
                x = x - dx[k]
                y = y - dy[k]

        # 인덱스 범위 벗어나면 이전 좌표 값으로 돌아감
        else:
            x = x - dx[k]
            y = y - dy[k]


for test_case in range(1, int(input()) + 1):
    n = int(input())
    maze = [list(map(int, input())) for _ in range(n)]
    visited = [[False] * n for _ in range(n)]
    stack = []
    success = 0

    for i in range(n):
        for j in range(n):
            if maze[i][j] == 2:
                sx = i
                sy = j
    dfs(maze, sx, sy)
    print(success)





