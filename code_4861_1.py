# 4861. [파이썬 S/W 문제해결 기본] 3일차 - 회문
# 8/16

import sys

sys.stdin = open('sample.txt')

t = int(input())

for test_case in range(1, t + 1):
    n, m = map(int, input().split())

    alp = [0] * n

    for i in range(n):
        alp[i] = " ".join(input())
        alp[i] = alp[i].split()

    alp2 = []
    x = ''
    for i in range(n):
        for j in range(n):
            x += alp[j][i]
        alp2.append(x)
        x = ''

    c = m // 2

    # m 이 홀수
    if m % 2 != 0:
        # 가로 회문
        for i in range(n):
            for j in range(c, n - c):
                if alp[i][j - c : j] == alp[i][j + c : j : -1]:
                    print(f'#{test_case} ', *(alp[i][j - c : j + c + 1]), sep='')
                    break
        else:
            for i in range(n):
                for j in range(c, n - c):
                    if alp2[i][j - c : j] == alp2[i][j + c : j : -1]:
                        print(f'#{test_case} ', *(alp2[i][j - c : j + c + 1]), sep='')
                        break

        # else:
        #     for j in range(n):
        #         for i in range(c, n - c):
        #             if alp[i - c : i][j] == alp[i + c : i : -1][j]:
        #                 print(f'#{test_case} ', *(alp[i - c : i + c + 1][j]), sep='')
        #                 exit()

    # m 이 짝수
    else:
        # 가로 회문
        for i in range(n):
            for j in range(c, n - c + 1):
                if alp[i][j - c : j] == alp[i][j + c - 1 : j - 1 : -1]:
                    print(f'#{test_case} ', *(alp[i][j - c : j + c]), sep='')
                    break

        # 세로 회문
        else:
            for i in range(n):
                for j in range(c, n - c + 1):
                    if alp2[i][j - c : j] == alp2[i][j + c - 1 : j - 1 : -1]:
                        print(f'#{test_case} ', *(alp2[i][j - c : j + c]), sep='')
                        break
        # else:
        #     for j in range(n):
        #         for i in range(c, n - c + 1):
        #             if alp[i - c : i][j] == alp[i + c - 1 : i - 1 : -1][j]:
        #                 print(f'#{test_case} ', *(alp[i - c : i + c][j]), sep='')
        #                 exit()
