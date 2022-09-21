# 완전 검색을 적용한 Baby Gin 검사

'''
9
111456
123123
233677
112233
333333
123456
667767
054060
101123
'''


def baby_gin(i):
    global result

    if i == len(card):
        tri = 0
        run = 0
        # triple 셋과 run 셋 여부 확인
        for k in range(0, 4, 3):
            if card[0 + k] == card[1 + k] == card[2 + k]:
                tri += 1
            elif card[0 + k] + 1 == card[1 + k] and card[1 + k] + 1 == card[2 + k]:
                run += 1
        if tri + run == 2:
            result = True
            return

    # 선택 정렬
    for j in range(i, len(card)):
        if card[j] < card[i]:
            card[i], card[j] = card[j], card[i]
        baby_gin(i + 1)
        card[j], card[i] = card[i], card[j]


n = int(input())
for tc in range(1, n + 1):
    card = list(map(int, input()))
    result = False
    baby_gin(0)
    print(f'#{tc} {result}')