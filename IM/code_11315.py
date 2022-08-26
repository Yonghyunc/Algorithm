# 11315. 오목 판정

for test_case in range(1, int(input()) + 1):
    n = int(input())
    omok = [input() for _ in range(n)]

    success = "NO"
    for i in range(n):
        stone_h = 0
        stone_v = 0
        for j in range(n):
            if omok[i][j] == 'o':
                stone_h += 1
            else:
                stone_h = 0

            if omok[j][i] == 'o':
                stone_v += 1
            else:
                stone_v = 0

            if stone_h >= 5 or stone_v >= 5:
                success = "YES"
                break

    for i in range(n - 5):
        stone_c1 = 0
        stone_c2 = 0
        for c in range(i, n):
            if omok[c][c] == 'o':
                stone_c1 += 1
            else:
                stone_c1 = 0

            if omok[c][n - c - 1] == 'o':
                stone_c2 += 1
            else:
                stone_c2 = 0

            if stone_c1 >= 5 or stone_c2 >= 5:
                success = "YES"
                break

    print(f'#{test_case} {success}')