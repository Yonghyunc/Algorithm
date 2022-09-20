# 10726. 이진수 표현

for tc in range(1, int(input()) + 1):

    n, m = map(int, input().split())

    # 1. m의 이진수 표현
    binary = []
    s = 27
    while s >= 0:
        if m >= 2 ** s:
            binary.append(1)
            m = m - 2 ** s
        else:
            if binary:
                binary.append(0)
        s -= 1

    # 2. 마지막 n 비트가 1로 켜져있는지 확인
    light = 'ON'
    if len(binary) < n:
        light = 'OFF'
    else:
        for i in range(1, n + 1):
            if binary[-i] != 1:
                light = 'OFF'
    print(f'#{tc} {light}')
