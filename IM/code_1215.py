# 1215. [S/W 문제해결 기본] 3일차 - 회문1

# for test_case in range(1, 11):
n = int(input())

board = [input() for _ in range(8)]

cir = 0

# 가로 회문 탐색
for i in range(8):
    for j in range(8 - n + 1):
        word = board[i][j:j + n]
        if word == word[::-1]:
            cir += 1

# 세로 회문 탐색
for i in range(8):
    for j in range(8 - n + 1):
        word = ''
        for k in range(n):
            word += board[j + k][i]
        if word == word[::-1]:
            cir += 1
print(cir)
    # print(f'#{test_case} {cir}')