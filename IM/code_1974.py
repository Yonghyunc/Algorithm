# 1974. 스도쿠 검증

for test_case in range(1, int(input()) + 1):
    sudoku = [list(map(int, input().split())) for _ in range(9)]
    result = 1

    # 가로 세로 만족여부 확인
    for i in range(9):
        horizon = []
        vertical = []
        for j in range(9):
            if sudoku[i][j] in horizon:
                result = 0
                break
            horizon.append(sudoku[i][j])
            if sudoku[j][i] in vertical:
                result = 0
                break
            vertical.append(sudoku[j][i])

    # 3 X 3 상자 만족여부 확인
    for x in range(0, 9, 3):
        for y in range(0, 9, 3):
            box = []
            for i in range(3):
                for j in range(3):
                    if sudoku[x + i][y + j] in box:
                        result = 0
                        break
                    box.append(sudoku[x + i][y + j])

    print(f'#{test_case} {result}')