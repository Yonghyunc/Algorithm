# 5247. [파이썬 S/W 문제해결 구현] 6일차 - 연산


cal =[
    lambda x: x * 2,
    lambda x: x + 1,
    lambda x: x - 10,
    lambda x: x - 1,
]


def calculator(n, m, cnt):
    print('n', n, 'cnt', cnt)
    # print(already)
    global min_cnt

    if n == m:
        if cnt < min_cnt:
            min_cnt = cnt
        return

    if cnt > min_cnt:
        return

    cnt += 1

    # visited = [False] * 4
    for i in range(4):
        # if i < 2:       # 숫자가 커지는 연산
        if 0 < cal[i](n) <= m + 10:
            if i < 2 and cal[i](n) > m * 2:
                continue
            if i >= 2 and cal[i](n) < m - 10:
                continue
            # if i == 1 and cal[i](n) < m // 2:
            #     continue
            # visited[i] = True
            already.append(cal[i](n))
            calculator(cal[i](n), m, cnt)
        # if i >= 2:
        #     if m < cal[i](n) and (cal[i](n) not in already) and not visited[i]:
        #         visited[i] = True
        #         already.append(cal[i](n))
        #         cnt += 1
        #         calculator(cal[i](n), m, cnt)






# for tc in range(1, int(input()) + 1):
n, m = map(int, input().split())
min_cnt = m // n
already = []
calculator(n, m, 0)
print(min_cnt)
