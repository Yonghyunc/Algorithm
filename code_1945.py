# 1945. 간단한 소인수분해


t = int(input())

for test_case in range(1, t + 1):
    num = int(input())

    pf = [2, 3, 5, 7, 11]
    div_count = [0] * 5

    for idx, pf in enumerate(pf):
        while num % pf == 0:
            div_count[idx] += 1

    # print(*(div_count))

    # print(f'#{test_case} {div_count}')
