# 2001. 파리 퇴치

t = int(input())

for test_case in range(1, t + 1):

    n, m = map(int, input().split())

    arr = [list(map(int, input().split())) for _ in range(n)]

    max_fly = 0

    for i in range(n - m + 1):
        for j in range(n - m + 1):

            fly = 0

            for x in range(m):
                for y in range(m):

                    fly += arr[i + x][j + y]

            if max_fly < fly:
                max_fly = fly

    print(f'#{test_case} {max_fly}')

