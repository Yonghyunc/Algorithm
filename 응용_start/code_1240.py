# 1240. [S/W 문제해결 응용] 1일차 - 단순 2진 암호코드

import sys
sys.stdin = open('input.txt')


secret = {
    '0001101': 0,
    '0011001': 1,
    '0010011': 2,
    '0111101': 3,
    '0100011': 4,
    '0110001': 5,
    '0101111': 6,
    '0111011': 7,
    '0110111': 8,
    '0001011': 9,
}

code = ['0001101', '0011001', '0010011',
        '0111101', '0100011', '0110001',
        '0101111', '0111011', '0110111', '0001011']

for tc in range(1, int(input()) + 1):

    n, m = map(int, input().split())
    arr = [input() for _ in range(n)]
    key = []

    x = 0
    y = m - 1
    # 암호코드가 1로 끝나므로, 뒤에서부터 탐색
    while x < n and y >= 0:
        if len(key) == 8:  # 암호 찾았을 때
            break

        sk = False

        if arr[x][y:y - 7:-1][::-1] in code:
            for k in range(5):
                if arr[x + k][y:y - 7:-1][::-1] == arr[x][y:y - 7:-1][::-1]:      # 암호 배열 완성
                    sk = True
                else:
                    sk = False
            if sk:
                key.insert(0, secret.get(arr[x][y:y - 7:-1][::-1]))
                y -= 7
            else:
                y -= 1

        else:
            y -= 1

        if y - 7 < 0:       # 다음 행으로 이동
            x += 1
            y = m - 1

    odd = 0
    even = 0
    for i in range(8):
        if i % 2 != 0 :         # 짝수
            even += key[i]
        else:                   # 홀수
            odd += key[i]

    if (odd * 3 + even) % 10 == 0:
        print(f'#{tc} {even + odd}')
    else:
        print(f'#{tc} 0')

# 굳이 딕셔너리 안 쓰고 인덱스를 써도 될 듯

# 굳이 딕셔너리를 사용하지 않고, 리스트의 인덱스 값으로 암호를 반환

code = ['0001101', '0011001', '0010011',
        '0111101', '0100011', '0110001',
        '0101111', '0111011', '0110111', '0001011']

for tc in range(1, int(input()) + 1):

    n, m = map(int, input().split())
    arr = [input() for _ in range(n)]
    key = []

    x = 0
    y = m - 1
    while x < n and y >= 0:
        if len(key) == 8:  # 암호 찾았을 때
            break

        sk = False

        if arr[x][y:y - 7:-1][::-1] in code:
            for k in range(5):
                if arr[x + k][y:y - 7:-1][::-1] == arr[x][y:y - 7:-1][::-1]:      # 암호 배열 완성
                    sk = True
                else:
                    sk = False
            if sk:
                key.insert(0, code.index(arr[x][y:y - 7:-1][::-1]))
                y -= 7
            else:
                y -= 1

        else:
            y -= 1

        if y - 7 < 0:       # 다음 행으로 이동
            x += 1
            y = m - 1

    odd = 0
    even = 0
    for i in range(8):
        if i % 2 != 0 :         # 짝수
            even += key[i]
        else:                   # 홀수
            odd += key[i]

    if (odd * 3 + even) % 10 == 0:
        print(f'#{tc} {even + odd}')
    else:
        print(f'#{tc} 0')
