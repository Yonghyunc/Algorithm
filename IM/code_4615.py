# 4615. 재미있는 오셀로 게임

# 상, 하, 좌, 우, 좌상, 우상, 좌하, 우하향
dx = [-1, 1, 0, 0, -1, -1, 1, 1]
dy = [0, 0, -1, 1, -1, 1, -1, 1]


def change(x, y, c):
    global end
    # 범위를 만족 시키는 경우 돌의 색깔 확인
    if 0 <= x < n and 0 <= y < n:
        # 상대의 돌인 경우
        if board[x][y] == 3 - c:
            board[x][y] = c                     # 돌 색깔 바꾸기
            color[c] += 1                       # 내 돌 개수 + 1
            color[3 - c] -= 1                   # 상대돌 개수 - 1
            change(x + dx[d], y + dy[d], c)     # 그 지점에서 같은 방향으로 한칸 이동하여 함수 실행

            # 조건을 만족하지 못했을 경우, 원래의 상태로 돌림
            if not end:
                board[x][y] = 3 - c  # 돌 색깔 바꾸기
                color[c] -= 1
                color[3 - c] += 1

        # 빈칸이 나오면 조건 불만족
        elif board[x][y] == 0:
            return

        # 사이에 위치한 상대의 돌을 바꾸고, 내 돌을 만남 => 조건 만족
        else:
            end = True
            return

    # 범위를 벗어나면 조건 불만족
    else:
        return


for tc in range(1, int(input()) + 1):

    n, m = map(int, input().split())

    # 보드판 기본 세팅
    board = [[0] * n for _ in range(n)]
    board[n//2 - 1][n//2 - 1], board[n//2][n//2] = 2, 2
    board[n//2][n//2 - 1], board[n//2 - 1][n//2] = 1, 1

    color = [0, 2, 2]       # 색깔별 돌 개수 (인덱스 번호를 돌의 색을 표현하는 숫자로 맞춤)

    for i in range(m):
        # 돌을 놓을 수 없는 곳은 입력으로 주어지지 않는다.
        y, x, c = map(int, input().split())

        # 인덱스는 입력값에서 -1 씩 해주어야 함
        x = x - 1
        y = y - 1
        board[x][y] = c
        color[c] += 1

        # 자신의 돌과 새로 놓는 돌 사이의 상대편의 돌 확인 후 색깔 체인지
        # 사이에 있는 상대편의 돌이 여러개여도 가능
        for d in range(8):
            end = False
            change(x + dx[d], y + dy[d], c)

    print(f'#{tc} {color[1]} {color[2]}')
