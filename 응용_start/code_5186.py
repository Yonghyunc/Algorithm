# 5186. [파이썬 S/W 문제해결 구현] 1일차 - 이진수2

for tc in range(1, int(input()) + 1):

    n = float(input())
    i = -1
    binary = []
    while True:
        if n >= 2 ** i:
            binary.append(1)
            n -= 2 ** i
        else:
            binary.append(0)
        i -= 1

        if n == 0 or len(binary) > 12:
            break

    print(f'#{tc} ', end='')
    if len(binary) > 12:
        print('overflow')
    else:
        print(*binary, sep='')
