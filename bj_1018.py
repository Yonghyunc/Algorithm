# 백준 1018 : 체스판 다시 칠하기

n, m = map(int, input().split())
board = [input() for _ in range(n)]

min_change = 100000
for i in range(n - 7):
    for j in range(m - 7):
        chess = [[] * 8 for _ in range(8)]

        for x in range(8):
            for y in range(8):
                chess[x] += board[i + x][j + y]

        col = ['B', 'W']
        # 블랙 시작, 화이트 시작 2가지 케이스
        for t in range(2):
            change = 0
            if chess[0][0] != col[t]:
                chess[0][0] = col[t]
                change += 1

            for a in range(7):
                for b in range(7):
                    # 블랙일 때,
                    if chess[a][b] == 'B':
                        # 옆 항목 확인
                        if chess[a][b + 1] != 'W':
                            change += 1
                            chess[a][b + 1] = 'W'
                        # 아래 항목 확인
                        if chess[a + 1][b] != 'W':
                            change += 1
                            chess[a + 1][b] = 'W'

                    # 화이트일 때,
                    elif chess[a][b] == 'W':
                        if chess[a][b + 1] != 'B':
                            change += 1
                            chess[a][b + 1] = 'B'
                        # 아래 항목 확인
                        if chess[a + 1][b] != 'B':
                            change += 1
                            chess[a + 1][b] = 'B'

            if chess[7][6] == 'W':
                if chess[7][7] == 'W':
                    change += 1
            else:
                if chess[7][7] == 'B':
                    change += 1

            print(change)
            if min_change > change:
                min_change = change

print(min_change)


'''
예제 4번이 왜 32로 나올까...
--> 맨 마지막 chess[7][7]을 확인 못함
'''