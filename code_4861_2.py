# 4861. [파이썬 S/W 문제해결 기본] 3일차 - 회문
# 8/16

import sys

sys.stdin = open('sample.txt')

# m 이 홀수
def odd(alp, n, m):
    c = m // 2
    for i in range(n):
        for j in range(c, n - c):
            if alp[i][j - c : j] == alp[i][j + c : j : -1]:
                print(*(alp[i][j - c : j + c + 1]), sep='')
                break


# m 이 짝수
def even(alp, n, m):
    c = m // 2
    for i in range(n):
        for j in range(c, n - c + 1):
            if alp[i][j - c : j] == alp[i][j + c - 1 : j - 1 : -1]:
                print(*(alp[i][j - c : j + c]), sep='')
                break


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

    print(f'#{test_case} ', end='')

    # m 이 홀수
    if m % 2 != 0:
        odd(alp, n, m)
        odd(alp2, n, m)

    # m 이 짝수
    else:
        even(alp, n, m)
        even(alp2, n, m)
