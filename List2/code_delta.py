# 연습문제 : 델타검색
# 8/10 일차 문제
# 8/11 해결


import random


arr = [[0] * 5 for _ in range(5)]

for i in range(5):
    for j in range(5):
        arr[i][j] = random.randrange(1, 26)

di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]
abs_sum = 0

for i in range(5):
    for j in range(5):
        close = {0}
        if 0 <= i < 5 and 0 <= j < 5:

            for k in range(4):
                dx = i + di[k]
                dy = j + dj[k]

                if dx < 0 or dx > 4:
                    dx = i - di[k]

                if dy < 0 or dy > 4:
                    dy = j - dj[k]

                close.add(arr[dx][dy])
                dx = i
                dx = j
    print(close)
