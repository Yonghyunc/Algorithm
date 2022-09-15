# 1232. [S/W 문제해결 기본] 9일차 - 사칙연산


def cal_postorder(k):
    global result
    if 0 < k <= n:
        a = cal_postorder(ch1[k])
        b = cal_postorder(ch2[k])
        if point[k] == '+':
            result = a + b
        elif point[k] == '-':
            result = a - b
        elif point[k] == '*':
            result = a * b
        elif point[k] == '/':
            result = a / b
        else:
            result = point[k]
    return result


for tc in range(1, 11):
    n = int(input())        # 정점의 개수

    point = [0] * (n + 1)   # 정점의 값
    ch1 = [0] * (n + 1)
    ch2 = [0] * (n + 1)

    for _ in range(n):
        p, v, *con = input().split()
        if v in ['+', '-', '*', '/']:
            point[int(p)] = v
            ch1[int(p)] = int(con[0])
            ch2[int(p)] = int(con[1])
        else:
            point[int(p)] = int(v)

    result = 0
    cal_postorder(1)
    print(f'#{tc}', end=" ")
    print("{0:.0f}".format(result))