# 프로그래머스 77484. 로또의 최고 순위와 최저 순위


def solution(lottos, win_nums):
    lottos.sort()
    cnt = lottos.count(0)
    if cnt == 6:
        return [1, 6]
    win = 0
    for i in range(6):
        if lottos[i] != 0:
            if lottos[i] in win_nums:
                win += 1

    low = 7 - win
    high = 7 - (win + cnt)

    if low > 6:
        low = 6
    if high > 6:
        high = 6

    return [high, low]

lottos =[45, 4, 35, 20, 3, 9]
win_nums = [20, 9, 3, 45, 4, 35]
print(solution(lottos, win_nums))