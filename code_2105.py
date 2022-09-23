# 2105. [모의 SW 역량테스트] 디저트 카페


dx = [1, -1, -1, 1]
dy = [1, 1, -1, -1]


def eat(x, y, d, yummy):
    print(x, y, d)
    global max_desert

    yummy.append(desert[x][y])
    if d > 3:
        return

    if x == stx and y == sty and yummy:
        print(yummy)
        if len(yummy) > max_desert:
            max_desert = len(yummy)
        return

    if 0 <= x + dx[d] < n and 0 <= y + dy[d] < n:       # 이동시킨 값이 범위 내에 위치하면
        if desert[x + dx[d]][y + dy[d]] not in yummy:
            print('안쪽 if문')
            eat(x + dx[d], y + dy[d], d)
        else:
            print('안쪽 else문')
            eat(x, y, d + 1)

    print('바깥 else문')
    eat(x, y, d + 1)


# for tc in range(1, int(input()) + 1):
n = int(input())

desert = [input().replace(' ', '') for _ in range(n)]
max_desert = 0
for i in range(1, n - 1):
    for j in range(n - 2):
        stx = i
        sty = j
        eat(i, j, 0, [])
print(max_desert)