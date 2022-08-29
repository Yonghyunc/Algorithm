# 백준 2578 : 빙고

# 빙고판
board = [list(map(int, input().split())) for _ in range(5)]

# 사회자가 호명하는 번호
call = []
for _ in range(5):
    ca = list(map(int, input().split()))
    for i in range(5):
        call.append(ca[i])

# 한 리스트 내에 나올 수 있는 빙고 케이스 전부 담기
cross1 = []
cross2 = []
for x in range(5):
    vertical = []
    for y in range(5):
        vertical.append(board[y][x])
    board.append(vertical)
    cross1.append(board[x][x])
    cross2.append(board[x][- x - 1])
board.append(cross1)
board.append(cross2)


cnt = 0             # 호명 횟수
breaker = False     # 종료 조건

for i in range(25):     # 최대 호명만큼
    if breaker:         # 조건 만족 시 종료
        break
    bingo = 0
    cnt += 1
    for x in range(12):         # 만족할 수 있는 빙고 수
        if breaker:
            break
        for y in range(5):
            if call[i] == board[x][y]:
                board[x][y] = 0

        if board[x] == [0, 0, 0, 0, 0]:
            bingo += 1

        if bingo == 3:
            breaker = True

print(cnt)
