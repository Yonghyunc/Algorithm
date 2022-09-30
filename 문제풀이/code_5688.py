# 5688. 세제곱근을 찾아라

for tc in range(1, int(input()) + 1):
    n = int(input())
    x = -1
    a = 1

    while a**3 <= n:
        if a**3 != n:
            a += 1
        else:
            x = a
            break

    print(f'#{tc} {x}')
